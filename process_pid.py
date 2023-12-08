#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

import typer_cloup as typer

import asyncio

import watcher.watch_proc as ww
import notifications.alertmanager as nal
import utils.process_lookup_infos as look
import utils.logger as l


app = typer.Typer()

@app.command()
def num(num: int = typer.Argument(..., help="PID number"), \
        email: List[str] = typer.Option(None, \
        help="Email address(es) to send process report"), \
        notifymethod: str = typer.Option("local", help="Your additionnal notify option")):

    prog = look.lookup_process_from_pid(num)
    if not prog:
        typer.secho(f"Process PID: {num} not found !", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)
    else:
        typer.secho(f"Ok. Process PID: {num}", fg=typer.colors.BLUE, bold=True)

    typer.echo(f"Your notify option {notifymethod} will be used")

    if email:
        for m in email:
            typer.echo(f"Email address {m} will be used")
    
    msg = look.gather_informations(prog)
    
    asyncio.run(ww.pswaiter(prog))
    #asyncio.run(ww.watchproc(num))
    nal.send_alert(email, notifymethod, "PID", num)

if __name__ == "__main__":
    app()