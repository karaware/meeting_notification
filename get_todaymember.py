#!/usr/bin/env python
# -*- coding: utf-8 -*-
import error_post_chatwork

def get_todaymember():
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import os
    import datetime

    # 利用する API を指定する
    api_scope = ['https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive']

    # 先ほどダウンロードした json パスを指定する
    credentials_path = os.path.join(os.path.expanduser('~'), 'path', 'to', '/root/meeting_notification/key/meetingorder-test-c1cd18f30f44.json')

    # json から Credentials 情報を取得
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, api_scope)

    # 認可されたクライアントを得る
    gspread_client = gspread.authorize(credentials)

    # スプレッドシートの名前を指定する（日本語も使えます）
    spread_sheet_name = "gsstestsheat"

    # 一つ目のシートを開く
    sheet = gspread_client.open(spread_sheet_name).sheet1

    dt_now = datetime.datetime.now()

    nowdata = dt_now.strftime('%-m月%-d日')

    #nowdata = "1月1日"
    
    try:
        cell = sheet.find(nowdata)
    except:
        print('error')
        error_post_chatwork.error_post_chatwork()
        exit()
    todaymember = sheet.cell(cell.row, cell.col-1).value
    
    return todaymember
