import requests
import random

import pytest

BASE_URL = "http://91.210.171.73:8080/api/"  # API endpoint

sess = requests.session()

# @pytest.fixture(autouse=True, scope='session')
# def auth():
#     print('\nРабота фикстуры авторизации')
#
#     res = sess.post(BASE_URL+"/auth/signin/", '{"login": "cajacoptest", "password": "0f282a4f102bf3b171e3b742c0021c7d"}')
#
#     print('\nВозврат фикстуры авторизации')
#     return res

@pytest.fixture(scope='session')
def get_data_categoryes():
    print('\nПолучения категорий')
    response = sess.get(BASE_URL+"category/", auth=('admin', 'admin'))
    return response

@pytest.fixture(scope='session')
def create_category():
    print('\nСоздания категории')
    hash = hex(random.getrandbits(128))
    response = requests.post(BASE_URL+"category/", json={'name': 'test-name-'+hash}, auth=('admin', 'admin'))
    return response

@pytest.fixture(scope='session')
def get_data_category():
    print('\nПолучение данных категории')
    hash = hex(random.getrandbits(128))
    respost = requests.post(BASE_URL + "category/", json={'name': 'test-name-' + hash}, auth=('admin', 'admin'))
    respost_body = respost.json()
    cat_id = str(respost_body["id"])

    response = requests.get(BASE_URL+"category/" + cat_id + "/", auth=('admin', 'admin'))

    return response

@pytest.fixture(scope='session')
def update_category():
    print('\nОбновление данных категории')
    hash = hex(random.getrandbits(128))
    respost = requests.post(BASE_URL + "category/", json={'name': 'test-name-' + hash}, auth=('admin', 'admin'))
    respost_body = respost.json()
    cat_id = str(respost_body["id"])

    response = requests.put(BASE_URL + "category/" + cat_id + "/", json={'name': 'test-name-' + hash}, auth=('admin', 'admin'))

    return response

@pytest.fixture(scope='session')
def delete_category():
    print('\nУдаление категории')
    hash = hex(random.getrandbits(128))
    respost = requests.post(BASE_URL + "category/", json={'name': 'test-name-' + hash}, auth=('admin', 'admin'))
    respost_body = respost.json()
    cat_id = str(respost_body["id"])

    response = requests.delete(BASE_URL+"category/"+cat_id+"/", auth=('admin', 'admin'))

    return response
