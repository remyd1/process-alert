#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.logger as l
import re


def check_notifymethods(notifications):
    """
    params notifications: list of notifications
    return valid notifications within a list
    """
    notify_possibilities = ["local", "matrix", "mattermost"]
    sanitized_notifications = []
    for notif in notifications:
        notif = notif.strip()
        if notif not in notify_possibilities:
            l.logger.warning("notification method not known !")
            notifications.remove(notif)
        else:
            sanitized_notifications.append(notif)
    return sanitized_notifications


def check_PID(PID):
    try:
        PID = int(PID)
    except Exception as e:
        l.logger.critical("PID is not an integer : {}!!".format(e))
    if PID <= 1:
        l.logger.critical("PID is not a calid number : {}!!".format(e))
        raise ValueError("PID must be an integer > 1")
    return PID

def check_emails(emails):
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    sanitized_emails = []
    for email in emails:
        email = email.strip()
        if not re.fullmatch(regex, email):
            emails.remove(email)
        else:
            sanitized_emails.append(email)
    return sanitized_emails
    