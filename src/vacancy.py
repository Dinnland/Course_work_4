
class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, vacancy: dict):
        self.api = vacancy['api']  # API
        self.id = vacancy["id"]  # id вакансии
        self.employer = vacancy['employer']  # название компании
        self.title = vacancy["title"]  # профессия
        self.url = vacancy['url']  # ссылка на вакансию
        self.experience = vacancy["experience"]  # Опыт
        self.area = vacancy["area"]  # место работы, локация
        self.type_of_work = vacancy["type_of_work"]   # полный/ неполный раб день
        self.salary_from = vacancy['salary_from']  # ЗП от
        self.salary_to = vacancy['salary_to']  # ЗП до
        self.currency = vacancy["currency"]

    def __str__(self):
        return f"""
        Работодатель: \'{self.employer}\'
        Должность: '{self.title}'
        Опыт: '{self.experience}'
        ЗП от: '{self.salary_from}'
        ЗП до: '{self.salary_to}'
        Валюта: '{self.currency}'
        Ссылка: '{self.url}'
        Место работы: '{self.area}'
        """
