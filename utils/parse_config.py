#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from pathlib import Path
from os import access, R_OK

def file_readable(path):
    """
    :Param path to a file
    check if file is readable
    """
    assert(access(file, R_OK)), f"File {file} is not readable"
    return path

def parse_config():
    """
    Parse config main function
    :Return config
    """
    config = configparser.ConfigParser()
    paths = ["config/process-alert.conf", "~/.config/process-alert.conf", \
        "/etc/process-alert/process-alert.conf"]
    for p in paths:
        path = Path(p)
        if path.is_file():
            p = file_readable(p)
            config.read(p)
            break
    return config

def try_read_val(config, key, section):
    """
    :Param configuration content, key, section
    :Return value
    """
    try:
        val = config[section][key]
    except Exception as e:
        raise e
    return val