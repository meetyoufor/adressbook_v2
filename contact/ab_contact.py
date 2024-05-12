"""
словарь отсортирован в алфавитном порядке
бинарный поиск
"""

from datetime import datetime
import hashlib


class Contact:

    def __init__(self, contact_info: dict[str, str]) -> None:
        self.id_contact = GeneratorID.email_hash(contact_info['email'])
        self.first_name = contact_info['first_name']
        self.last_name = contact_info['last_name']
        self.full_name = self.last_name + ' ' + self.first_name
        self.email = contact_info['email']
        self.address = contact_info['address']
        self.created_at = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def create_contact(self) -> dict[str, str]:
        new_contact = {
                'id_contact': self.id_contact,
                'first_name': self.first_name,
                'second_name': self.last_name,
                'full_name': self.full_name,
                'email': self.email,
                'address': self.address,
                'created_at': self.created_at
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


class GeneratorID:

    @staticmethod
    def email_hash(email: str) -> str:
        email_bytes = email.encode('UTF-8')
        hashed_email = hashlib.sha256(email_bytes).hexdigest()

        return hashed_email
