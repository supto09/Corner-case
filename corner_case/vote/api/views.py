import datetime

from django.db.models import Count
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from corner_case.restaurant.api.serializers import MenuSerializer
from corner_case.restaurant.models import Menu, Restaurant
from corner_case.vote.api.serializers import VoteCreateSerializer
from corner_case.vote.models import Vote


def get_menu_sorted_with_vote(date):
    """
    This method returns the list of menu For a given day, sorted based on the vote
    and in case two men have equal vote, Menu that was created earlier will be prioritized
    """
    return Menu.objects.filter(date=date).annotate(
        vote_count=Count('vote')
    ).order_by('-vote_count', 'created_at')


@extend_schema_view(
    post=extend_schema(summary="Vote for menu"),
)
class VoteCreateApiView(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = VoteCreateSerializer
    queryset = Vote.objects.all()


@extend_schema_view(
    get=extend_schema(summary="Select winner"),
)
class WinnerRetrieveApiView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MenuSerializer

    def get_object(self):
        today = datetime.date.today()

        yesterday_winner = get_menu_sorted_with_vote(today + datetime.timedelta(days=-1)).first()
        day_before_yesterday_winner = get_menu_sorted_with_vote(today + datetime.timedelta(days=-2)).first()

        today_menu_list = get_menu_sorted_with_vote(today)

        print("Today menu", today_menu_list.first())
        print("Yesterday menu", yesterday_winner)
        print("Day Before yesterday menu", day_before_yesterday_winner)

        # if either of the previous two day is none then current best is the winner
        if yesterday_winner is None or day_before_yesterday_winner is None:
            print("One of previous is none")
            return today_menu_list[0]

        # if both previous day has winner then check if they are same as today's winner
        # if all three are same then
        if yesterday_winner.restaurant_id == day_before_yesterday_winner.restaurant_id and day_before_yesterday_winner.restaurant_id == today_menu_list.first().restaurant_id:
            print("All three are same so return the next")
            return today_menu_list[1]

        return today_menu_list[0]
