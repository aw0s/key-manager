#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


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


class DbOperations:
    def __init__(self, mode: str) -> None:
        self.mode = mode
