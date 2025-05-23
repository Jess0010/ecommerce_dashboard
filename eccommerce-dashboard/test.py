import unittest
from app import app


class TestApiEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_low_stock_levels(self):
        # Test the endpoint for the low stock levels api
        # Send a GET request to the endpoint
        response = self.app.get("api/low_stock_levels")
        # Check the status code of the response is 200
        self.assertEqual(response.status_code, 200)

        # Test if the response is in JSON format
        self.assertTrue(response.is_json)

        # Test if the response contains al the expected keys
        self.assertTrue("products" in response.json)
        self.assertTrue("quantities" in response.json)

        # Test if the products response is shown aas a list
        self.assertIsInstance(response.json["products"], list)

        # Test to see if quantities response is in integer form
        self.assertTrue(all(isinstance(x, int) for x in response.json["quantities"]))


if __name__ == "__main__":
    unittest.main()
