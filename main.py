import requests


def search_vacancies():
    # Базовый URL для API HeadHunter
    base_url = "https://api.hh.ru/vacancies"

    # Параметры запроса
    params = {
        "text": "системный администратор",  # Поисковый запрос
        "area": 43,  # Калужская область (код 43 в hh)
        "salary": 100000,  # Минимальная зарплата
        "salary_to": 200000,  # Максимальная зарплата
        "only_with_salary": True,  # Только вакансии с указанной зарплатой
        "per_page": 100,  # Количество результатов на странице (максимум 100)
        "page": 0  # Номер страницы (начинается с 0)
    }

    try:
        # Отправляем GET-запрос
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Проверяем на ошибки

        # Получаем JSON-ответ
        data = response.json()

        # Выводим информацию о найденных вакансиях
        print(f"Найдено вакансий: {data['found']}")
        print(f"Обработано: {len(data['items'])}")

        for vacancy in data['items']:
            salary_from = vacancy['salary'].get('from', 'не указана')
            salary_to = vacancy['salary'].get('to', 'не указана')
            salary_currency = vacancy['salary'].get('currency', '')

            print("\n---")
            print(f"Должность: {vacancy['name']}")
            print(f"Компания: {vacancy['employer']['name']}")
            print(f"Зарплата: от {salary_from} до {salary_to} {salary_currency}")
            print(f"Ссылка на вакансию: {vacancy['alternate_url']}")

            # Если есть прикрепленные файлы, выводим ссылки на них
            if 'resume_access' in vacancy and vacancy['resume_access'] and 'url' in vacancy['resume_access']:
                print(f"Ссылка на прикрепленные файлы: {vacancy['resume_access']['url']}")
            else:
                print("Прикрепленные файлы: отсутствуют")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")


if __name__ == "__main__":
    search_vacancies()