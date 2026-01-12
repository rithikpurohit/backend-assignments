from django.urls import path
from .views import UserListView, UserDetailView, UserHealthStatusView

urlpatterns = [
    path("", UserListView.as_view()),
    path("<int:pk>/", UserDetailView.as_view()),
    path("<int:pk>/health/", UserHealthStatusView.as_view()),
]
