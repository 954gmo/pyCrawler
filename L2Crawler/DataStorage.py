# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import sqlite3
import settings


class DataOutput(object):
    def __init__(self):
        self.conn = sqlite3.connect('movie.db')
        self.create_table('movies')
        self.data = list()

    def create_table(self, table_name):
        sql = """
            CREATE TABLE IF NOT EXISTS ? (
                id integer primary key,
                MovieId integer,
                MovieTitle varchar(40) NOT NULL,
                RatingFinal REAL NOT NULL DEFAULT 0.0,
                ROtherFinal REAL NOT NULL DEFAULT 0.0,
                RPictureFinal REAL NOT NULL DEFAULT 0.0,
                RDirectorFinal REAL NOT NULL DEFAULT 0.0,
                RStoryFinal REAL NOT NULL DEFAULT 0.0,
                Usercount integer NOT NULL DEFAULT 0,
                AttitudeCount integer NOT NULL DEFAULT 0,
                TotalBoxOffice varchar(20) NOT NULL,
                TodayBoxOffice varchar(20) NOT NULL,
                Rank integer NOT NULL DEFAULT 0,
                ShowDays integer NOT NULL DEFAULT 0,
                isRelease integer NOT NULL
            )
        """
        self.conn.execute(sql, (table_name, ))

    def store_data(self, data):
        if data is None:
            return

        self.data.append(data)

        if len(self.data) > settings.WRITE_PER_ENTRY_CNT:
            self.output_db('movies')

    def output_db(self, table_name):
        for data in self.data:
            self.conn.execute(
                f"""
                    INSERT INTO {table_name}
                    (
                        
                    ) 
                """, data
            )