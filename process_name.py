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
def name(name: str = typer.Argument(..., help="Process name"), \
        email: List[str] = typer.Option(None, \
        help="Email address(es) to send process report"), \
        notifymethod: str = typer.Option("local", help="Your additionnal notify option")):

    typer.secho(f"Searching for process name(s) {name}", fg=typer.colors.MAGENTA, bold=True)
    prog = lookup_pid(name)
    if not prog:
        typer.secho(f"Your program's name {name} has not been found !", \
            fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)
    typer.echo(f"Your notify option {notifymethod} will be used")

    if email:
        for m in email:
            typer.echo(f"Email address {m} will be used")
    
    msg = gather_informations(prog)

    #asyncio.run(ww.watchproc(prog))
    asyncio.run(ww.pswaiter(prog))
        
    if notifymethod == "local":
        asyncio.run(nd.desknotify("process-alert", msg))
    if email:
        ne.send(email, name, msg)
    
def gather_informations(prog):
    infos = [proc.as_dict() for proc in prog]
    msg = json.dumps(infos)
    with open('process_info.json', 'w') as f:
        f.write(msg)
    return msg

def lookup_pid(name):
    # Simple program that search process name.
    progs = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info["name"] == name:
            progs.append(proc)
            typer.secho(f"Ok. Found process PID {proc.pid}", fg=typer.colors.BLUE, bold=True)
    return progs


if __name__ == "__main__":
    app()
