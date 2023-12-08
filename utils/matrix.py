#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Lorenzo Carbonell <a.k.a. atareao>
# from https://github.com/atareao/pyblisher/blob/48e883e8a9f52c73253a6aaf6a1ceae4f6443c32/src/matrix.py

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import json
import requests
import utils.logger as l
from urllib.parse import quote
import time


class MatrixClient:
    def __init__(self, base_url, token, room):
        room = quote(room)
        ts = int(time.time())
        eventType = "m.room.message"
        self._url = (f"https://{base_url}/_matrix/client/v3/rooms/{room}:"
                     f"{base_url}/send/{eventType}/{ts}")
        self._headers = {"Authorization": f"Bearer {token}",
                         "Content-Type": "application/json",
                         "Accept": "application/json"}

    def populate(self, text):
        try:
            data = {
                "msgtype": "m.text",
                "body": text
            }
            response = requests.put(self._url, headers=self._headers,
                                    json=data)
            l.logger.debug("Status code: %s", response.status_code)
            l.logger.debug("Response: %s", response.text)
            if response.status_code == 200:
                return response.json()
            raise Exception(f"Error: {response.status_code}. {response.text}")
        except Exception as exception:
            l.logger.error(exception)
