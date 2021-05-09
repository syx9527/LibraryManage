import pymysql
import traceback

host = "127.0.0.1"
user = "root"
password = "123456"
database = "yyy"  # 数据库名字


def get_conn():
    """
    链接数据库
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
                           db=database,
                           )
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    """
    关闭链接
    :param conn:
    :param cursor:
    :return:
    """
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def exec_(sql):
    cursor = None
    conn = None
    try:
        conn, cursor = get_conn()
        cursor.execute(sql)
        conn.commit()  # 提交事务 update delete insert操作
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def main():
    sql = "select * from student"  # mysql查询语句
    res = query(sql)
    print(res)
