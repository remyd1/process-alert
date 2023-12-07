
import logging
import smtplib
from email.mime.text import MIMEText
import socket
import getpass


def send(to, processus, content):
    """Send email about the ended process.

    :param to: email addresses to send to
    :param processus: the initial processus to monitor (could be PID or name)
    :param msg: full process information in json
    """
    
    host = socket.getfqdn()
    user = getpass.getuser()
    From = "{}@{}".format(user, host)

    body = content
    body += '\n\n(Automatically sent by process-alert program)'
    msg = MIMEText(body)
    msg['Subject'] = "Your program {} is finished".format(processus)
    msg['From'] = From
    msg['To'] = ', '.join(to)

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    try:
        logging.info('Sending email to: {}'.format(msg['To']))
        s.send_message(msg)
    finally:
        s.quit()