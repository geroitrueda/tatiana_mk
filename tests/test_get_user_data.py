import requests
import allure
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
EMAIL_ENDS = "reqres.in"
@allure.title("Проверяем получение списка пользователей")
def test_list_users():
    with allure.step("Делаем запрос по адресу api/users?page=2"):
        response = requests.get(BASE_URL + LIST_USERS)
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 200
    data = response.json()['data']
    for item in data:
        with allure.step("Проверяем элемент из списка"):
            validate(item, USER_DATA_SCHEME)
            with allure.step("Проверяем окончание имейл адреса"):
                assert item['email'].endswith(EMAIL_ENDS)