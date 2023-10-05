def test_get_category_id_200(get_data_category):
    response = get_data_category
    assert response.status_code == 200

def test_get_category_id_check_content_type_equals_json(get_data_category):
    response = get_data_category
    assert response.headers['Content-Type'] == "application/json"

def test_get_category_id_check_id_exist(get_data_category):
    response_body = get_data_category.json()
    assert "id" in response_body

def test_get_category_id_check_name_exist(get_data_category):
    response_body = get_data_category.json()
    assert "name" in response_body

def test_get_category_id_check_id_integer(get_data_category):
    response_body = get_data_category.json()
    assert type(response_body["id"]) == int

def test_get_category_id_check_name_string(get_data_category):
    response_body = get_data_category.json()
    assert type(response_body["name"]) == str

def test_get_category_id_check_name_len(get_data_category):
    response_body = get_data_category.json()
    assert len(response_body["name"]) <= 150

def test_put_category_id_200(update_category):
    response = update_category
    assert response.status_code == 200

def test_put_category_id_check_content_type_equals_json(update_category):
    response = update_category
    assert response.headers['Content-Type'] == "application/json"

def test_put_category_id_check_id_exist(update_category):
    response_body = update_category.json()
    assert "id" in response_body

def test_put_category_id_check_name_exist(update_category):
    response_body = update_category.json()
    assert "name" in response_body

def test_put_category_id_check_id_int(update_category):
    response_body = update_category.json()
    assert type(response_body["id"]) == int

def test_put_category_id_check_name_str(update_category):
    response_body = update_category.json()
    assert type(response_body["name"]) == str

def test_put_category_id_check_name_len(update_category):
    response_body = update_category.json()
    assert len(response_body["name"]) <= 150

def test_delete_category_id_204(delete_category):
    response = delete_category
    assert response.status_code == 204

def test_delete_category_id_check_content_type_equals_json(delete_category):
    response = delete_category
    assert 'Content-Type' in response.headers and response.headers['Content-Type'] == "application/json"

def test_delete_category_id_check_id_exist(delete_category):
    response_body = {}

    if "json" in delete_category:
        response_body = delete_category.json()

    assert "id" in response_body

def test_delete_category_id_check_name_exist(delete_category):
    response_body = {}

    if "json" in delete_category:
        response_body = delete_category.json()

    assert "name" in response_body

def test_delete_category_id_check_id_int(delete_category):
    response_body = {}

    if "json" in delete_category:
        response_body = delete_category.json()

    assert "id" in response_body and type(response_body["id"]) == int

def test_delete_category_id_check_name_str(delete_category):
    response_body = {}

    if "json" in delete_category:
        response_body = delete_category.json()

    assert "name" in response_body and type(response_body["name"]) == str

def test_delete_category_id_check_name_len(delete_category):
    response_body = {}

    if "json" in delete_category:
        response_body = delete_category.json()

    assert "name" in response_body and len(response_body["name"]) <= 150
