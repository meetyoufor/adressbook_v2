import abc
from datetime import datetime


class AddressbookBack(abc.ABC):
    ...


class Addressbook:
    __ADDRESSBOOK_LIMIT: int = 200
