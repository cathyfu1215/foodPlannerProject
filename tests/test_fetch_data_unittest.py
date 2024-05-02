'''
Cong (Cathy)Fu
Project - Food Planner
This is the unittest of the fetching_data_functions file .
'''

import requests
from requests.exceptions import HTTPError, ConnectionError
import unittest
import requests_mock


class TestFetchData(unittest.TestCase):
    def test_get_food_data(self):

        # for simplicity reasons, I will only test the english language options
        test_url = 'https://food-nutrition.canada.ca/api/canadian-nutrient-file/food'

        expected_data = [
            {
                "food_code": 571,
                "food_description": "Chicken, broiler, giblets, raw"
            },
            {
                "food_code": 572,
                "food_description": "Chicken, broiler, giblets, flour coated,\
                      fried"
            }
            ]

        with requests_mock.Mocker() as m:
            m.get(test_url, json=expected_data)
            response = requests.get(test_url)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()[0]["food_code"], 571)
            self.assertEqual(response.json()[1]["food_code"], 572)

    def test_get_empty_food_data(self):

        # for simplicity reasons, I will only test the english language options
        test_url = 'https://food-nutrition.canada.ca/api/canadian-nutrient-file/food'

        expected_data = []

        with requests_mock.Mocker() as m:
            m.get(test_url, json=expected_data)
            self.assertRaises(ValueError)

    def test_get_food_data_with_http_error(self):
        # a wrong url
        test_url = 'https://wrongfood-nutrition.canada.ca/api/canadian-nutrient-file/food'
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_get_food_data_with_connection_error(self):

        test_url = 'https://food-nutrition.canada.ca/api/canadian-nutrient-file/food'
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_get_nutrient_data(self):

        # for simplicity reasons, I will only test the english language options
        test_url = 'https://food-nutrition.canada.ca/api/canadian-nutrient-file/nutrientname'

        expected_data = [
                        {
                            "nutrient_name_id": 550,
                            "nutrient_symbol": "ASPA",
                            "nutrient_name": "ASPARTAME",
                            "unit": "mg",
                            "nutrient_code": 550,
                            "tagname": "",
                            "nutrient_decimals": 0,
                            "nutrient_web_order": 15,
                            "nutrient_web_name": "Aspartame",
                            "nutrient_group_id": 7
                        }
                        ]

        with requests_mock.Mocker() as m:
            m.get(test_url, json=expected_data)
            response = requests.get(test_url)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()[0]["nutrient_name_id"], 550)

    def test_get_empty_nutrient_data(self):

        # for simplicity reasons, I will only test the english language options
        test_url = 'https://food-nutrition.canada.ca/api/canadian-nutrient-file/nutrientname'

        expected_data = []

        with requests_mock.Mocker() as m:
            m.get(test_url, json=expected_data)
            self.assertRaises(ValueError)

    def test_get_nutrient_data_with_http_error(self):
        # a wrong url
        test_url = 'https://wrongfood-nutrition.canada.ca/api/canadian-nutrient-file/food'
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_get_nutrient_data_with_connection_error(self):

        test_url = 'https://food-nutrition.canada.ca/api/canadian-nutrient-file/nutrientname'
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_get_nutrient_amount(self):

        # for simplicity reasons, I will only test the english language options
        # I will use food 571 as an example

        test_url = 'https://food-nutrition.canada.ca/api/canadian-nutrient-file/nutrientamount/?id=571'

        expected_data = [
                        {
                            "food_code": 571,
                            "nutrient_value": 0.0,
                            "standard_error": 0,
                            "number_observation": 0,
                            "nutrient_name_id": 291,
                            "nutrient_web_name": "Fibre, total dietary",
                            "nutrient_source_id": 12
                        },
                        {
                            "food_code": 571,
                            "nutrient_value": 0.0,
                            "standard_error": 0,
                            "number_observation": 0,
                            "nutrient_name_id": 221,
                            "nutrient_web_name": "Alcohol",
                            "nutrient_source_id": 0
                        }
                        ]

        with requests_mock.Mocker() as m:
            m.get(test_url, json=expected_data)
            response = requests.get(test_url)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()[0]["nutrient_name_id"], 291)
            self.assertEqual(response.json()[1]["nutrient_name_id"], 221)

    def test_get_empty_nutrient_amount(self):

        # for simplicity reasons, I will only test the english language options
        test_url = 'https://food-nutrition.canada.ca/api/canadian-nutrient-file/nutrientamount/?id=571'

        expected_data = []

        with requests_mock.Mocker() as m:
            m.get(test_url, json=expected_data)
            self.assertRaises(ValueError)

    def test_get_nutrient_amount_with_http_error(self):
        # a wrong url
        test_url = 'https://wrongfood-nutrition.canada.ca/api/canadian-nutrient-file/food'
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_get_nutrient_amount_with_connection_error(self):

        test_url = 'https://food-nutrition.canada.ca/api/canadian-nutrient-file/nutrientamount/?id=571'
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)


if __name__ == "__main__":
    unittest.main()
