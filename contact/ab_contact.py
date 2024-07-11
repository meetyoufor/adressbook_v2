# from address_book.ab_addressbook import AddressBook
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Contact:
    id_contact: int
    email: str
    address: str
    created_at: str
    first_name: str
    last_name: str
    updated_at: str = field(init=False)
    full_name: str = field(init=False)

    def __post_init__(self) -> None:
        # self.id_contact = AddressBook.get_current_increment() + 1
        self.full_name = self.last_name + ' ' + self.first_name
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
