#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

from settings import *


def init_db() -> None:
    with sqlite3.connect('passdb.db') as conn:
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE login (
            password text
        )""")
        cursor.execute("""CREATE TABLE keypass (
            destignation text,
            login_mail text,
            password text
        )""")

        conn.commit()


def password_correctness(password: str) -> bool:
    with sqlite3.connect('passdb.db') as conn:
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM login""")
        password_db = cursor.fetchone()[0]

        return password == password_db


class DbOperations:
    def __init__(self, mode: str) -> None:
        self.mode = mode

        self.conn = None
        self.cursor = None

    def connection_open(self) -> None:
        with sqlite3.connect(DB_NAME) as self.conn:
            self.cursor = self.conn.cursor()


