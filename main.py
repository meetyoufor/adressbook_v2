import os

from file_handler.ab_file_handler import JsonFileHandler
from addressbook.ab_addressbook import AddressBook
from validator.ab_validator import Validator
from contact.ab_contact import Contact


class UserInterface:

    def __init__(self, filename: str):
        self.addressbook = AddressBook()
        self.filename = filename

    def main(self) -> None:
        while True:
            if os.path.isfile(self.filename):
                self.select_mode()
                break
            else:
                print('Неверный путь, повторите ввод')

    def select_mode(self) -> list | None:
        while True:
            mode = input('Выберите режим:\n'
                        'Посмотреть список контактов (r)\n'
                        'Внести новый контакт (w)\n'
                        'Завершить программу (q)\n')
            items = {
                'r': JsonFileHandler.read_file,
                'w': self.create_new_contact,
                'q': False
            }
            return items[mode]()

    def create_new_contact(self) -> None:
        while True:
            email = Validator.format_email(email=input('Введите электронную почту:\n'))
            first_name = Validator.format_name(name=input('Введите имя:\n'))
            last_name = Validator.format_name(name=input('Введите фамилию:\n'))
            address = input('Введите адрес:\n')
            break

        new_contact = Contact(email=email, first_name=first_name, last_name=last_name, address=address)
        self.add_new_contact(new_contact.to_dict())
        print(new_contact)

    def add_new_contact(self, contact) -> None:
        pass


if __name__ == '__main__':
    start = UserInterface(filename='data_base/database.json')
    start.main()
