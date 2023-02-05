import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DepositTestCase(APITestCase):

    def test_post_with_valid_data(self):
        url = reverse('deposits')
        data = {
            "date": "01.01.2021",
            "periods": 3,
            "amount": 10000,
            "rate": 6
        }
        expected_data = {
            "01.02.2021": 10050.0,
            "01.03.2021": 10100.25,
            "01.04.2021": 10150.75
        }
        json_data = json.dumps(data)
        response = self.client.post(
            url,
            data=json_data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_model_validation_with_not_valid_data(self):
        url = reverse('deposits')
        data = {
            "date": "1.01.2021",
            "periods": "2 месяца",
            "amount": 10000.50,
            "rate": 0.5
        }
        expected_error = {
            "date": [
                "Enter a valid value."
            ],
            "periods": [
                "A valid integer is required."
            ],
            "amount": [
                "A valid integer is required."
            ],
            "rate": [
                "Ensure this value is greater than or equal to 1."
            ]
        }
        json_data = json.dumps(data)
        response = self.client.post(
            url,
            data=json_data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(expected_error, response.data)

    def test_post_with_not_valid_date(self):
        url = reverse('deposits')
        data = {
            "date": "99.99.9999",
            "periods": 5,
            "amount": 10000,
            "rate": 6
        }
        expected_error = {
            "non_field_errors": [
                "Введенная дата не корректна"
            ]
        }
        json_data = json.dumps(data)
        response = self.client.post(
            url,
            data=json_data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(expected_error, response.data)

    def test_post_with_not_valid_periods(self):
        url = reverse('deposits')
        data = {
            "date": "01.01.2021",
            "periods": 100,
            "amount": 10000,
            "rate": 6
        }
        expected_error = {
            "non_field_errors": [
                "Период вклада может быть от 1 до 60 месяцев"
            ]
        }
        json_data = json.dumps(data)
        response = self.client.post(
            url,
            data=json_data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(expected_error, response.data)

    def test_post_with_not_valid_amount(self):
        url = reverse('deposits')
        data = {
            "date": "01.01.2021",
            "periods": 5,
            "amount": 100,
            "rate": 6
        }
        expected_error = {
            "non_field_errors": [
                "Вклад может быть от 10000 до 3000000"
            ]
        }
        json_data = json.dumps(data)
        response = self.client.post(
            url,
            data=json_data,
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(expected_error, response.data)
