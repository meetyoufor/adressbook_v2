import os

from file_handler.ab_file_handler import JsonFileHandler
from adressbook.ab_addressbook import Addressbook
from validator.ab_validator import Validator
from contact.ab_contact import Contact


class UserInterface:

    def __init__(self):
        self.addressbook = Addressbook()

    def choose_file(self) -> str | None:
        while True:
            file_path = input('Пожалуйста, ввидите путь к файлу:\n')
            if os.path.isfile(file_path):
                return file_path
            else:
                print('Неверный путь, повторите ввод')

    def select_mode(self) -> list | None:
        file_path = self.choose_file()
        while True:
            mod = input('Выберите режим:\n'
                        'Посмотреть список контактов (r)\n'
                        'Внести новый контакт (w)\n')
            if mod == 'r':
                result = JsonFileHandler.read_file(file_path)
                print(result)
                return JsonFileHandler.read_file(file_path)
            if mod == 'w':
                self.create_new_contact()

    def create_new_contact(self) -> Contact:
        new_contact: dict[str, str] = {}

        while True:
            email = input('Введите электронную почту:\n')
            new_contact['email'] = Validator.format_email(email=email)
            last_name = input('Введите фамилию:\n')
            new_contact['last_name'] = Validator.format_name(name=last_name)
            first_name = input('Введите имя:\n')
            new_contact['first_name'] = Validator.format_name(name=first_name)
            address = input('Введите адрес:\n')
            new_contact['address'] = address
            print(new_contact)
            break

        contact_instance = Contact(new_contact)
        return contact_instance

    def add_new_contact(self, contact):



if __name__ == '__main__':
    start_go = UserInterface()
    start_go.select_mode()

# 'data_base/database.json'