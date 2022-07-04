# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import sqlite3
import os
from pathlib import Path

def sample():

    BASE_DIR = Path(__file__).resolve().parent
    DB_PATH = os.path.join(BASE_DIR, 'test.db')
    conn = sqlite3.connect(DB_PATH)
    # conn = sqlite3.connect(':memory:') # create database in Memory

    # cursor() ,
    # commit() transaction,
    # rollback() transaction,
    # close() connection

    cur = conn.cursor()

    # cur.execute() sql stmt,
    # cur.executemany() sql stmt,
    # cur.close() cursor,
    # cur.fetchone() record,
    # cur.fetchmany() records,
    # cur.fetchall() records,
    # cur.scroll() cursor
    sql_stmt = """
        CREATE TABLE IF NOT EXISTS person (
            id integer primary key,
            name varchar(20),
            age integer
            )
    """
    cur.execute(sql_stmt)

    conn.commit()
    print("table created")

    # not secure, easy to SQL injection
    data = "0, 'sig_gmo', 20"
    query_insertion = f'INSERT INTO person VALUES ({data})'
    cur.execute(query_insertion)

    query_insertion = 'INSERT INTO person VALUES(?, ?, ?)'
    data = (1, 'sig_gmo2', 21)
    cur.execute(query_insertion, data )

    data = [
        (2, 'sig_gmo3', 23),
        (3, 'sig_gmo4', 24),
        (4, 'gmo_sig', 25),
            ]

    cur.executemany(query_insertion, data)

    conn.commit()
    print("data inserted")

    query_selection = """
        SELECT *
        FROM person
    """

    print("select * ")
    cur.execute(query_selection)
    res = cur.fetchall()

    for ent in res:
        print(ent)

    print("fetchone one")
    cur.execute("select * from person")
    res = cur.fetchone()
    print(res)

    update_query = """
        UPDATE person 
        SET name=? 
        WHERE id=?
    """

    cur.execute(update_query, ('new', 0))
    conn.commit()
    print("updated new 0")

    print("select id=0")
    cur.execute("select * from person where id=?", (0,))
    res = cur.fetchone()
    print(res)

    print("delete id=0")
    cur.execute("delete from person where id=?", (0,))
    conn.commit()

    cur.execute("select * from person")
    res = cur.fetchall()
    for ent in res:
        print(ent)


if __name__ == "__main__":
    sample()
