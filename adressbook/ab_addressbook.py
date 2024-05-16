from contact.ab_contact import Contact
from file_handler.ab_file_handler import JsonFileHandler


class Addressbook:
    __ADDRESSBOOK_LIMIT: int = 200

    def __init__(self):
        self.__contacts = []

    def load_contacts(self, filename: str):
        self.__contacts = JsonFileHandler.read_file(filename)

    def get_contacts(self):
        return self.__contacts

    def __add__(self, other: dict, contacts: list):
        if not isinstance(other, dict):
            raise Exception('Нельзя добавить данный объект в addressbook')

        first_letter = other['full_name'][0]
        for item in contacts:
            if first_letter in item.keys():
                item[first_letter].append(contacts)
                break
        else:
            new_letter = {first_letter: [other]}
            contacts.append(new_letter)

        return self

    def __sub__(self, other: dict[str, dict]):
        self.__contacts.remove(other)
        return self

    def __getitem__(self, item: str):
        pass

    def __setitem__(self, key, value):
        pass
