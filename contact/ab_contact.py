"""
словарь отсортирован в алфавитном порядке
бинарный поиск
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Contact(ABC):

    def __init__(self, **kwargs) -> None:
        self.id_contact = id_contact
        self.email = kwargs['email']
        self.address = kwargs['address']
        self.created_at = datetime.now()

    @abstractmethod
    def create_contact(self) -> dict:
        new_contact: dict = {
            'id_contact': self.id_contact,
            'email': self.email,
            'address': self.address,
            'created_at': self.created_at
        }
        return new_contact

    @abstractmethod
    def change_contact(self, contact: dict, attr: str, new_attr: str) -> None:
        contact[attr] = new_attr

    @abstractmethod
    def delete_contact(self, database: list, contact: dict) -> None:
        database.remove(contact)

    def __str__(self): pass


class PersonContactMixin:

    def __init__(self, **kwargs) -> None:
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.full_name = self.last_name + ' ' + self.first_name

    def create_contact(self) -> dict:
        new_contact: dict = {
            'first_name': self.first_name,
            'second_name': self.last_name,
            'full_name': self.full_name
        }
        return new_contact

    def change_contact(self): pass

    def delete_contact(self): pass

    def __str__(self): pass


class PersonContact(Contact, PersonContactMixin):

    def __init__(self) -> None:
        super().__init__()
        PersonContactMixin.__init__(self)

    def create_contact(self) -> dict:
        new_contact = super().create_contact() | PersonContactMixin.create_contact(self)
        return new_contact

    def change_contact(self) -> dict: pass

    def delete_contact(self) -> dict: pass

    def __str__(self): pass
