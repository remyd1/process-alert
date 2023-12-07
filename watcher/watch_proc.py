import asyncio
from watchfiles import awatch
import psutil
import logger as l


def on_terminate(proc):
    #logging.warning("process {} terminated with exit code {}".format(proc, proc.returncode))
    l.logger.warning("process {} terminated".format(proc))

async def pswaiter(pid_or_procs):
    if isinstance(pid_or_procs, int):
        pid = pid_or_procs
        p = psutil.Process(pid)
        SIG = p.wait()
        on_terminate(pid)
        #logging.warning("process {} terminated with exit code {}".format(pid, SIG))
    else:
        procs = pid_or_procs
        gone, alive = psutil.wait_procs(procs, callback=on_terminate)
    
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