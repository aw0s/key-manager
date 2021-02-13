#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sys import exit

import pyperclip

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
            operations = db_operations.DbOperations(db_name=DB_NAME)
            operations.connection_init()

            while (command := input(">>> ")) != 'exit':
                if command == 'add-service':
                    service_name = input("Type service name: ")

                    services_names_tuple = operations.get_services_tuple()
                    if service_name not in services_names_tuple:
                        service_mail = input("Type mail or nick: ")
                        service_password = input("Type service password: ")

                        operations.add_service(
                            name=service_name,
                            nick_mail=service_mail,
                            password=service_password,
                        )

                        print("Service has been added successfully.")
                    else:
                        print("Service with this name already exists.")
                elif command == 'remove-service':
                    service_name = input("Type service name: ")

                    operations.remove_service(service_name)

                    print("Service has been removed successfully.")
                elif command == 'copy-nick-or-mail':
                    service_name = input("Service name: ")

                    pyperclip.copy(operations.get_nick_mail(service_name))
                elif command == 'copy-password':
                    service_name = input("Service name: ")

                    pyperclip.copy(operations.get_service_password(service_name))
                elif command == 'print-nick-or-mail':
                    service_name = input("Service name: ")

                    print(operations.get_nick_mail(service_name))
                elif command == 'print-password':
                    service_name = input("Service name: ")

                    print(operations.get_service_password(service_name))
                elif command == 'change-password':
                    new_password = input("Type new password: ")

                    operations.change_password(new_password=new_password)
                else:
                    print("Unrecognized command.")
            break
        else:
            print("Incorrect password. Try again.")


if __name__ == '__main__':
    main()
