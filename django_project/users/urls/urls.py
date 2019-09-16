from django.urls import path

from users.views import (
    CreateUserView,
    LoginView,
    ProfileView
)


urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
