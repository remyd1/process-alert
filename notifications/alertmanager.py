#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

import notifications.desktop_notify as nd
import notifications.matrix as matx
import notifications.mattermost as matst

import utils.logger as l


def msg_content(processType, process):
    processTitle = str(process)
    subject = "process-alert: {}".format(processTitle)
    body = "Your program with {} {} is over".format(processType, processTitle)
    body += "\nYou will find additionnal informations in process-alert*.log and process_info.json"
    return processTitle, subject, body

def send_alert(notifymethod, subject, body):
    response = None
    if "local" in notifymethod:
        asyncio.run(nd.desknotify(subject, body))
    if "matrix" in notifymethod:
        response = matx.send_notif(body)
    if "mattermost" in notifymethod:
        response = matst.send_notif(body)
    if response:
        l.logger.debug(response)

    