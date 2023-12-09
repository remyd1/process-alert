#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

from utils import pc

import watcher.watch_proc as ww
import notifications.alertmanager as nal
import utils.process_lookup_infos as look
import utils.logger as l




def manage_process(process, processType):
    
    if processType == "PID":
        try:
            pid = int(process)
            prog = look.lookup_process_from_pid(pid)
        except Exception as e:
            raise e
    else:
        prog = look.lookup_process_from_name(process)    
    return prog


if __name__ == '__main__':
    config = pc.parse_config()
    process = pc.try_read_val(config, 'process_name', 'general')
    processType = "name"
    if not process:
        process = pc.try_read_val(config, 'process_pid', 'general')
        processType = "PID"
    use_email = pc.try_read_val(config, 'use_email', 'alerting')
    if use_email in ["yes", "default"]:
        email = pc.try_read_val(config, 'smtp_receiver', 'alerting')
    else:
        email = None
    notifymethod = pc.try_read_val(config, 'notifymethod', 'alerting')
    prog = manage_process(process, processType)
    msg = look.gather_informations(prog)
    asyncio.run(ww.pswaiter(prog))
    nal.send_alert(email, notifymethod, processType, process)



    
