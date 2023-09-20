from django.urls import path

from .views import get_csrf_token_view, SignUpView, LoginView, UserInformationView


app_name = 'users'
urlpatterns = [
    path('get-csrf-token/', get_csrf_token_view, name='get-token'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('log-in/', LoginView.as_view(), name='log-in'),
    path('get-user/', UserInformationView.as_view(), name='get-user')
]
