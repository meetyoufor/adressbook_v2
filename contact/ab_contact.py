import abc


class Contact(abc.ABC):

    def __init__(self, emile: str, address: str) -> None:
        self.emile = emile
        self.address = address

    @abc.abstractmethod
    def create_contact(self) -> dict:
        ...

    @abc.abstractmethod
    def change_contact(self) -> dict:
        ...


class PersonContact(Contact):
    ...

    def create_contact(self) -> dict:
        ...

    def change_contact(self) -> dict:
        ...
