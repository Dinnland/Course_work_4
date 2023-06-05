from src.api import Engine
from src.exceptions import ParsingError
import requests


class SuperJobAPI(Engine):
    """
    Класс для работы с API SuperJob
    """
    url = "https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, key):
        self.params = {
            "count": 100,
            "page": None,
            "keyword": key,
            "archive": False
        }

        # ключ, токен приложения
        self.headers = {
            "X-Api-App-Id": "v3.r.137584905.526adb218b45b77ed30a754f011b6a193a8cd9e4.7c38987a8b44336c9b0b5aab57d13de6b36bdef3"
        }

        # СПИСОК ВАКАНСИЙ
        self.vacancies = []

    def get_vacancies(self, page_count=1):
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

    def get_request(self):
        """
        Метод делает запрос к API сайта
        :return: response.json()["objects"]
        """
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f'Ошибка при получении вакансий! статус: {response.status_code}')
        return response.json()["objects"]

    def get_formatted_vacancies(self):
        """
        метод, добавляющий вакансии в отдельный список formatted_vacancies
        """
        formatted_vacancies = []
        currency_trans = {
            'rub': "RUR",
            'uah': "UAH",
            'uzs': "UZS"
        }
        for vacancy in self.vacancies:
            formatted_vacancy = {
                'api': 'SuperJob',  # API
                'id': vacancy["id"],                     # id вакансии
                'employer': vacancy['firm_name'],        # название компании
                'title': vacancy["profession"],          # профессия
                'url': vacancy['link'],                  # ссылка на вакансию
                "experience": vacancy["experience"]["title"],       # Опыт
                'area': vacancy["town"]["title"],                   # место работы, локация
                "type_of_work": vacancy["type_of_work"]['title'],   # полный/ неполный раб день
                'salary_from': vacancy['payment_from'],  # ЗП от
                'salary_to': vacancy['payment_to'],      # ЗП до
                'currency': vacancy["currency"],         # валюта
                }
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies
