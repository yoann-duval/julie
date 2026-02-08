import unittest
from fastapi.testclient import TestClient
from src.main import app

class TestMagicLink(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_magic_link_flow(self):
        # 1. Generate Link
        response = self.client.post("/generate-magic-link", json={"first_name": "Alice"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("magic_link_url", data)
        token = data["token"]

        # 2. Consume Link (Success)
        response = self.client.get(f"/welcome?token={token}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Bonjour Alice", response.text)

        # 3. Consume Link (Again - Failure)
        response = self.client.get(f"/welcome?token={token}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "Ce lien a déjà été utilisé")

        # 4. Invalid Token
        response = self.client.get("/welcome?token=invalid-token")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Lien invalide")

if __name__ == "__main__":
    unittest.main()
