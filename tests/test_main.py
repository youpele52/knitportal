from unittest import TestCase
from fastapi.testclient import TestClient
from knitportal.main import app


class TestMain(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "you've reached the knitportal"})
