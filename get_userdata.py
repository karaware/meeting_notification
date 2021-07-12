#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import error_post_chatwork

def get_userdata(todaymember):
    dbname = 'meeting_notification.sqlite3'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    sql = 'SELECT * FROM user where cname = "' + todaymember + '";'
    cur.execute(sql)
    userlist = cur.fetchone()
    if not userlist:
        print('error')
        error_post_chatwork.error_post_chatwork()
        exit()
    return userlist
