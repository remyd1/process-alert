#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

from utils import parse_config

import watcher.watch_proc as ww
import notifications.alertmanager as nal
import utils.process_lookup_infos as look
import utils.logger as l




def manage_process(process):
    
    if(isinstance(process, int)):
        prog = look.lookup_process_from_pid(process)
    else:
        prog = look.lookup_process_from_name(process)
    
    return prog

    if not prog:
        typer.secho(f"Process PID: {num} not found !", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)
    typer.echo(f"Your notify option {notifymethod} will be used")

    if email:
        for m in email:
            typer.echo(f"Email address {m} will be used")
    
    
    asyncio.run(ww.pswaiter(num))
    nal.send_alert(email, notifymethod, "PID", num)


def try_read_val(config, key, section):
    try:
        val = config[section][key]
    except Exception as e:
        raise e
    return val


if __name__ == '__main__':
    config = parse_config.parse_config()
    process = try_read_val(config, 'process_name', 'general')
    processType = "name"
    if not process:
        process = try_read_val(config, 'process_pid', 'general')
    use_email = try_read_val(config, 'use_email', 'alerting')
    if use_email in ["yes", "default"]:
        email = try_read_val(config, 'smtp_receiver', 'alerting')
    notifymethod = try_read_val(config, 'notifymethod', 'alerting')
    prog = manage_process(process)
    msg = look.gather_informations(prog)
    asyncio.run(ww.pswaiter(prog))
    nal.send_alert(email, notifymethod, processType, process)



    
