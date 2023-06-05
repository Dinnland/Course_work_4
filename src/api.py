from abc import ABC, abstractmethod


class Engine(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями
    """

    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

