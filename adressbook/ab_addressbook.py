class Addressbook:
    __ADDRESSBOOK_LIMIT: int = 200

    def __init__(self):
        self.__contacts = []

    def __add__(self, other: dict[str, dict]):
        self.__contacts.append(other)
        return self

    def __sub__(self, other: dict[str, dict]):
        self.__contacts.remove(other)
        return self

    def __getitem__(self, item: str): pass

    def __setitem__(self, key, value): pass
