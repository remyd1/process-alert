#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.parse_config as cfg
import json
import requests
from utils.matrix import MatrixClient
from utils import validate_options as v
import utils.logger as l


# from https://spec.matrix.org/v1.9/client-server-api/#put_matrixclientv3roomsroomidsendeventtypetxnid
def send_notif(message):
    """
    :params str message: body of the message (there is no subject in messages)
    """
    config = cfg.parse_config()
    matrix_server_url = cfg.try_read_val(config, 'matrix_server_url', 'alerting')
    if matrix_server_url:
        matrix_server_url = v.check_matrix_server_url(matrix_server_url)
    else:
        l.logger.error("Could not send any Matrix notification because matrix_server_url seems to be empty")
    token = cfg.try_read_val(config, 'matrix_token', 'alerting')
    if token:
        token = v.strip_dquotes(token)
    else:
        l.logger.error("Could not send any Matrix notification because matrix_token seems to be empty")
    room = cfg.try_read_val(config, 'matrix_internal_room_id', 'alerting')
    if room:
        room = v.strip_dquotes(room)
    else:
        l.logger.error("Could not send any Matrix notification because matrix_internal_room_id seems to be empty")
    
    matrix_client = MatrixClient(server, token, room)
    response = matrix_client.populate(message)
    return response
