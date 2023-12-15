#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.parse_config as cfg
import json
import requests
import utils.logger as l
from utils import validate_options as v

# from https://mattermost.com/blog/mattermost-integrations-incoming-webhooks/
def send_notif(message):
    """
    :params str message: body of the message (there is no subject in messages)
    """
    config = cfg.parse_config()
    hook_url = cfg.try_read_val(config, 'mattermost_hook_url', 'alerting')
    if hook_url:
        hook_url = v.check_mattermost_hook_url(hook_url)
    else:
        l.logger.error("Could not send any Mattermost notification because mattermost_hook_url seems to be empty")
    
    headers = {"Content-Type": "application/json"}
    values = '{{ "text": "{}"}}'.format(message)
    l.logger.info(values)
    response = requests.post(hook_url, headers=headers, data=values)
    return response