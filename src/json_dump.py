import json
import os
from src.saver import Saver


class JSONDumpLoad(Saver):
    """
    Класс для записи в JSON и чтения данного файла
    """

    file_name = 'vacancy.json'

    @classmethod
    def json_writer(cls, vacancy: dict):
        """
        Запись в файл JSON
        """
        with open(cls.file_name, 'w', encoding='utf-8') as f:
            json.dump(vacancy, f, indent=4, ensure_ascii=False)

    @classmethod
    def json_reader(cls):
        """
        Чтение файла JSON
        """
        with open(cls.file_name, 'r', encoding='UTF-8') as file:
            return json.load(file)
