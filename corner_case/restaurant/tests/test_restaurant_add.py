import datetime

from django.test import TestCase, Client
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token

from corner_case.restaurant.models import Restaurant, Menu
from corner_case.users.models import User


class TestRestaurant(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin_user = User.objects.create_superuser("admin@test.com", "123456")
        self.admin_token = Token.objects.create(user=self.admin_user)

        self.employee_user = User.objects.create_user("employee@test.com", "123456")
        self.employee_token = Token.objects.create(user=self.employee_user)

        print(self.admin_user)
        print(self.admin_token)

        self.restaurant = baker.make(Restaurant)

    # admin is allowed to create restaurant
    def test_admin_menu_add(self):
        self.client = Client(HTTP_AUTHORIZATION="Token " + self.admin_token.key)

        response = self.client.post("/api/restaurants", {"name": "Test Restaurant"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # employee is not allowed to create restaurant
    def test_employee_menu_add(self):
        self.client = Client(HTTP_AUTHORIZATION="Token " + self.employee_token.key)

        response = self.client.post("/api/restaurants", {"name": "Test Restaurant"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_menu_add(self):
        self.client = Client(HTTP_AUTHORIZATION="Token " + self.admin_token.key)

        response = self.client.post(
            "/api/restaurants/menu",
            {
                "name": "Test Restaurant",
                "restaurant_id": self.restaurant.id,
                "date": datetime.date.today(),
            },
        )

        response_two = self.client.post(
            "/api/restaurants/menu",
            {
                "name": "Test Restaurant",
                "restaurant_id": self.restaurant.id,
                "date": datetime.date.today(),
            },
        )

        # can create a single menu for one day
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # can't create another menu for same restaurant same day
        self.assertEqual(response_two.status_code, status.HTTP_400_BAD_REQUEST)
