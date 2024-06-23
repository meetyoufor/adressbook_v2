from addressbook.ab_addressbook import AddressBook
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Contact:
    email: str
    address: str
    created_at: str
    first_name: str
    last_name: str
    id_contact: int = field(init=False)
    updated_at: str = field(init=False)
    full_name: str = field(init=False)

    def __post_init__(self) -> None:
        self.id_contact = AddressBook.get_current_id() + 1
        self.full_name = self.last_name + ' ' + self.first_name
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #
    # def __str__(self):
    #     return (f'id: {self.id_contact}\n'
    #             f'full name: {self.full_name}\n'
    #             f'email: {self.email}\n')
