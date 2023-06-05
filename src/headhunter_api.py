from src.api import Engine
from src.exceptions import ParsingError
import requests


class HeadHunterAPI(Engine):
    """
    Класс для работы с API HeadHunter
    """

    # адрес API
    url = "https://api.hh.ru/vacancies/"

    def __init__(self, key):
        self.params = {
            "per_page": 100,
            "page": None,
            "text": key,
            "archived": False
        }
        # Тут наша прога
        self.headers = {
            "User-Agent": "HeadHunterAPI_cw4"
            }
        # СПИСОК ВАКАНСИЙ
        self.vacancies = []

    def get_request(self):
        """
        Метод создает запрос к api сайта
        :return: response.json()["Items"] список из item
        """
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f'Ошибка при получении вакансий! статус: {response.status_code}')
        return response.json()["items"]

    def get_vacancies(self, page_count=2):
        """
        получение вакансий
        :param page_count:
        :return:
        """
        self.vacancies = []  # очищение списка вакансий
        # постраничный перебор
        for page in range(page_count):
            page_vacancies = []
            self.params["page"] = page
            print(f"({self.__class__.__name__}) Парсинг страницы {page} -", end=" ")
            try:
                page_vacancies = self.get_request()
            except ParsingError as error:
                print(error)
            else:
                self.vacancies.extend(page_vacancies)
                print(f'Загружено вакансий: {len(page_vacancies)}')
            if len(page_vacancies) == 0:
                break

    def get_formatted_vacancies(self):
        """
        метод, добавляющий вакансии в отдельный список formatted_vacancies
        """
        formatted_vacancies = []

        for vacancy in self.vacancies:
            formatted_vacancy = {
                    'api': 'HeadHunter',  # API
                    'id': vacancy['id'],                               # id вакансии
                    'employer': vacancy['employer']['name'],    # название компании
                    'title': vacancy['name'],                   # профессия
                    'url': vacancy['alternate_url'],            # ссылка на вакансию
                    "experience": vacancy["experience"]["name"],    # Опыт
                    'area': vacancy["area"]["name"],                # место работы, локация
                    "type_of_work": vacancy["employment"]['name']   # полный/ неполный раб день
            }
            salary = vacancy['salary']
            if salary:
                if salary['from'] != 'null' or salary['to'] != 'null':
                    formatted_vacancy['salary_from'] = salary['from']  # ЗП от
                    formatted_vacancy['salary_to'] = salary['to']  # ЗП до
                    formatted_vacancy['currency'] = salary['currency']  # валюта
            else:
                formatted_vacancy['salary_from'] = 0    # ЗП от
                formatted_vacancy['salary_to'] = 0      # ЗП до
                formatted_vacancy['currency'] = None        # валюта

            formatted_vacancies.append(formatted_vacancy)
            formatted_vacancy = {}

        return formatted_vacancies
