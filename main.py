#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3

import db_operations


def main() -> None:
    if not os.path.exists('passdb.db'):
        db_operations.init_db()


if __name__ == '__main__':
    main()
