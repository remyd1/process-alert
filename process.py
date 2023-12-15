#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

from utils import parse_config as cfg
from utils import validate_options as v
import watcher.watch_proc as ww
import notifications.alertmanager as nal
import notifications.email as ne
import utils.process_lookup_infos as look
import utils.logger as l
from utils import bcolors as bc




def manage_process(process, processType):
    """
    Basic method to check program using psutil
    """
    if processType == "PID":
        pid = v.check_PID(process)
        prog = look.lookup_process_from_pid(pid)
    else:
        prog = look.lookup_process_from_name(process)    
    return prog


if __name__ == '__main__':
    config = cfg.parse_config()
    process = cfg.try_read_val(config, 'process_name', 'general')
    processType = "name"
    if not process:
        process = cfg.try_read_val(config, 'process_pid', 'general')
        processType = "PID"
    use_email = cfg.try_read_val(config, 'use_email', 'alerting')
    if use_email in ["yes", "default"]:
        email_to = cfg.try_read_val(config, 'smtp_receiver', 'alerting')
        if email_to:
            email_to = email_to.split(",")
            email_to = v.check_emails(email_to)
    else:
        email_to = None
    notifymethod = cfg.try_read_val(config, 'notifymethod', 'alerting')
    if notifymethod:
        notifymethod = notifymethod.split(",")
        notifymethod = v.check_notifymethods(notifymethod)
    prog = manage_process(process, processType)
    if not prog:
        raise LookupError(f"{bc.bcolors.FAIL}Process {process} not found !!{bc.bcolors.ENDC}")
    else:
        msg = look.gather_informations(prog)
        asyncio.run(ww.pswaiter(prog))
        processTitle, subject, body = nal.msg_content(processType, process)
        if notifymethod:
            nal.send_alert(notifymethod, subject, body)
        if email_to:
            ne.send(email_to, processTitle, body, use_email, None, None, None)



    
