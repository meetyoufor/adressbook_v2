import abc


class Contact(abc.ABC):

    def __init__(self, **kwargs) -> None:
        pass

    @abc.abstractmethod
    def create_contact(self) -> dict:
        ...

    @abc.abstractmethod
    def change_contact(self) -> dict:
        ...


class PersonContactMixin:
    ...


class PersonContact(Contact):

    def __init__(self, **kwargs):
        super().__init__()

    def create_contact(self) -> dict:
        ...

    def change_contact(self) -> dict:
        ...
