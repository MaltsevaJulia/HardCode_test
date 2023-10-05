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
def get_data_pets():
    print('\nПолучения животных')
    response = requests.get(BASE_URL+"pet/", auth=('admin', 'admin'))
    return response

@pytest.fixture(scope='session')
def create_pet():
    print('\nСоздания животного')
    hash = hex(random.getrandbits(128))
    response = requests.post(BASE_URL+"pet/", json={'name': 'test-name-'+hash, 'photo_url': 'test-url-'+hash, 'category': {'name': 'cat'}, 'status': 'available'}, auth=('admin', 'admin'))
    return response

@pytest.fixture(scope='session')
def create_pet_error_category():
    print('\nСоздания животного в некорректной категории')
    hash = hex(random.getrandbits(128))
    response = requests.post(BASE_URL+"pet/", json={'name': 'test-name-'+hash, 'photo_url': 'test-url-'+hash, 'category': {'name': 'chair'}, 'status': 'available'}, auth=('admin', 'admin'))
    return response

@pytest.fixture(scope='session')
def get_data_pet():
    print('\nПолучение данных животного')
    hash = hex(random.getrandbits(128))
    respost = requests.post(BASE_URL+"pet/", json={'name': 'test-name-'+hash, 'photo_url': 'test-url-'+hash, 'category': {'name': 'cat'}, 'status': 'available'}, auth=('admin', 'admin'))
    respost_body = respost.json()
    pet_id = str(respost_body["id"])

    response = requests.get(BASE_URL+"pet/" + pet_id + "/", auth=('admin', 'admin'))

    return response

@pytest.fixture(scope='session')
def update_pet():
    print('\nОбновление данных животного')
    hash = hex(random.getrandbits(128))
    respost = requests.post(BASE_URL+"pet/", json={'name': 'test-name-'+hash, 'photo_url': 'test-url-'+hash, 'category': {'name': 'cat'}, 'status': 'available'}, auth=('admin', 'admin'))
    respost_body = respost.json()
    pet_id = str(respost_body["id"])

    hash = hex(random.getrandbits(128))
    response = requests.put(BASE_URL + "pet/" + pet_id + "/", json={'name': 'test-name-'+hash, 'photo_url': 'test-url-'+hash, 'category': {'name': 'cat'}, 'status': 'available'}, auth=('admin', 'admin'))

    return response

@pytest.fixture(scope='session')
def delete_pet():
    print('\nУдаление животного')
    hash = hex(random.getrandbits(128))
    respost = requests.post(BASE_URL+"pet/", json={'name': 'test-name-'+hash, 'photo_url': 'test-url-'+hash, 'category': {'name': 'cat'}, 'status': 'available'}, auth=('admin', 'admin'))
    respost_body = respost.json()
    pet_id = str(respost_body["id"])

    response = requests.delete(BASE_URL + "pet/" + pet_id + "/", auth=('admin', 'admin'))

    return response
