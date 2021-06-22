#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def get_userdata(todaymember):
    print(todaymember)
    dbname = 'meeting_notification.sqlite3'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    sql = 'SELECT * FROM user where cname = "' + todaymember + '";'
    cur.execute(sql)
    userlist = cur.fetchone()
    return userlist
