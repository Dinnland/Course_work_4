import json
from src.vacancy import Vacancy


class Connector:
    def __init__(self, user_keyword, vacancies_json):
        self.connect_file = f'{user_keyword.title()}.json'
        self.insert(vacancies_json)

    def insert(self, vacancies_json):
        with open(self.connect_file, 'w', encoding='utf-8') as f:
            json.dump(vacancies_json, f, indent=4, ensure_ascii=False) # ,  ensure_ascii=False

    def select(self):
        with open(self.connect_file, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        return [Vacancy(x) for x in vacancies]

    def sort_by_salary(self):
        desc = True if input(
            '1 - по убыванию зп \n'  # зп от макс к мин
            '2 - по увеличению зп \n>>> '  # НАОБОРОТ
        ) == '1' else False
        vacancies = self.select()

        return sorted(vacancies, key=lambda x: (x.salary_from if x.salary_from else 0, x.salary_to if x.salary_to else 0), reverse=desc)

    def area_sort(self):
        # area = input('Введите название города')
        area_sort = True if input(
            '1 - Я - А \n'  
            '2 - А - Я \n>>> '
        ) == '1' else False
        vacancies = self.select()
        return sorted(vacancies, key=lambda x: x.area, reverse=area_sort)
