#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
# import sqlite3

import db_operations
from settings import *


def main() -> None:
    if not os.path.exists(DB_NAME):
        db_operations.init_db()

    while True:
        password_input = input("Type your keypass password: ")
        password_correctness = db_operations.password_correctness(password_input)

        if password_correctness:
            while True:
                mode_input = input("Choose your db operation mode: ")

                if mode_input == 'read':
                    mode = 'read'
                elif mode_input == 'write':
                    mode = 'write'
                else:
                    print("Incorrect mode.")

            operation = db_operations.DbOperations(mode=mode)
        else:
            print("Incorrect password. Try again.")


if __name__ == '__main__':
    main()
