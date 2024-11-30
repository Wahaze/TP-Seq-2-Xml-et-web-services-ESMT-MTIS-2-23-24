import requests

BASE_URL = "http://localhost:8000/api"

def login():
    url = f"{BASE_URL}/login/"
    payload = {"email": "user@example.com", "password": "password"}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        token = response.json().get("access_token")
        print("Connexion réussie ! Token:", token)
        return token
    print("Échec de la connexion !")
    return None

def get_users(token):
    url = f"{BASE_URL}/users/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("Réponse GET /users:", response.json())

def create_user(token):
    url = f"{BASE_URL}/users/"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "name": "Adama",
        "email": "adama@example.com",
        "password": "password"
    }
    response = requests.post(url, json=payload, headers=headers)
    print("Réponse POST /users:", response.json())

def update_user(token, user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "name": "Adama Updated",
        "email": "adama_updated@example.com",
        "password": "new_password"
    }
    response = requests.put(url, json=payload, headers=headers)
    print(f"Réponse PUT /users/{user_id}:", response.json())

def delete_user(token, user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    print(f"Réponse DELETE /users/{user_id}:", response.status_code)

if __name__ == "__main__":
    token = login()
    if token:
        get_users(token)
        create_user(token)
        update_user(token, 1)
        delete_user(token, 1) 