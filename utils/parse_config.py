#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from pathlib import Path


def parse_config():
    config = configparser.ConfigParser()
    paths = ["config/process-alert.conf", "~/.config/process-alert.conf", \
        "/etc/process-alert/process-alert.conf"]
    for p in paths:
        path = Path(p)
        if path.is_file():
            config.read(p)
            break
    return config


def try_read_val(config, key, section):
    try:
        val = config[section][key]
    except Exception as e:
        raise e
    return val