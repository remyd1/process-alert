#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.parse_config as cfg
import json
import requests
import utils.logger as l

# from https://mattermost.com/blog/mattermost-integrations-incoming-webhooks/
def send_notif(message):
    """
    :params str message: body of the message (there is no subject in messages)
    """
    config = cfg.parse_config()
    
    hook_url = config['alerting']['mattermost_hook_url']
    
    headers = {"Content-Type": "application/json"}
    values = '{{ "text": "{}"}}'.format(message)
    l.logger.info(values)
    response = requests.post(hook_url, headers=headers, data=values)
    return response