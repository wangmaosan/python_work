# test新建pro账户用户，密码123456
#   输入账户名，enter运行
#   多个账户以", "间隔，例：wang, wang2, ww

import pymysql.cursors
import sys

user = sys.stdin.readline().strip()
user_list = user.split(', ')
DB_HOST = "rm-bp109k6336u50351fmo.mysql.rds.aliyuncs.com"
DB_PORT = 3306
DB_USER = "fusion_deploy"
DB_PASSWORD = "D5techsdb%"
DB_NAME = "test-fusion"

try:
    connect = pymysql.connect(
        host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=DB_PORT,
        charset='utf8'
    )
    # connect = PooledDB(MySQLdb, 30, host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=DB_PORT,
    #                 use_unicode=False, charset='utf8', cursorclass=DictCursor)
    cursor = connect.cursor()
    for user_name in user_list:
        sql = "insert into auth_user(`password`, `username`, `is_active`, `company_id`,`account_type`) " \
              "VALUES('96e79218965eb72c92a549dd5a330112', '%s', 1, 200, 3)" % user_name
        cursor.execute(sql)
        connect.commit()
        print("新建账户: " + user_name)
except OSError as err:
    print(f"OS error: {err}")
