from addressbook_config import record_limit
from addressbook_config import data_base
from datetime import datetime
from contact.ab_contact import Contact
from file_handler.ab_file_handler import JsonFileHandler


class AddressBook:
    __ADDRESSBOOK_LIMIT: int = record_limit
    __ADDRESSBOOK_DB: str = data_base

    @staticmethod
    def add_contact(contact: Contact, filename=__ADDRESSBOOK_DB):
        contacts = JsonFileHandler.read_file(filename)
        contacts.append(contact.__dict__)
        JsonFileHandler.write_file(filename=filename, data=contacts)

    @staticmethod
    def delete_contact():
        pass

    @staticmethod
    def update_contact():
        pass

    @staticmethod
    def get_contacts(filename=__ADDRESSBOOK_DB) -> list:
        return JsonFileHandler.read_file(filename)

    @staticmethod
    def get_contact_by_id(unique_id: str) -> int:
        contacts = AddressBook.get_contacts()
        for contact in contacts:
            return contact[unique_id]

    @staticmethod
    def get_current_id() -> int:
        contacts = AddressBook.get_contacts()
        for item in contacts:
            current_if = item.get('current_id_counter')
            if current_if:
                return current_if
            if not current_if:
                continue

    # def __add__(self, other: Contact):
    #     if not isinstance(other, Contact):
    #         raise Exception('Нельзя добавить данный объект в Addressbook')
    #     if not self.check_unique(other=other):
    #         raise Exception('Контакт уже находится в Addressbook\n')
    #     self.__contacts.append(other)
    #     return self


con1 = {
    "id_contact": 1,
    "first_name": "Алеша",
    "last_name": "Попов",
    "email": "Popov@osas.ru",
    "address": "Москва"
}
new_contact = Contact(
    email=con1['email'],
    id_contact=con1['id_contact'],
    first_name=con1['first_name'],
    last_name=con1['last_name'],
    address=con1['address'],
    created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)
AddressBook.add_contact(new_contact)
