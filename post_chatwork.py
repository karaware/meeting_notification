#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pychatwork as ch

def post_chatwork(userlist):
    client = ch.ChatworkClient("5d885ec366178e84854d76e4a19f5784")

    # get message from my room
    res = client.get_messages(room_id="173813291", force=True)

    messages = "[To:" + str(userlist[1]) + "]" + userlist[3] + "さん\n \
本日昼礼当番です！\n \
お題は以下からご確認ください。\n \
https://docs.google.com/spreadsheets/d/1sW_pF0TOUp2fh9BjWSefdczWj59INQ8oCcOg6u9FLAM/edit#gid=1627000145\n \
よろしくお願いします(bow)"

    # post message to my room
    client.post_messages(room_id="173813291", message=messages)
