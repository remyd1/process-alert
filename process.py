#!/usr/bin/env python3

import typer_cloup as typer
import process_name
import pid


app = typer.Typer()

app.add_sub(process_name.app, name="process_name")
app.add_sub(pid.app, name="pid")


if __name__ == '__main__':
    app()

