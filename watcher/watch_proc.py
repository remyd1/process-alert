#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
#from watchfiles import awatch
import psutil
import utils.logger as l


def on_terminate(proc):
    #logging.warning("process {} terminated with exit code {}".format(proc, proc.returncode))
    l.logger.warning("process {} terminated".format(proc))

async def pswaiter(procs):
    gone, alive = psutil.wait_procs(procs, callback=on_terminate)

"""
async def watchproc(pid_or_procs):
    if isinstance(pid_or_procs, int):
        pidstr = str(pid)
        async for changes in awatch('/proc/' + pidstr + "/"):
            print(changes)
    else:
        procs = pid_or_procs
        for proc in procs:
            pidstr = str(proc.pid)
            async for changes in awatch('/proc/' + pidstr + "/"):
                print(changes)
"""