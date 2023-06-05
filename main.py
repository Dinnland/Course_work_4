from src.headhunter_api import HeadHunterAPI
from src.superjob_api import SuperJobAPI
from src.json_dump import JSONDumpLoad
from src.connector import Connector
from src.vacancy import Vacancy


def main():

    vacancies_json = []
    user_keyword = input("Введите ключевое слова для поиска\n")
    # user_keyword = "Python"

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI(user_keyword)
    super_job_api = SuperJobAPI(user_keyword)

    choice_api = input('Выберите с какого сайта необходимо собрать вакансии.\n'
                    '1.HeadHunter\n'
                    '2.SuperJobAPI\n'
                    '3.Со всех\n'
                    'Укажите номер пункта: ')

    pages = int(input('Введите оличество страниц\n'
                  '0-20\n'))

    while True:
        if choice_api == '1':
            hh_api.get_vacancies(pages)
            # hh_api.get_formatted_vacancies()
            vacancies_json.extend(hh_api.get_formatted_vacancies())
            break
        elif choice_api == '2':
            super_job_api.get_vacancies(pages)
            super_job_api.get_formatted_vacancies()
            # print(sjfv)
            vacancies_json.extend(super_job_api.get_formatted_vacancies())
            break
        elif choice_api == '3':
            for api in (super_job_api, hh_api):  # , hh_api):
                # page_count - кол-во страниц
                api.get_vacancies(page_count=pages)
                vacancies_json.extend(api.get_formatted_vacancies())
                yy = api.get_formatted_vacancies()
                # print(vacancies_json)
            break

    # print(vacancies_json)
    connector = Connector(user_keyword=user_keyword, vacancies_json=vacancies_json)
    vacancies = connector.select()

    while True:
        command = input(
            '1 - Вывести список вакансий\n'
            '2 - Отсортировать по зп\n'
            '3 - Сортировать по городу\n'
            'exit - Выход\n'
            '>>> '
        )
        if command.lower() == 'exit':
            break
        elif command == '1':
            vacancies = connector.select()
        elif command == '2':
            vacancies = connector.sort_by_salary()
        elif command == '3':
            vacancies = connector.area_sort()
        for vacc in vacancies:
            print(vacc, end='\n')

    # # Получение вакансий с разных платформ
    # hh_vacancies = hh_api.get_vacancies("Python")
    # # superjob_vacancies = superjob_api.get_vacancies("Python")
    #
    # # Создание экземпляра класса для работы с вакансиями
    # vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
    #                   "Требования: опыт работы от 3 лет...")

    # # Сохранение информации о вакансиях в файл
    # json_saver = JSONSaver()
    # json_saver.add_vacancy(vacancy)
    # json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
    # json_saver.delete_vacancy(vacancy)
    #
    # # Функция для взаимодействия с пользователем
    # def user_interaction():
    #     platforms = ["HeadHunter", "SuperJob"]
    #     search_query = input("Введите поисковый запрос: ")
    #     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    #     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    #     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
    #
    #     if not filtered_vacancies:
    #         print("Нет вакансий, соответствующих заданным критериям.")
    #         return
    #
    #     sorted_vacancies = sort_vacancies(filtered_vacancies)
    #     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    #     print_vacancies(top_vacancies)



if __name__ == "__main__":
    main()
