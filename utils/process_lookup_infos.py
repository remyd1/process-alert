#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import json
import utils.bcolors as bc

import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def gather_informations(prog):
    """
    gather informations about prog using .as_dict() psutil method

    :param prog: prog in a psutil.Process() instance
    :return msg: dictionnary of process informations
    """
    infos = [proc.as_dict() for proc in prog] if isinstance(prog, list) else \
        prog.as_dict()
    msg = json.dumps(infos)
    with open(dir_path+'/../results/process_info.json', 'w') as f:
        f.write(msg)
    return msg

def lookup_process_from_name(name):
    """
    :param name: process name to search in psutil.process_iter
    """
    progs = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info["name"] == name:
            progs.append(proc)
            print(f"{bc.bcolors.OKBLUE}Ok. Found process PID {proc.pid}{bc.bcolors.ENDC}")
    return progs

def lookup_process_from_pid(num):
    """
    :param num: process pid to search in psutil.process_iter
    """
    # a faster option would be to use:
    # psutil.pid_exists(pid)
    # but we would not have further informations
    # about the process itself
    prog = None
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info["pid"] == num:
            prog = [proc]
    return prog