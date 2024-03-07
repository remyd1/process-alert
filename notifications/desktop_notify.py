#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import psutil
import os
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

async def desknotify(subject, body):
    if 'DISPLAY' in os.environ or 'WAYLAND_DISPLAY' in os.environ:
        n = await notifier.send(title=subject, message=body)
        await asyncio.sleep(4)  # wait a bit before clearing notification
        await notifier.clear(n)  # removes the notification
        await notifier.clear_all()  # removes all notifications for this app
    else:
        print('No DISPLAY available; desktop local notification is not possible.')