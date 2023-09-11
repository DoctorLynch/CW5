import os
from src.db_class import DBManager
from src.connect_to_hh import HH

if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.create_tables()

    hh = HH()
    hh.get_json_files()

    i = 1

    for file in os.listdir("/Users/Катюша/CW5/src/json_filepath/"):
        db_manager.insert_vacancies(file)
        i += 1

    print()
    print(db_manager.get_companies_and_vacancies_count())
    print()
    print(db_manager.get_all_vacancies())
    print()
    print(round(db_manager.get_avg_salary(), 1), 'руб. Средняя зарплата')
    print()
    for row in db_manager.get_vacancies_with_higher_salary():
        print(row)
        print()

    print()
    print(db_manager.get_vacancies_with_keyword("python"))

    db_manager.close_conn()
