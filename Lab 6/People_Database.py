__author__ = 'QiongchengXu'
import sqlite3


DATABASE_NAME = "Product.db"


def main():
    insert_record(1, "body wash")
    retrieve_all_records()


def insert_record(pid, name):
    conn = sqlite3.connect(DATABASE_NAME)
    sql = "insert into products (product_id, product_name) values ({0}, '{1}')".format(pid, name)
    print sql
    conn.execute(sql)
    conn.commit()
    conn.close()


def retrieve_all_records():
    conn = sqlite3.connect(DATABASE_NAME)
    sql = "select * from products"
    rows = conn.execute(sql)

    for row in rows:
        print row[0], row[1]

    conn.commit()
    conn.close()


main()