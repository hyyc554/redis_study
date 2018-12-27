#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 3-13transaction.py
@version   : 1.0
@Time      : 2018/12/27 22:20
Description about this file: 

"""

from utils.redis_pool import conn
import time
from threading import Thread


def notrans():
    print(conn.incr('notrans:'))
    time.sleep(.1)
    conn.incr('notrans:', -1)


if 1:
    for i in range(3):
        Thread(target=notrans).start()
    time.sleep(.5)

# msg = conn.hgetall('mydata')
#
#
# print(msg)
