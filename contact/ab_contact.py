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
    #
    # def __getitem__(self, item: str) -> str:
    #     return self.to_dict()[item]
    #
    # def into_dict(self) -> dict[str, str]:
    #     return {
    #         'id_contact': self.id_contact,
    #         'first_name': self.first_name,
    #         'last_name': self.last_name,
    #         'full_name': self.full_name,
    #         'email': self.email,
    #         'address': self.address,
    #         'created_at': self.created_at
    #     }

    # def change_contact(self, contact: dict, attr: str, new_attr: str) -> None:
    #     contact[attr] = new_attr


'''
In [1]: hi = 'привет'

In [2]: hi.encode('utf-8')
Out[2]: b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
Функция create_unique_id:

Объединяет атрибуты (имя, фамилия, адрес) в одну строку, используя двоеточие (":") в качестве разделителя.
Преобразует строку в байты.
Кодирует байты в строку Base64, используя метод urlsafe_b64encode для создания URL-безопасного уникального идентификатора.
Функция decode_unique_id:

Декодирует строку Base64 обратно в байты.
Преобразует байты в строку.
Разделяет строку на исходные атрибуты, используя двоеточие (":") в качестве разделителя.
Возвращает словарь с исходными атрибутами.
Этот подход позволяет создать уникальный идентификатор на основе атрибутов и декодировать его обратно в исходные данные. Он также легко реализуем и не требует сложных библиотек или алгоритмов.'''
