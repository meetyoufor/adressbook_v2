import re


class Validator:
    __NAME_CHARS_LIMIT: int = 50
    __EMAIL_CHARS_LIMIT: int = 25
    __ADDRESS_CHARS_LIMIT: int = 150

    @staticmethod
    def format_name(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError('Неверный тип данных')
        if len(name) > Validator.__NAME_CHARS_LIMIT:
            raise ValueError(f'Превышено допустимое количество ({Validator.__NAME_CHARS_LIMIT}) символов.')
        if not re.match(r'^[а-яА-ЯёЁ]+$', name):
            raise ValueError('Строка должна содержать только кириллические символы.')

        formatted_name = name.strip().lower().capitalize()
        if name != formatted_name:
            return formatted_name

        return name

    @staticmethod
    def format_email(email: str) -> str:
        if not isinstance(email, str):
            raise TypeError('Неверный тип данных')
        if len(email) > Validator.__EMAIL_CHARS_LIMIT:
            raise ValueError(f'Превышено допустимое количество ({Validator.__EMAIL_CHARS_LIMIT}) символов.')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise TypeError('Ошибка при введении данных')

        formatted_email = email.strip().lower()
        if formatted_email != email:
            return formatted_email

        return email

    @staticmethod
    def format_address(**kwargs) -> str:
        for value in kwargs.values():
            if not isinstance(value, str):
                raise TypeError('Неверный тип данных')
        for value in kwargs.values():
            if not re.match(r'^[А-ЯЁа-яё0-9\s-]+$', value):
                raise ValueError('Строка должна содержать только кириллические символы.')
        for key, value in kwargs.items():
            kwargs[key] = value.capitalize()

        formatted_address = f'г. {kwargs['city']}, ул. {kwargs['street']}, д. {kwargs['house_number']}, кв. {kwargs['apartment_number']}'
        if len(formatted_address) > Validator.__ADDRESS_CHARS_LIMIT:
            raise ValueError(f'Превышено допустимое количество ({Validator.__ADDRESS_CHARS_LIMIT}) символов.')

        return formatted_address
