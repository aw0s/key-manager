#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from sys import exit
# import sqlite3

import db_operations
from settings import *


def main() -> None:
    if not os.path.exists(DB_NAME):
        db_operations.init_db()

    while True:
        password_input = input("Type your keypass password: ")
        if password_input == 'exit':
            exit(0)

        password_correctness = db_operations.password_correctness(
            db_name=DB_NAME,
            password=password_input,
        )

        if password_correctness:
            operation = db_operations.DbOperations(db_name=DB_NAME)
            operation.connection_open()

            while command := input(">>> ") != 'exit':
                if command == 'add-service':
                    service_name = input("Type your service name: ")
                    service_mail = input("Type your mail or nick: ")
                    service_password = input("Type your service password: ")

                    operation.add_service(
                        name=service_name,
                        nick_mail=service_mail,
                        password=service_password,
                    )

                    print("Service has been added successfully.")
                elif command == 'get-password':
                    pass
                else:
                    print("Incorrect command.")
        else:
            print("Incorrect password. Try again.")


if __name__ == '__main__':
    main()
