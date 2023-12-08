#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.parse_config as cfg
import json
import requests
from utils.matrix import MatrixClient


# from https://spec.matrix.org/v1.9/client-server-api/#put_matrixclientv3roomsroomidsendeventtypetxnid
def send_notif(message):
    """
    :params str message: body of the message (there is no subject in messages)
    """
    config = cfg.parse_config()
    
    server = config['alerting']['matrix_server_url']
    token = config['alerting']['matrix_token']
    room = config['alerting']['matrix_internal_room_id']

    matrix_client = MatrixClient(server, token, room)
    response = matrix_client.populate(message)
