import re


class Validator:

    @staticmethod
    def format_name(name: str, chars_limit: int = 50) -> str:
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
    def format_email(email: str, chars_limit: int = 25) -> str:
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

    @staticmethod
    def format_address(
            city: str,
            street: str,
            house_number: str,
            apartment_number: str,
            chars_limit: int = 150
    ) -> str:

        address_data = {
            'city': city,
            'street': street,
            'house_number': house_number,
            'apartment_number': apartment_number
        }

        for value in address_data.values():
            if not isinstance(value, str):
                raise TypeError('Неверный тип данных')
        for value in address_data.values():
            if not re.match(r'^[А-ЯЁа-яё0-9\s-]+$', value):
                raise ValueError('Строка должна содержать только кириллические символы.')
        for key, value in address_data.items():
            address_data[key] = value.capitalize()

        formatted_address = f'г. {city}, ул. {street}, д. {house_number}, кв. {apartment_number}'
        if len(formatted_address) > chars_limit:
            raise ValueError(f'Превышено допустимое количество ({chars_limit}) символов.')

        return formatted_address
