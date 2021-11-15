from threadwrapper import *
from omnitools import def_template
import asyncio
import time


def a1(b, c=None):
    return c%b


def job_template(*args, **kwargs):
    return lambda: a1(*args, **kwargs)


times = 2**12
limit = 2**5
start = time.time()
tw = ThreadWrapper(threading.Semaphore(limit))
result = {}
for i in range(times):
    job = def_template(a1, i**2, c=i**3) or job_template(i**2, c=i**3)
    tw.add(job=job, result=result, key=i)
tw.wait()
e = time.time()-start
print(times, e, e/times)


async def a2(b, c=None):
    return c%b


start = time.time()
loop = asyncio.new_event_loop()
twa = ThreadWrapper_async(asyncio.Semaphore(limit), loop=loop)
for i in range(times):
    job = a2(i**2, c=i**3)
    twa.add(job=job)
twa.wait()
e = time.time()-start
print(times, e, e/times)
