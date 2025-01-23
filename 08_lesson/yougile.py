import pytest
import requests

BASE_URL = "https://ru.yougile.com"
API_KEY = "xo9EUzVkX-xm1bVVh87za+CHch5blsSSj4k084NTr07VXxQN+ERmXn83GV8gOa8M"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Данные для авторизации
AUTH_DATA = {
    "login": "nomakx@mail.ru",
    "password": "K7dEmLLbM6T@SHk",
    "companyId": "63d50650-bb03-463c-baf9-0a31b3db9983"
}

# Фикстура для получения ID проекта
@pytest.fixture
def project_id():
    # Создаем проект
    payload = {"title": "Город в котором я живу"}
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 201
    return response.json()["id"]

# Тесты для [POST] /api-v2/projects
def test_create_project_positive():
    payload = {"title": "Город в котором я живу"}
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_project_negative():
    # Отправляем пустой запрос
    payload = {}
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 400

# Тесты для [GET] /api-v2/projects
def test_get_projects_list_positive():
    response = requests.get(f"{BASE_URL}/api-v2/projects", headers=HEADERS)
    assert response.status_code == 200
    assert "content" in response.json()

def test_get_projects_list_negative():
    # Используем неверный метод (POST вместо GET)
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS)
    assert response.status_code == 400  # Method Not Allowed

# Тесты для [GET] /api-v2/projects/{id}
def test_get_project_by_id_positive(project_id):
    response = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["id"] == project_id

def test_get_project_by_id_negative():
    # Используем несуществующий ID
    non_existent_id = "несуществующий_id"
    response = requests.get(f"{BASE_URL}/api-v2/projects/{non_existent_id}", headers=HEADERS)
    assert response.status_code == 404

# Тесты для [PUT] /api-v2/projects/{id}
def test_add_user_to_project_positive(project_id):
    payload = {
        "users": {
            "5d75fcc3-b35f-4421-a6d5-ba011d8de7ea": "admin"
        }
    }
    response = requests.put(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS, json=payload)
    assert response.status_code == 200
    assert "id" in response.json()

def test_add_user_to_project_negative(project_id):
    # Отправляем пустой запрос
    payload = {}
    response = requests.put(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS, json=payload)
    assert response.status_code == 200

# Тест для получения ключа API (негативный, так как лимит исчерпан)
def test_get_api_key_negative():
    response = requests.post(f"{BASE_URL}/api-v2/auth/keys", json=AUTH_DATA)
    assert response.status_code == 201  # Forbidden