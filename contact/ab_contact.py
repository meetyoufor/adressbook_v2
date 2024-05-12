"""
словарь отсортирован в алфавитном порядке
бинарный поиск
"""

from datetime import datetime


class Contact:

    def __init__(self, **kwargs) -> None:
        self.id_contact = id_contact
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.full_name = self.last_name + ' ' + self.first_name
        self.email = kwargs['email']
        self.address = kwargs['address']
        self.created_at = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def create_contact(self) -> dict:
        new_contact: dict = {
            'id_contact': self.id_contact,
            'first_name': self.first_name,
            'second_name': self.last_name,
            'full_name': self.full_name,
            'email': self.email,
            'address': self.address,
            'created_at': self.created_at,
        }
        return new_contact

    def change_contact(self, contact: dict, attr: str, new_attr: str) -> None:
        contact[attr] = new_attr

    def delete_contact(self, database: list, contact: dict) -> None:
        database.remove(contact)

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        return self.email == other.email

    def __str__(self):
        return f'{self.full_name}, address: {self.address}\n'

    def __repr__(self):
        return f' id:{self.id_contact}, created at: {self.created_at}\n'
