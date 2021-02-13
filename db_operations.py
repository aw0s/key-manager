#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


def init_db() -> None:
    with sqlite3.connect('passdb.db') as conn:
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE login (
            password text
        )""")
        cursor.execute("""CREATE TABLE keymanager (
            name text,
            nick_mail text,
            password text
        )""")

        conn.commit()


def password_correctness(db_name: str, password: str) -> bool:
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM login""")
        password_db = cursor.fetchone()[0]

        return password == password_db


def get_password(db_name: str) -> str:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM login""")
    password = cursor.fetchone[0]

    return password


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
        self.read_cursor = None
        self.write_cursor = None

        self.keymanager_table_data = []
        self.login_table_data = []

    def connection_init(self) -> None:
        with sqlite3.connect(self.db_name) as self.conn:
            self.read_cursor = self.conn.cursor()
            self.write_cursor = self.conn.cursor()

        self.read_cursor.execute("""SELECT * FROM keymanager""")
        self.keymanager_table_data = self.read_cursor.fetchall()

        self.read_cursor.execute("""SELECT * FROM login""")
        self.login_table_data = self.read_cursor.fetchall()

    def add_service(self, name: str, nick_mail: str, password: str) -> None:
        self.write_cursor.execute(f"""INSERT INTO keymanager (
            name, nick_mail, password
        ) VALUES (
            "{name}", "{nick_mail}", "{password}"
        )""")
        self.conn.commit()

    def remove_service(self, service_name: str) -> None:
        self.write_cursor.execute(f'''DELETE FROM keymanager WHERE name="{service_name}"''')
        self.conn.commit()

    def get_nick_mail(self, service_name: str) -> str:
        service_tuple = tuple(filter(lambda x: x[0] == service_name, self.keymanager_table_data))[0]
        nick_mail = service_tuple[1]

        return nick_mail

    def get_service_password(self, service_name: str) -> str:
        service_tuple = tuple(filter(lambda x: x[0] == service_name, self.keymanager_table_data))[0]
        password = service_tuple[2]

        return password

    def change_password(self, new_password: str) -> None:
        old_password = self.login_table_data[0][0]

        self.write_cursor.execute(f'''DELETE FROM login WHERE password="{old_password}"''')
        self.write_cursor.execute(f"""INSERT INTO login (password) VALUES ("{new_password}")""")
        self.conn.commit()

    def get_services_tuple(self) -> tuple:
        services_tuple = tuple(record[0] for record in self.keymanager_table_data)

        return services_tuple
