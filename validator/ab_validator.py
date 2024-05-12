import re


class Validator:

    @staticmethod
    def format_name(*, name: str, chars_limit: int = 50) -> str:
        if not isinstance(name, str):
            raise TypeError('Неверный тип данных')
        if len(name) > chars_limit:
            raise ValueError(f'Превышено допустимое количество ({chars_limit}) символов.')
        if not re.match(r'^[а-яА-ЯёЁ]+$', name):
            raise ValueError('Строка должна содержать только кириллические символы.')

        formatted_name = name.strip().lower().capitalize()
        if name != formatted_name:
            return formatted_name

        return name

    @staticmethod
    def format_email(*, email: str, chars_limit: int = 25) -> str:
        if not isinstance(email, str):
            raise TypeError('Неверный тип данных')
        if len(email) > chars_limit:
            raise ValueError(f'Превышено допустимое количество ({chars_limit}) символов.')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise TypeError('Ошибка при введении данных')

        formatted_email = email.strip().lower()
        if formatted_email != email:
            return formatted_email

        return email
