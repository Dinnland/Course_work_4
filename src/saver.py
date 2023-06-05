from abc import ABC, abstractmethod


class Saver(ABC):
    """
    Запись полученных вакансий в файл json
    """
    @abstractmethod
    def json_writer(self, vacancies: dict):
        pass

    @abstractmethod
    def json_reader(self):
        pass
