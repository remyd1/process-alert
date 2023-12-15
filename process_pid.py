#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

import typer_cloup as typer

import asyncio

from utils import validate_options as v
import watcher.watch_proc as ww
import notifications.alertmanager as nal
import notifications.email as ne
import utils.process_lookup_infos as look
import utils.logger as l


app = typer.Typer()

@app.command()
def num(num: int = typer.Argument(..., help="PID number"), \
        email_to: List[str] = typer.Option(None, \
        help="Email address(es) to send process report"), \
        notifymethod: List[str] = typer.Option(["local"], \
        help="Your additionnal notify option")):

    num = v.check_PID(num)
    prog = look.lookup_process_from_pid(num)
    if not prog:
        typer.secho(f"Process PID: {num} not found !", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)
    else:
        typer.secho(f"Ok. Process PID: {num}", fg=typer.colors.BLUE, bold=True)

    if notifymethod:
        notifymethod = v.check_notifymethods(notifymethod)
        for method in notifymethod:
            typer.echo(f"Your notify option {method} will be used")

    if email_to:
        email_to = v.check_emails(email_to)
        for m in email_to:
            typer.echo(f"Email address {m} will be used")
    
    msg = look.gather_informations(prog)
    
    asyncio.run(ww.pswaiter(prog))
    processTitle, subject, body = nal.msg_content("PID", num)
    if notifymethod:
        nal.send_alert(notifymethod, subject, body)
    if email_to:
        ne.send(email_to, processTitle, body, None, None, None, None)

if __name__ == "__main__":
    app()