#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pychatwork as ch

def post_chatwork(userlist):
    client = ch.ChatworkClient("####")

    # get message from my room
    #res = client.get_messages(room_id="####", force=True)
    #BYD-MEMBER
    res = client.get_messages(room_id="####", force=True)

    messages = "[To:" + str(userlist[1]) + "]" + userlist[3] + "さん\n \
本日昼礼当番です！\n \
よろしくお願いします(bow)"

    client.post_messages(room_id="####", message=messages)
    #client.post_messages(room_id="####", message=messages)
