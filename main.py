import os

from file_handler.ab_file_handler import JsonFileHandler
from adressbook.ab_addressbook import Addressbook
from validator.ab_validator import Validator
from contact.ab_contact import Contact


class UserInterface:

    def __init__(self, *, filename: str):
        self.addressbook = Addressbook()
        self.filename = filename

    def main(self) -> None:
        while True:
            if os.path.isfile(self.filename):
                self.select_mode()
            else:
                print('Неверный путь, повторите ввод')

    def select_mode(self) -> list | None:
        while True:
            mod = input('Выберите режим:\n'
                        'Посмотреть список контактов (r)\n'
                        'Внести новый контакт (w)\n')
            if mod == 'r':
                result = JsonFileHandler.read_file(self.filename)
                print(result)
                return JsonFileHandler.read_file(self.filename)
            if mod == 'w':
                self.create_new_contact()

    def create_new_contact(self) -> None:
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
        self.add_new_contact(contact_instance)

    def add_new_contact(self, contact) -> None:
        Addressbook.load_contacts(self.addressbook, self.filename)
        contacts = Addressbook.get_contacts(self.filename)
        updated_contacts = contacts + contact
        JsonFileHandler.write_file(self.filename, updated_contacts)


if __name__ == '__main__':
    start = UserInterface(filename='data_base/database.json')
    start.main()
