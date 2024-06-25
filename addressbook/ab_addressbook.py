import os
from datetime import datetime
from addressbook_config import record_limit
from addressbook_config import data_base
from contact.ab_contact import Contact
from validator.ab_validator import Validator
from file_handler.ab_file_handler import JsonFileHandler


class AddressBook:
    __ADDRESSBOOK_LIMIT: int = record_limit
    __ADDRESSBOOK_DB: str = data_base

    @staticmethod
    def add_contact(
            contact: Contact,
            filename=__ADDRESSBOOK_DB
    ) -> None:
        contacts = AddressBook.get_contacts()
        contacts.append(contact.__dict__)
        AddressBook.sort_by_alphabet(contacts)
        JsonFileHandler.write_file(filename=filename, data=contacts)

    @staticmethod
    def delete_contact(
            unique_id: int,
            filename=__ADDRESSBOOK_DB
    ) -> None:
        contacts = AddressBook.get_contacts()
        contact = AddressBook.get_contact_by_id(unique_id)
        contacts.remove(contact)
        AddressBook.sort_by_alphabet(contacts)
        JsonFileHandler.write_file(filename=filename, data=contacts)

    @staticmethod
    def update_contact(
            unique_id: int,
            filename=__ADDRESSBOOK_DB,
            email=None, address=None, first_name=None, last_name=None
    ) -> None:
        contacts = AddressBook.get_contacts()
        contact = AddressBook.get_contact_by_id(unique_id)
        contact_index = contacts.index(contact)

        if email:
            email = Validator.format_email(email)
        if first_name:
            first_name = Validator.format_name(first_name)
        if last_name:
            last_name = Validator.format_name(last_name)

        updates = {
            'email': email,
            'address': address,
            'first_name': first_name,
            'last_name': last_name
        }

        for key, value in updates.items():
            if value:
                contact[key] = value

        if first_name or last_name:
            contact['full_name'] = last_name + ' ' + first_name

        contacts[contact_index] = contact
        AddressBook.sort_by_alphabet(contacts)
        JsonFileHandler.write_file(filename=filename, data=contacts)

    @staticmethod
    def get_contacts(filename=__ADDRESSBOOK_DB) -> list:
        return JsonFileHandler.read_file(filename)

    @staticmethod
    def get_contact_by_id(unique_id: int) -> dict:
        contacts = AddressBook.get_contacts()
        for contact in contacts:
            if contact['id_contact'] == unique_id:
                return contact['id_contact']

    @staticmethod
    def get_current_id() -> int:
        contacts = AddressBook.get_contacts()
        for item in contacts:
            current_id = item.get('current_id_counter')
            if current_id:
                return current_id
            if not current_id:
                continue

    @staticmethod
    def sort_by_alphabet(contacts: list) -> None:
        contacts.sort(key=lambda x: x['last_name'])

    @staticmethod
    def adding_contact_by_binary_search(
            contacts: list,
            contact: Contact
    ) -> None:
        first_contact = 0
        last_contact = len(contacts) - 1

        while first_contact <= last_contact:
            middle = (first_contact + last_contact) // 2

            if len(contact.__dict__['last_name']) < len(contacts[middle]['last_name']):
                last_contact = middle - 1
            if len(contact.__dict__['last_name']) > len(contacts[middle]['last_name']):
                last_contact = middle + 1
            if contact.__dict__['last_name'] < contacts[middle]['last_name']:
                last_contact = middle - 1
            if contact.__dict__['last_name'] > contacts[middle]['last_name']:
                last_contact = middle + 1

            ...

    @staticmethod
    def get_addressbook_db(filename=__ADDRESSBOOK_DB):
        return filename


if __name__ == '__main__':
    def main() -> None:
        while True:
            if os.path.isfile(AddressBook.get_addressbook_db()):
                select_mode()
                break
            else:
                print('Неверный путь, повторите ввод')


    def select_mode() -> list | None:
        items = {
            'r': AddressBook.get_contacts,
            'w': create_new_contact
        }

        while True:
            mode = input('Выберите режим:\n'
                         'Посмотреть список контактов (r)\n'
                         'Внести новый контакт (w)\n'
                         'Завершить программу (q)\n')

            if mode == 'q':
                break

            return items[mode]()


    def create_new_contact() -> None:
        while True:
            email = Validator.format_email(email=input('Введите электронную почту:\n'))
            first_name = Validator.format_name(name=input('Введите имя:\n'))
            last_name = Validator.format_name(name=input('Введите фамилию:\n'))
            region = input('Укажите регион / край / область:\n')
            city = input('Укажите город:\n')
            street = input('Укажите название улицы:\n')
            house_number = input('Укажите номер дома:\n')
            apartment_number = input('Укажите номер квартиры:\n')
            address = Validator.format_address(
                region=region,
                city=city,
                street=street,
                house_number=house_number,
                apartment_number=apartment_number
            )

            new_contact = Contact(
                email=email,
                first_name=first_name,
                last_name=last_name,
                address=address,
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

            add_new_contact(new_contact)
            break


    def add_new_contact(new_contact: Contact) -> None:
        AddressBook.add_contact(new_contact)
