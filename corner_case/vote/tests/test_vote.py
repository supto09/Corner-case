import datetime

from django.test import TestCase, Client
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token

from corner_case.restaurant.models import Restaurant, Menu
from corner_case.users.models import User


class TestVote(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user("employee@test.com", "123456")
        self.token = Token.objects.create(user=self.user)

        print(self.user)
        print(self.token)

        self.restaurant = baker.make(Restaurant)
        self.restaurant_two = baker.make(Restaurant)

        self.today_menu_one = baker.make(
            Menu, restaurant=self.restaurant, date=datetime.date.today()
        )
        self.today_menu_two = baker.make(
            Menu,
            restaurant=self.restaurant_two,
            date=datetime.date.today(),
        )
        self.tomorrow_menu_one = baker.make(
            Menu,
            restaurant=self.restaurant,
            date=datetime.date.today() + datetime.timedelta(days=+1),
        )

    def test_vote_create(self):
        self.client = Client(HTTP_AUTHORIZATION="Token " + self.token.key)

        today_vote_one_response = self.client.post(
            "/api/votes/create", {"menu_id": self.today_menu_one.id}
        )

        tomorrow_vote_response = self.client.post(
            "/api/votes/create", {"menu_id": self.tomorrow_menu_one.id}
        )

        # Can vote for a menu for a single day
        self.assertEqual(today_vote_one_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(tomorrow_vote_response.status_code, status.HTTP_201_CREATED)

        today_vote_two_response = self.client.post(
            "/api/votes/create", {"menu_id": self.today_menu_two.id}
        )
        # can't vote again for menu for same day'
        self.assertEqual(
            today_vote_two_response.status_code, status.HTTP_400_BAD_REQUEST
        )
