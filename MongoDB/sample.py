# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import datetime

import pymongo


def create_db(db_name="new_db"):
    # DB is not created until it gets content
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[db_name]

    return db


def create_collection(db, collection='customer'):
    # collection is not created until it gets content
    if collection_exist(db=db, collection=collection):
        return db[collection]
    return db[collection]


def collection_exist(db, collection='customer'):
    if collection in db.list_collection_names():
        return True
    return False


def db_exist(db_name="pythonSpider"):
    client = pymongo.MongoClient()
    for db in client.list_database_names():
        print(db)

    if db_name in client.list_database_names():
        print(f"--- {db_name} --- exists ---")


def sample():
    client = pymongo.MongoClient()
    # client = pymongo.MongoClient('localhost', 27017)
    # client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.pythonSpider
    # db = client['pythonSpider']
    col = db['book']

    book = {
        "author": "Mike",
        "text": "my first book",
        "tag": ["web crawler", "python", "Network"],
        "date": datetime.datetime.utcnow()
    }
    book_id = col.insert_one(book)
    print(book_id.inserted_id)

    books = [
        {
            "author": "John",
            "text": "my second book",
            "tags": ["quant", 'finance'],
            "date": datetime.datetime.utcnow()
        },
        {
            "author": "gmo",
            "text": "my book",
            "tags": ["c++", "python"],
            "date": datetime.datetime.utcnow()
        },
    ]

    books_id = col.insert_many(books)
    print(books_id.inserted_ids)

    print(col.find_one())
    for x in col.find():
        print(x)


if __name__ == "__main__":
    sample()


