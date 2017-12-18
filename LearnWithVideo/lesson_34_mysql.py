import pymysql


def create_table():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='py3learn')

    sql = '''create table if not exists dev(
    id int NOT NULL AUTO_INCREMENT,
    name text,
    job text,
    PRIMARY KEY (`id`))'''
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print('create table dev successfully')
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()


def insert_table():
    insert_db = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                db='py3learn',
                                charset="utf8")
    sql = 'insert into dev (name,job) values (%s,%s)'
    cursor = insert_db.cursor()
    try:
        value = ('wx', 'pyton')
        cursor.execute(sql, value)
        insert_db.commit()
        print("insert successfully")
        return True
    except BaseException as e:
        insert_db.rollback()
        print(e)
    finally:
        cursor.close()
        insert_db.close()


def query_table():
    querty_db = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                db='py3learn')
    sql = 'select * from dev'
    cursor = querty_db.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        print('查询一条数据为： id =%d, name =%s, job =%s' % (result[0]), result[1], result[2])
        cursor.scroll(0, mode='absolute')
        results = cursor.fetchall()
        data = {}
        lists = []
        for row in results:
            data = data.copy()
            print('查询多条数据： id =%d,name =%s,job=%s' % (row[0], row[1], row[2]))
            data['id'] = row[0]
            data['name'] = row[1]
            data['job'] = row[2]
            lists.append(data)
        print(lists)
        return lists
    except BaseException as a:
        querty_db.rollback()
        print(a)
    finally:
        cursor.close()
        querty_db.close()


if __name__ == '__main__':
    # create_table()
    # insert_table()
    query_table()
