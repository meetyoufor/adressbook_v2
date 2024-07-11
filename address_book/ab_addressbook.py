import os

from constants import *
from contact.ab_contact import Contact
from datetime import datetime
from dotenv import load_dotenv
from file_handler.ab_file_handler import JsonFileHandler
from validator.ab_validator import Validator


class AddressBook:
    __DB_URL: str = os.getenv('DB_URL')
    __RECORDS_LIMIT: int = int(os.getenv('RECORDS_LIMIT'))

    @staticmethod
    def add_contact(contact: Contact) -> None:
        if AddressBook.is_address_book_records_limit_reached():
            print('Невозможно добавить контакт, лимит записей исчерпан')
            return

        contacts = AddressBook.get_contacts()
        if AddressBook.get_address_book_length() < 1:
            contacts.append(contact)

        try:
            AddressBook.adding_contact_by_binary_search(contacts, contact)
        except Exception as e:
            print(f'Не удалось добавить контакт. Ошибка: {e}')

        JsonFileHandler.write_file(filename=AddressBook.__DB_URL, data=contacts)

    @staticmethod
    def adding_contact_by_binary_search(
            contacts: list,
            contact: Contact
    ) -> None:
        temp_contacts = contacts[1:]  # первый объект в спике - инкремент
        temp_contact = contact.__dict__['last_name']
        left_contact = 0
        right_contact = len(temp_contacts)

        while temp_contacts[left_contact]['last_name'] < temp_contacts[right_contact]['last_name']:
            middle_contact = (left_contact + right_contact) // 2
            if temp_contact < temp_contacts[middle_contact]['last_name']:
                left_contact = middle_contact + 1
            if temp_contact > temp_contacts[middle_contact]['last_name']:
                right_contact = middle_contact

        position = left_contact + 1  # первый объект в спике - инкремент
        contacts.insert(position, contact)
        JsonFileHandler.write_file(AddressBook.__DB_URL, contacts)

    @staticmethod
    def delete_contact(unique_id: int) -> None:
        contacts = AddressBook.get_contacts()
        contact = AddressBook.get_contact_by_id(unique_id)

        try:
            contacts.remove(contact)
        except Exception as e:
            print(f'Не удалось удалить контакт. Ошибка: {e}')

        JsonFileHandler.write_file(filename=AddressBook.__DB_URL, data=contacts)

    @staticmethod
    def update_contact(unique_id: int, **kwargs) -> None:
        contacts = AddressBook.get_contacts()
        contact = AddressBook.get_contact_by_id(unique_id)
        contact_index = contacts.index(contact)

        for key, value in kwargs.items():
            contact[key] = value

        contact['full_name'] = contact['last_name'] + ' ' + contact['first_name']

        contacts[contact_index] = contact
        AddressBook.sort_by_alphabet(contacts)
        JsonFileHandler.write_file(filename=AddressBook.__DB_URL, data=contacts)

    @staticmethod
    def get_db_url():
        return AddressBook.__DB_URL

    @staticmethod
    def get_contacts() -> list:
        return JsonFileHandler.read_file(AddressBook.__DB_URL)

    @staticmethod
    def get_address_book_length() -> int:
        contacts = JsonFileHandler.read_file(filename=AddressBook.__DB_URL)
        return len(contacts) - 1

    @staticmethod
    def get_current_increment() -> int:
        contacts = AddressBook.get_contacts()
        for item in contacts:
            current_id = item.get('current_id_counter')
            if current_id:
                return current_id
            if not current_id:
                continue

    @staticmethod
    def get_contact_by_id(unique_id: int) -> dict:
        contacts = AddressBook.get_contacts()
        for contact in contacts:
            if contact['id_contact'] == unique_id:
                return contact['id_contact']
        print('Контакт с таким id не найден')

    @staticmethod
    def sort_by_alphabet(contacts: list) -> None:
        contacts.sort(key=lambda x: x['last_name'])

    @staticmethod
    def is_address_book_records_limit_reached() -> bool:
        return AddressBook.__RECORDS_LIMIT <= AddressBook.get_address_book_length()

    @staticmethod
    def configure():
        load_dotenv()


def main() -> None:
    AddressBook.configure()
    db_url = AddressBook.get_db_url()

    if not os.path.isfile(db_url):
        print('Отсутствует подключение к списку контактов')
        return

    flags = {
        'r': AddressBook.get_contacts(),
        'w': create_new_contact(),
        'u': AddressBook.update_contact(int(input('Введите id контакта'))),
        'd': AddressBook.delete_contact(int(input('Введите id контакта')))
    }

    mode = input(MAIN_MENU_TEXT)
    if mode == 'q':
        return

    return flags[mode]


def create_new_contact() -> None:
    new_contact_data = {
        'email': Validator.format_email(input('Введите электронную почту:\n')),
        'last_name': Validator.format_name(input('Введите фамилию:\n')),
        'first_name': Validator.format_name(input('Введите имя:\n')),
        'address': prepare_address_data()
    }

    new_contact = Contact(
        id_contact=AddressBook.get_current_increment() + 1,
        email=new_contact_data['email'],
        first_name=new_contact_data['first_name'],
        last_name=new_contact_data['last_name'],
        address=new_contact_data['address'],
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    add_new_contact(new_contact)


def prepare_address_data() -> str:
    address_data = {
        'city': input('Укажите город:\n'),
        'street': input('Укажите название улицы:\n'),
        'house_number': input('Укажите номер дома:\n'),
        'apartment_number': input('Укажите номер квартиры:\n')
    }

    address = Validator.format_address(
        city=address_data['city'],
        street=address_data['street'],
        house_number=address_data['house_number'],
        apartment_number=address_data['apartment_number']
    )

    return address


def add_new_contact(new_contact: Contact) -> None:
    AddressBook.add_contact(new_contact)


def prepare_data_for_update_contact():
    updated_contact = {}

    contact_id = int(input('Укажите id пользователя\n'))
    mode = input(UPDATE_CONTACT_TEXT)

    if 'f' in mode:
        updated_contact['first_name'] = Validator.format_name(input('Введите имя:\n'))
    if 'l' in mode:
        updated_contact['last_name'] = Validator.format_name(input('Введите фамилию:\n'))
    if 'e' in mode:
        updated_contact['email'] = Validator.format_email(input('Введите электронную почту:\n'))
    if 'a' in mode:
        updated_contact['address'] = prepare_address_data()

    AddressBook.update_contact(contact_id, **updated_contact)


if __name__ == '__main__':
    main()

"""
app = FastApi()
app.base_url = 'https://www.i_m_programmer.ru'

import redis

@redis.cache(time='1d')
@app.get('/get_users')
def get_contact():
    return AddressBook.get_contact()
"""
