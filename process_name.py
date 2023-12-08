#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

import typer_cloup as typer
import psutil
import asyncio
import json

import watcher.watch_proc as ww
import notifications.alertmanager as nal
import utils.process_lookup_infos as look
import utils.logger as l


app = typer.Typer()

@app.command()
def name(name: str = typer.Argument(..., help="Process name"), \
        email: List[str] = typer.Option(None, \
        help="Email address(es) to send process report"), \
        notifymethod: str = typer.Option("local", help="Your additionnal notify option")):

    typer.secho(f"Searching for process name(s) {name}", fg=typer.colors.MAGENTA, bold=True)
    prog = look.lookup_process_from_name(name)
    if not prog:
        typer.secho(f"Your program's name {name} has not been found !", \
            fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)
    typer.echo(f"Your notify option {notifymethod} will be used")

    if email:
        for m in email:
            typer.echo(f"Email address {m} will be used")
    
    msg = look.gather_informations(prog)

    #asyncio.run(ww.watchproc(prog))
    asyncio.run(ww.pswaiter(prog))
    nal.send_alert(email, notifymethod, "name", name)

if __name__ == "__main__":
    app()
