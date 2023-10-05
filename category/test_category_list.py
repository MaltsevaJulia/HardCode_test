def test_get_category_200(get_data_categoryes):
    response = get_data_categoryes
    assert response.status_code == 200

def test_get_category_check_content_type_equals_json(get_data_categoryes):
    response = get_data_categoryes
    assert response.headers['Content-Type'] == "application/json"

def test_get_category_check_count_exist(get_data_categoryes):
    response_body = get_data_categoryes.json()
    assert "count" in response_body

def test_get_category_check_next_exist(get_data_categoryes):
    response_body = get_data_categoryes.json()
    assert "next" in response_body

def test_get_category_check_previous_exist(get_data_categoryes):
    response_body = get_data_categoryes.json()
    assert "previous" in response_body

def test_get_category_check_results_exist(get_data_categoryes):
    response_body = get_data_categoryes.json()
    assert "results" in response_body

def test_get_category_check_count_integer(get_data_categoryes):
    response_body = get_data_categoryes.json()
    assert type(response_body["count"]) == int

def test_get_category_check_next_string(get_data_categoryes):
    response_body = get_data_categoryes.json()
    assert type(response_body["next"]) == str or response_body["next"] is None

def test_get_category_check_previous_string(get_data_categoryes):
    response_body = get_data_categoryes.json()
    assert type(response_body["previous"]) == str or response_body["previous"] is None

def test_get_category_check_results_id_int(get_data_categoryes):
    response_body = get_data_categoryes.json()
    results = response_body["results"]

    for item in results:
        assert type(item["id"]) == int

def test_get_category_check_results_name_str(get_data_categoryes):
    response_body = get_data_categoryes.json()
    results = response_body["results"]

    for item in results:
        assert type(item["name"]) == str

def test_get_category_check_results_name_len(get_data_categoryes):
    response_body = get_data_categoryes.json()
    results = response_body["results"]

    for item in results:
        assert len(item["name"]) <= 150

def test_post_category_201(create_category):
    response = create_category
    assert response.status_code == 201

def test_post_category_check_content_type_equals_json(create_category):
    response = create_category
    assert response.headers['Content-Type'] == "application/json"

def test_post_category_check_id_exist(create_category):
    response_body = create_category.json()
    assert "id" in response_body

def test_post_category_check_name_exist(create_category):
    response_body = create_category.json()
    assert "name" in response_body

def test_post_category_check_id_int(create_category):
    response_body = create_category.json()
    assert type(response_body["id"]) == int

def test_post_category_check_name_str(create_category):
    response_body = create_category.json()
    assert type(response_body["name"]) == str

def test_post_category_check_name_len(create_category):
    response_body = create_category.json()
    assert len(response_body["name"]) <= 150
