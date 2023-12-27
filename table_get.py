import MySQLdb
import time

#mysql起動のため10秒待つ
time.sleep(10)

# 接続する 
connection = MySQLdb.connect(
 host = 'db',
 user='root',
 passwd='root',
 db='test_db')

# カーソルを取得する
cursor = connection.cursor()

# SQLを実行する
cursor.execute("""show tables;""")

# 実行結果を取得する
rows = cursor.fetchall()

# 1行ずつ表示する
for row in rows:
 print(row)

cursor.close
connection.close