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
    credentials_path = os.path.join(os.path.expanduser('~'), 'path', 'to', '/usr/local/TOOLS/meeting_notification/key/meeting-notification-317702-d40ac5400d60.json')

    # json から Credentials 情報を取得
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, api_scope)

    # 認可されたクライアントを得る
    gspread_client = gspread.authorize(credentials)

    # スプレッドシートの名前を指定する（日本語も使えます）
    spread_sheet_name = "全体昼礼自動通知くん行動予定表参照用"

    # 一つ目のシートを開く
    sheet = gspread_client.open(spread_sheet_name).sheet1

    dt_now = datetime.datetime.now()

    nowdata = dt_now.strftime('%Y/%m/%d')

    #nowdata = "1月1日"
    
    try:
        cell = sheet.find(nowdata)
    except:
        print('error todaymember not found')
        #error_post_chatwork.error_post_chatwork()
        exit()
    todaymember = sheet.cell(cell.row, cell.col+1).value
    return todaymember
