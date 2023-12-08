#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typer_cloup as typer
import process_name
import process_pid

app = typer.Typer()

app.add_sub(process_name.app, name="process_name")
app.add_sub(process_pid.app, name="process_pid")


if __name__ == '__main__':
    app()

