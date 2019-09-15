from django.urls import path

from users.views import (
    CreateUserView,
    ProfileView
)


urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
