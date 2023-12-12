#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.parse_config as cfg
import json
import requests
from utils.matrix import MatrixClient
from utils import validate_options as v


# from https://spec.matrix.org/v1.9/client-server-api/#put_matrixclientv3roomsroomidsendeventtypetxnid
def send_notif(message):
    """
    :params str message: body of the message (there is no subject in messages)
    """
    config = cfg.parse_config()
    matrix_server_url = cfg.try_read_val(config, 'matrix_server_url', 'alerting')
    matrix_server_url = v.check_matrix_server_url(matrix_server_url)
    token = cfg.try_read_val(config, 'matrix_token', 'alerting')
    token = v.strip_dquotes(token)
    room = cfg.try_read_val(config, 'matrix_internal_room_id', 'alerting')
    room = v.strip_dquotes(room)

    matrix_client = MatrixClient(server, token, room)
    response = matrix_client.populate(message)
    return response
