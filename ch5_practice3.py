import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
                       user='root', passwd='', db='mysql')

cur = conn.cursor()
cur.execute("USE django_tangerine")

cur.execute("SELECT * from auth_user WHERE id<20")
print(cur.fetchone())
cur.close()
conn.close()
