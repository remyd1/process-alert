#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import psutil
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

async def desknotify(subject, body):

    n = await notifier.send(title=subject, message=body)
    
    await asyncio.sleep(4)  # wait a bit before clearing notification
    await notifier.clear(n)  # removes the notification
    await notifier.clear_all()  # removes all notifications for this app