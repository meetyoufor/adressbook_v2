import os

from file_handler.ab_file_handler import JsonFileHandler
from adressbook.ab_addressbook import Addressbook
from validator.ab_validator import Validator


class UserInterface:


    class UserInterface:

        def __init__(self):
            self.addressbook = Addressbook()

        def choose_file(self) -> str | None:
            while True:
                file_path = input('Пожалуйста, ввидите путь к файлу')
                if os.path.isfile(file_path):
                    return file_path
                else:
                    print('Неверный путь, повторите ввод')

        def select_mode(self, file_path: str) -> list | None:
            while True:
                mod = input('Выберите режим:'
                            '\nПосмотреть список контактов (r)'
                            '\nВнести новый контакт (w)')

                if mod == 'r':
                    return JsonFileHandler.read_file(file_path)
                if mod == 'w':
                    JsonFileHandler.write_file()

        def create_new_contact(self) -> dict:
            new_contact = {}

            while True:
                email = input('Введите электронную почту')
                new_contact['email'] = Validator.format_email(email=email)
                last_name = input('Введите фамилию')
                new_contact['first_name'] = Validator.format_name(name=last_name)
                first_name = input('Введите имя')
                new_contact['last_name'] = Validator.format_name(name=first_name)
                address = input('Введите адрес')
                new_contact['address'] = address
                break

            return new_contact
