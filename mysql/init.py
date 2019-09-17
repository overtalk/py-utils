# -*- coding: utf-8, a = ‘中文’  -*-
import pymysql




class Config:
    host = ''
    port = 0
    user = ''
    password = ''
    db = ''
    charset = ''

    def __init__(self, user, password, db, host='127.0.0.1', port=3306, charset='utf8mb4'):
        self.charset = charset
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db


class MySQL:
    config = Config
    conn = pymysql.Connection

    def __init__(self, c):
        self.config = c
        self.conn = pymysql.connect(host=c.host,
                                    port=c.port,
                                    user=c.user,
                                    passwd=c.password,
                                    db=c.db,
                                    charset=c.charset)

    def close(self):
        self.conn.close()

    def version(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("Database version : %s " % data)

    def query(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM algorithm;")
        # fetchall：获取所有的数据，默认以元祖的方式返回，如果你指定了cursorclass = pymysql.cursors.DictCursor，则以dict的方式返回
        result = cursor.fetchall()
        for row in result:
            print(row[1])
        cursor.close()

    def insert(self):
        cursor = self.conn.cursor()
        try:
            # 执行一条insert语句，返回受影响的行数
            # cursor.execute("INSERT INTO para5(name,age) VALUES(%s,%s);",('次牛','12'))
            # 执行多次insert并返回受影响的行数
            cursor.executemany("INSERT INTO algorithm(detail) VALUES(%s);",
                               [('3号算法'), ('4号算法'), ('5号算法')])
            # 提交执行
            self.conn.commit()
        except Exception as e:
            # 如果执行sql语句出现问题，则执行回滚操作
            self.conn.rollback()
            print(e)
        finally:
            # 不论try中的代码是否抛出异常，这里都会执行
            # 关闭游标和数据库连接
            cursor.close()

    def delete(self):
        cursor = self.conn.cursor()
        try:
            # 执行一条insert语句，返回受影响的行数
            # cursor.execute("INSERT INTO para5(name,age) VALUES(%s,%s);",('次牛','12'))
            # 执行多次insert并返回受影响的行数
            cursor.executemany("DELETE FROM algorithm WHERE detail in (%s, %s, %s);",
                               [('3号算法', '4号算法', '5号算法')])
            # 提交执行
            self.conn.commit()
        except Exception as e:
            # 如果执行sql语句出现问题，则执行回滚操作
            self.conn.rollback()
            print(e)
        finally:
            # 不论try中的代码是否抛出异常，这里都会执行
            # 关闭游标和数据库连接
            cursor.close()


config = Config(user='root', password='12345678', db='gp_oj')
mysql = MySQL(c=config)
mysql.version()
mysql.insert()
mysql.query()
mysql.delete()
mysql.query()
mysql.close()


