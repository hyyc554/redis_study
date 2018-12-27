#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 3-14.py
@version   : 1.0
@Time      : 2018/12/27 22:58
Description about this file: 

"""
from utils.redis_pool import conn
import time
from threading import Thread
def trans():
    pipeline = conn.pipeline()
    pipeline.incr('trans:')
    time.sleep(.1)
    pipeline.incr('trans:',-1)
    print(pipeline.execute())
if 1:
    for i in range(3):
        Thread(target=trans).start()
    time.sleep(.5)


