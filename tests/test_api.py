import unittest
import requests
import subprocess
import time
import os
import signal

class TestUserAPI(unittest.TestCase):
    BASE_URL = "http://localhost:8000/api"
    server_process = None
    token = None

    @classmethod
    def setUpClass(cls):
        # Démarrer le serveur Django
        cls.server_process = subprocess.Popen(
            ["python", "manage.py", "runserver"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Attendre que le serveur démarre
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        # Arrêter le serveur Django
        if cls.server_process:
            os.kill(cls.server_process.pid, signal.SIGTERM)

    def setUp(self):
        # Login pour obtenir le token
        response = requests.post(
            f"{self.BASE_URL}/login/",
            json={"email": "test@example.com", "password": "password"}
        )
        if response.status_code == 200:
            self.token = response.json().get("access_token")

    def test_get_users(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.BASE_URL}/users/", headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {
            "name": "Test User",
            "email": "newuser@example.com",
            "password": "password123"
        }
        response = requests.post(
            f"{self.BASE_URL}/users/",
            json=data,
            headers=headers
        )
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main() 