# coding=utf-8

"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。
"""

import pymysql


def saveGifts(gifts):
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor
    }
    conn = pymysql.Connect(**config)
    conn.autocommit(1)
    cursor = conn.cursor()
    try:
        #    创建数据库
        DB_NAME = 'python'
        result = cursor.execute('CREATE DATABASE IF NOT EXISTS ' + DB_NAME)
        print("创建数据库的结果：" + str(result))
        conn.select_db(DB_NAME)
        # 创建表
        crate_sql = 'CREATE TABLE IF NOT EXISTS py_gifts(id VARCHAR(32) PRIMARY KEY,code VARCHAR(16))'
        result = cursor.execute(crate_sql)
        print('创建表的结果: ' + str(result))
        # 插入数据
        insert_sql = 'INSERT INTO py_gifts(id,code) VALUES(%s,%s)'
        keys = []
        for i in range(len(gifts)):
            import UUIDFactory
            keys.append(UUIDFactory.uuid())
        result = cursor.executemany(insert_sql, zip(keys,gifts))
        print('插入数据库的结果：' + str(result))
    except:
        import traceback
        traceback.print_exc()
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def main():
    import q_0001
    gifts = q_0001.generate(20, 6)
    saveGifts(gifts)


if __name__ == '__main__':
    main()






