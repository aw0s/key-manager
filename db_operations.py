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
            name text,
            login_mail text,
            password text
        )""")

        conn.commit()


def password_correctness(db_name: str, password: str) -> bool:
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM login""")
        password_db = cursor.fetchone()[0]

        return password == password_db


"""
SQL commands:
add service:
INSERT INTO keymanager (
service_name, service_nick_mail, service_password
) values (
"uno", "due", "tre"
)

delete service: DELETE FROM keymanager WHERE service_name="uno"
"""


class DbOperations:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

        self.conn = None
        self.cursor = None

    def connection_open(self) -> None:
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor = self.conn.cursor()

    def add_service(self, name: str, nick_mail: str, password: str) -> None:
        self.cursor.execute(f"""INSERT INTO keypass (
            
        )""")
