import json


class JsonFileHandler:

    @staticmethod
    def read_file(filename: str) -> list:
        try:
            with open(filename, mode='r', encoding='UTF-8') as file:
                return json.load(file)
        except Exception as e:
            print(f'Не удалось получить список контактов. Ошибка: {e}')

    @staticmethod
    def write_file(filename: str, data):
        try:
            with open(filename, 'w', encoding='UTF-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                print(f'Данные сохранены: {data}')
        except Exception as e:
            print(f'Не удалось обновить список контактов. Ошибка: {e}')
