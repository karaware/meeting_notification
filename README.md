# 概要
全体昼礼の担当者に対して chatwork で通知します。 

# 環境
Python3 

# パッケージ
pychatwork 
gspread 
ServiceAccountCredentials 
os 
datetime 
sqlite3 

# 利用準備
post_chatwork.py で以下を設定します。  
ch.ChatworkClient : chatwork の API トークン
room_id : 通知する対象のチャットルーム ID


# 利用方法
main.pyを実行します。 




