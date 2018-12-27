#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : redis_pool.py
@version   : 1.0
@Time      : 2018/12/27 22:37
Description about this file: 

"""
import redis

pool = redis.ConnectionPool(host='47.106.237.76', port=6379,password='hyc554')

conn = redis.Redis(connection_pool=pool)


