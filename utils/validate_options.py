#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.logger as l
import re

def strip_dquotes(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found,
    or there are less than 2 characters, return the string unchanged.
    """
    if (len(s) >= 2 and s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

def check_notifymethods(notifications):
    """
    params notifications: list of notifications
    return valid notifications within a list
    """
    notify_possibilities = ["local", "matrix", "mattermost"]
    sanitized_notifications = []
    for notif in notifications:
        notif = notif.strip()
        notif = strip_dquotes(notif)
        if notif not in notify_possibilities:
            l.logger.warning("notification method not known !")
            notifications.remove(notif)
        else:
            sanitized_notifications.append(notif)
    return sanitized_notifications


def check_PID(PID):
    """
    Basic check for PID
    :param PID integer
    :Return PID integer if > 1
    """
    PID = strip_dquotes(PID)
    try:
        PID = int(PID)
    except Exception as e:
        l.logger.critical("PID is not an integer : {}!!".format(e))
    if PID <= 1:
        l.logger.critical("PID is not a calid number : {}!!".format(e))
        raise ValueError("PID must be an integer > 1")
    return PID

def check_emails(emails):
    """
    Basic email check with regexp
    param emails
    return valid emails
    """
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    sanitized_emails = []
    for email in emails:
        email = email.strip()
        email = strip_dquotes(email)
        if not re.fullmatch(regex, email):
            emails.remove(email)
        else:
            sanitized_emails.append(email)
    return sanitized_emails

def check_matrix_server_url(matrix_server_url):
    """
    Basic matrix server URL check
    Removing 'https://' from base URL
    """
    matrix_server_url = strip_dquotes(matrix_server_url)
    if matrix_server_url.startswith('https://'):
        return matrix_server_url[8:]
    return matrix_server_url

def check_mattermost_hook_url(mattermost_hook_url):
    """
    Basic matrix server URL check
    Removing 'https://' from base URL
    """
    mattermost_hook_url = strip_dquotes(mattermost_hook_url)
    if not mattermost_hook_url.startswith('https://'):
        raise ValueError("Mattermost hook URL must start with https://")
    return matrix_server_url