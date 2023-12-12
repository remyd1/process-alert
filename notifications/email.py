#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
import ssl
from email.mime.text import MIMEText
import socket
import getpass
from utils import parse_config as cfg
from utils import validate_options as v
import utils.logger as l


def send(to, processus, content, use_email="default", \
    smtp_server=None, smtp_sender=None, smtp_password=None):

    """Send email about the ended process.

    :param to: email addresses to send to
    :param processus: the initial processus to monitor (could be PID or name)
    :param msg: full process information in json
    :param use_email: "default" or "yes" (see config file)
    :param smtp_server smtp server to use
    :param smtp_password your mail password
    :param smtp_sender "From: <user@tld.com>" field
    """

    config = cfg.parse_config()

    if not use_email:
        use_email = cfg.try_read_val(config, 'use_email', 'alerting')
    #if use_email == "no":
    #    l.logger.warn("Trying to send email but use_email is set to no")

    if not smtp_server:
        smtp_server = cfg.try_read_val(config, 'smtp_server', 'alerting')
        smtp_server = v.strip_dquotes(smtp_server)
    if not smtp_password:
        smtp_password = cfg.try_read_val(config, 'smtp_password', 'alerting')
        smtp_password = v.strip_dquotes(smtp_password)
    
    host = socket.getfqdn()
    user = getpass.getuser()
    if not smtp_sender:
        smtp_sender = cfg.try_read_val(config, 'smtp_sender', 'alerting')
        smtp_sender = v.strip_dquotes(smtp_sender)
        if not smtp_sender:
            smtp_sender = "{}@{}".format(user, host)

    
    port = 465  # Only used for SSL on a remote server

    body = content
    body += '\n\n(Automatically sent by process-alert program)'
    msg = MIMEText(body)
    msg['Subject'] = "Your program {} is finished".format(processus)
    msg['From'] = smtp_sender
    msg['To'] = ', '.join(to)

    if use_email == "default":
        # Send the message via our own SMTP server.
        with smtplib.SMTP('localhost') as server:
            logging.info('Sending email to: {}'.format(msg['To']))
            server.send_message(msg)
    else:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(smtp_sender, smtp_password)
            server.send_message(msg)