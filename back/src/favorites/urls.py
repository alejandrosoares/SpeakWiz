from django.urls import path

from .views import UserFavoriteView, UserFavoriteResourceListView


app_name = 'favorites'
urlpatterns = [
    path(
        '',
        UserFavoriteView.as_view(),
        name='user-favorites'),
    path(
        'resources/',
        UserFavoriteResourceListView.as_view(),
        name='user-favorites-resource'),
]
