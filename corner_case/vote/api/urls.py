from django.urls import path

from corner_case.vote.api.views import VoteCreateApiView, WinnerRetrieveApiView

app_name = "votes"
urlpatterns = [
    path('/create', VoteCreateApiView.as_view()),
    path('/winner', WinnerRetrieveApiView.as_view()),
]
