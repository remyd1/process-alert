#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

import notifications.desktop_notify as nd
import notifications.email as ne
import notifications.matrix as mat

def send_alert(email, notifymethod, processType, process):

    processTitle = str(process)
    subject = "process-alert: {}".format(processTitle)
    body = "Your program with {} {} is over".format(processType, processTitle)
    body += "\nYou will find additionnal informations in process-alert*.log and process_info.json"
    if notifymethod == "local":
        asyncio.run(nd.desknotify(subject, body))
    elif notifymethod == "matrix":
        mat.send_notif(body)
    if email:
        ne.send(email, processTitle, body)