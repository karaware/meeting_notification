#!/usr/bin/env python
# -*- coding: utf-8 -*-

import get_todaymember
import get_userdata
import post_chatwork

todaymember = get_todaymember.get_todaymember()
if todaymember:
    userlist = get_userdata.get_userdata(todaymember)
    post_chatwork.post_chatwork(userlist)
