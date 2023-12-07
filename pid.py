#!/usr/bin/env python3

from typing import List

import typer_cloup as typer
import psutil
import notifications.desktop_notify as nd
import notifications.email as ne
import asyncio
import watcher.watch_proc as ww
import json
import logger as l


app = typer.Typer()

@app.command()
def num(num: int = typer.Argument(..., help="PID number"), \
        email: List[str] = typer.Option(None, \
        help="Email address(es) to send process report"), \
        notifymethod: str = typer.Option("local", help="Your additionnal notify option")):

    prog = check_pid(num)
    if not prog:
        typer.secho(f"Process PID: {num} not found !", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)
    else:
        typer.secho(f"Ok. Process PID: {num}", fg=typer.colors.BLUE, bold=True)

    typer.echo(f"Your notify option {notifymethod} will be used")

    if email:
        for m in email:
            typer.echo(f"Email address {m} will be used")
    
    msg = gather_informations(prog)
    
    asyncio.run(ww.pswaiter(num))
    #asyncio.run(ww.watchproc(num))

    if notifymethod == "local":
        asyncio.run(nd.desknotify("process-alert", msg))
    if email:
        ne.send(email, str(num), msg)
    
def gather_informations(prog):
    infos = [proc.as_dict() for proc in prog] if isinstance(prog, list) else \
        prog.as_dict()
    msg = json.dumps(infos)
    with open('process_info.json', 'w') as f:
        f.write(msg)
    return msg


def check_pid(num):
    # a faster option would be to use:
    # psutil.pid_exists(pid)
    # but we would not have further informations
    # about the process itself
    prog = None
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info["pid"] == num:
            prog = proc
    return prog

if __name__ == "__main__":
    app()