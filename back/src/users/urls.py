from django.urls import path

from .views import SignUpView, LoginView, UserProfileView


app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='log-in'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
