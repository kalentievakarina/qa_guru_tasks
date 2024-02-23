from datetime import time
from math import*


def test_dark_theme_by_time():
    print('Passed')
    current_time = time(hour=23)
    if time(hour=6) < current_time < time(hour=22):
        is_dark_theme = None
        print('Dark theme is disabled!')
    else:
        is_dark_theme = True
        print('Dark theme is enabled!')
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    dark_theme_enabled_by_user = True
    if dark_theme_enabled_by_user == True:
        is_dark_theme = True
        print('Dark theme is enabled!')
    elif dark_theme_enabled_by_user == False:
        is_dark_theme = None
        print('Dark theme is disabled!')
    elif dark_theme_enabled_by_user == None:
        current_time = time(hour=23)
        if time(hour=6) < current_time < time(hour=22):
            is_dark_theme = None
            print('Dark theme is disabled!')
        else:
            is_dark_theme = True
            print('Dark theme is enabled!')
    assert is_dark_theme is True
    print('All ok!')


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    suitable_users = None

    for user in users:
        if user['name'] == 'Olga':
            suitable_users = user
            print(f"name {user['name']}, age {user['age']}")
    assert suitable_users == {"name": "Olga", "age": 45}


def test_find_suitable_user_2():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    suitable_users = None
    suitable_users = []
    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)
    assert suitable_users == [{"name": "Stanislav", "age": 15}, {"name": "Maria", "age": 18}]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def prettifier_function_name(func, arg1: str, arg2: int) -> str:
    pretty_arguments = ', '.join(arg)
    pretty_function_name = func.__name__.replace("_", " ").title()
    return f'{pretty_function_name} [{pretty_arguments}]'

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    actual_result = prettifier_function_name(open_browser,browser_name)
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    actual_result = prettifier_function_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = prettifier_function_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
