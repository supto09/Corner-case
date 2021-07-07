import datetime

from django.test import TestCase
from model_bakery import baker

from corner_case.restaurant.models import Restaurant, Menu
from corner_case.vote.api.views import get_menu_sorted_with_vote
from corner_case.vote.models import Vote


class TestWinner(TestCase):
    def setUp(self):
        self.restaurant_one = baker.make(Restaurant)
        self.restaurant_two = baker.make(Restaurant)
        self.restaurant_three = baker.make(Restaurant)

        self.menu_one = baker.make(
            Menu, restaurant=self.restaurant_one, date=datetime.date.today()
        )
        self.menu_two = baker.make(
            Menu, restaurant=self.restaurant_two, date=datetime.date.today()
        )
        self.menu_two = baker.make(
            Menu, restaurant=self.restaurant_three, date=datetime.date.today()
        )

        self.vote_one = baker.make(Vote, menu=self.menu_one)
        self.vote_two = baker.make(Vote, menu=self.menu_one)
        self.vote_three = baker.make(Vote, menu=self.menu_two)

        vote_list = Vote.objects.all()
        for vote in vote_list:
            print(vote.__dict__)

    def test_menu_list_ordered_by_vote(self):
        menu_list = get_menu_sorted_with_vote(datetime.date.today())

        for menu in menu_list:
            print(menu.__dict__)

        winner_menu = menu_list[0]

        # winner menu should have two vote
        self.assertEqual(winner_menu.vote_count, 2)

        # winner restaurant should restaurant_one
        self.assertEqual(winner_menu.restaurant_id, self.menu_one.restaurant_id)
