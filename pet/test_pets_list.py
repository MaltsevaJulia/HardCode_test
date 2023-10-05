def test_get_pets_200(get_data_pets):
    response = get_data_pets
    assert response.status_code == 200

def test_get_pets_check_content_type_equals_json(get_data_pets):
    response = get_data_pets
    assert response.headers['Content-Type'] == "application/json"

def test_get_pets_check_count_exist(get_data_pets):
    response_body = get_data_pets.json()
    assert "count" in response_body

def test_get_pets_check_next_exist(get_data_pets):
    response_body = get_data_pets.json()
    assert "next" in response_body

def test_get_pets_check_previous_exist(get_data_pets):
    response_body = get_data_pets.json()
    assert "previous" in response_body

def test_get_pets_check_results_exist(get_data_pets):
    response_body = get_data_pets.json()
    assert "results" in response_body

def test_get_pets_check_count_integer(get_data_pets):
    response_body = get_data_pets.json()
    assert type(response_body["count"]) == int

def test_get_pets_check_next_string(get_data_pets):
    response_body = get_data_pets.json()
    assert type(response_body["next"]) == str or response_body["next"] is None

def test_get_pets_check_previous_string(get_data_pets):
    response_body = get_data_pets.json()
    assert type(response_body["previous"]) == str or response_body["previous"] is None

def test_get_pets_check_results_id_int(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert type(item["id"]) == int

def test_get_pets_check_results_name_str(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert type(item["name"]) == str

def test_get_pets_check_results_name_len(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert len(item["name"]) <= 150

def test_get_pets_check_results_photo_url_str(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert type(item["photo_url"]) == str

def test_get_pets_check_results_photo_url_len(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert len(item["photo_url"]) <= 150

def test_get_pets_check_results_category_id_int(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert type(item["category"]["id"]) == int

def test_get_pets_check_results_category_name_str(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert type(item["category"]["name"]) == str

def test_get_pets_check_results_category_name_len(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert len(item["category"]["name"]) <= 150

def test_get_pets_check_results_status_str(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert type(item["status"]) == str

def test_get_pets_check_results_status_StatusEnum(get_data_pets):
    response_body = get_data_pets.json()
    results = response_body["results"]

    for item in results:
        assert item["status"] == 'available' or item["status"] == 'pending' or item["status"] == 'sold'


def test_post_pets_201(create_pet):
    response = create_pet
    assert response.status_code == 201

def test_post_pets_check_content_type_equals_json(create_pet):
    response = create_pet
    assert response.headers['Content-Type'] == "application/json"

def test_post_pets_check_id_exist(create_pet):
    response_body = create_pet.json()
    assert "id" in response_body

def test_post_pets_check_name_exist(create_pet):
    response_body = create_pet.json()
    assert "name" in response_body

def test_post_pets_check_photo_url_exist(create_pet):
    response_body = create_pet.json()
    assert "photo_url" in response_body

def test_post_pets_check_name_category_exist(create_pet):
    response_body = create_pet.json()
    assert "name" in response_body["category"]

def test_post_pets_check_status_exist(create_pet):
    response_body = create_pet.json()
    assert "status" in response_body

def test_post_pets_check_id_int(create_pet):
    response_body = create_pet.json()
    assert type(response_body["id"]) == int

def test_post_pets_check_name_str(create_pet):
    response_body = create_pet.json()
    assert type(response_body["name"]) == str

def test_post_pets_check_photo_url_str(create_pet):
    response_body = create_pet.json()
    assert type(response_body["photo_url"]) == str

def test_post_pets_check_name_category_str(create_pet):
    response_body = create_pet.json()
    assert type(response_body["category"]["name"]) == str

def test_post_pets_check_name_len(create_pet):
    response_body = create_pet.json()
    assert len(response_body["name"]) <= 150

def test_post_pets_check_photo_url_len(create_pet):
    response_body = create_pet.json()
    assert len(response_body["photo_url"]) <= 150

def test_post_pets_check_name_category_len(create_pet):
    response_body = create_pet.json()
    assert len(response_body["category"]["name"]) <= 150

def test_post_pets_404(create_pet_error_category):
    response = create_pet_error_category
    assert response.status_code == 404