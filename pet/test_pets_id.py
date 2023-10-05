import requests
import random

BASE_URL = "http://91.210.171.73:8080/api/"  # API endpoint

def create_pet():
    hash = hex(random.getrandbits(128))
    respost = requests.post(BASE_URL + "pet/", json={'name': 'test-name-'+hash, 'photo_url': 'test-url-'+hash, 'category': {'name': 'cat'}, 'status': 'available'}, auth=('admin', 'admin'))
    respost_body = respost.json()
    pet_id = str(respost_body["id"])
    return pet_id

def test_get_pets_id_200(get_data_pet):
    response = get_data_pet
    assert response.status_code == 200

def test_get_pets_id_check_content_type_equals_json(get_data_pet):
    response = get_data_pet
    assert response.headers['Content-Type'] == "application/json"

def test_get_pets_id_check_id_exist(get_data_pet):
    response_body = get_data_pet.json()
    assert "id" in response_body

def test_get_pets_id_check_name_exist(get_data_pet):
    response_body = get_data_pet.json()
    assert "name" in response_body

def test_get_pets_id_check_photo_url_exist(get_data_pet):
    response_body = get_data_pet.json()
    assert "photo_url" in response_body

def test_get_pets_id_check_id_category_exist(get_data_pet):
    response_body = get_data_pet.json()
    assert "category" in response_body and "id" in response_body["category"]

def test_get_pets_id_check_name_category_exist(get_data_pet):
    response_body = get_data_pet.json()
    assert "category" in response_body and "name" in response_body["category"]

def test_get_pets_id_check_status_exist(get_data_pet):
    response_body = get_data_pet.json()
    assert "status" in response_body

def test_get_pets_id_check_results_id_int(get_data_pet):
    response_body = get_data_pet.json()
    assert "id" in response_body and type(response_body["id"]) == int

def test_get_pets_id_check_results_name_str(get_data_pet):
    response_body = get_data_pet.json()
    assert "name" in response_body and type(response_body["name"]) == str

def test_get_pets_id_check_results_name_len(get_data_pet):
    response_body = get_data_pet.json()
    assert "name" in response_body and len(response_body["name"]) <= 150

def test_get_pets_id_check_results_photo_url_str(get_data_pet):
    response_body = get_data_pet.json()
    assert "photo_url" in response_body and type(response_body["photo_url"]) == str

def test_get_pets_id_check_results_photo_url_len(get_data_pet):
    response_body = get_data_pet.json()
    assert "photo_url" in response_body and len(response_body["photo_url"]) <= 150

def test_get_pets_id_check_results_id_category_int(get_data_pet):
    response_body = get_data_pet.json()
    assert "category" in response_body and type(response_body["category"]["id"]) == int

def test_get_pets_id_check_results_name_category_str(get_data_pet):
    response_body = get_data_pet.json()
    assert "category" in response_body and type(response_body["category"]["name"]) == str

def test_get_pets_id_check_results_name_category_len(get_data_pet):
    response_body = get_data_pet.json()
    assert "category" in response_body and len(response_body["category"]["name"]) <= 150

def test_put_pets_id_200(update_pet):
    response = update_pet
    assert response.status_code == 200

def test_put_pets_id_check_content_type_equals_json(update_pet):
    response = update_pet
    assert response.headers['Content-Type'] == "application/json"

def test_put_pets_id_check_id_exist(update_pet):
    response_body = update_pet.json()
    assert "id" in response_body

def test_put_pets_id_check_name_exist(update_pet):
    response_body = update_pet.json()
    assert "name" in response_body

def test_put_pets_id_check_photo_url_exist(update_pet):
    response_body = update_pet.json()
    assert "photo_url" in response_body

def test_put_pets_id_check_id_category_exist(update_pet):
    response_body = update_pet.json()
    assert "category" in response_body and "id" in response_body["category"]

def test_put_pets_id_check_name_category_exist(update_pet):
    response_body = update_pet.json()
    assert "category" in response_body and "name" in response_body["category"]

def test_put_pets_id_check_status_exist(update_pet):
    response_body = update_pet.json()
    assert "status" in response_body

def test_put_pets_id_check_id_int(update_pet):
    response_body = update_pet.json()
    assert "id" in response_body and type(response_body["id"]) == int

def test_put_pets_id_check_name_str(update_pet):
    response_body = update_pet.json()
    assert "name" in response_body and type(response_body["name"]) == str

def test_put_pets_id_check_photo_url_str(update_pet):
    response_body = update_pet.json()
    assert "photo_url" in response_body and type(response_body["photo_url"]) == str

def test_put_pets_id_check_category_id_int(update_pet):
    response_body = update_pet.json()
    assert "category" in response_body and "id" in response_body["category"] and type(response_body["category"]["id"]) == int

def test_put_pets_id_check_category_name_str(update_pet):
    response_body = update_pet.json()
    assert "category" in response_body and "name" in response_body["category"] and type(response_body["category"]["name"]) == str

def test_get_pets_check_results_status_StatusEnum(update_pet):
    response_body = update_pet.json()
    assert "status" in response_body and response_body["status"] in ('available', 'pending', 'sold')

def test_put_pets_id_check_name_len(update_pet):
    response_body = update_pet.json()
    assert "name" in response_body and len(response_body["name"]) <= 150

def test_put_pets_id_check_photo_url_len(update_pet):
    response_body = update_pet.json()
    assert "photo_url" in response_body and len(response_body["photo_url"]) <= 150

def test_put_pets_id_check_category_name_len(update_pet):
    response_body = update_pet.json()
    assert "category" in response_body and "name" in response_body["category"] and len(response_body["category"]["name"]) <= 150

def test_delete_pets_id_204(delete_pet):
     response = delete_pet
     assert response.status_code == 204

def test_delete_pets_id_check_content_type_equals_json(delete_pet):
    response = delete_pet
    assert 'Content-Type' in response.headers and response.headers['Content-Type'] == "application/json"

def test_delete_pets_id_check_id_exist(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "id" in response_body

def test_delete_pets_id_check_name_exist(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "name" in response_body

def test_delete_pets_id_check_photo_url_exist(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "photo_url" in response_body

def test_delete_pets_id_check_id_category_exist(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "category" in response_body and "id" in response_body["category"]

def test_delete_pets_id_check_name_category_exist(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "category" in response_body and "name" in response_body["category"]

def test_delete_pets_id_check_statys_exist(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "status" in response_body and "status" in response_body

def test_delete_pets_id_check_id_int(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "id" in response_body and type(response_body["id"]) == int

def test_delete_pets_id_check_name_str(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "name" in response_body and type(response_body["name"]) == str

def test_delete_pets_id_check_photo_url_str(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "photo_url" in response_body and type(response_body["photo_url"]) == str

def test_delete_pets_id_check_category_id_int(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "category" in response_body and type(response_body["category"]["id"]) == int

def test_delete_pets_id_check_category_name_str(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "category" in response_body and type(response_body["category"]["id"]) == str

def test_delete_pets_id_check_status_str(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "status" in response_body and type(response_body["status"]) == str

def test_delete_pets_id_check_name_len(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "name" in response_body and len(response_body["name"]) <= 150

def test_delete_pets_id_check_photo_url_len(delete_pet):
    response_body = {}

    if "json" in delete_pet:
        response_body = delete_pet.json()

    assert "photo_url" in response_body and len(response_body["photo_url"]) <= 150
