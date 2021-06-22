#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pychatwork as ch

def error_post_chatwork():
    client = ch.ChatworkClient("5d885ec366178e84854d76e4a19f5784")

    # get message from my room
    res = client.get_messages(room_id="173813291", force=True)

    messages = "[To:4094042] meeting_notification でエラーが発生しました。確認してください。"

    # post message to my room
    client.post_messages(room_id="173813291", message=messages)
