from django.urls import path

from .views import CardListView, CardDetailView


app_name = 'cards'
urlpatterns = [
    path('', CardListView.as_view(), name='list'),
    path('<int:card_pk>/', CardDetailView.as_view(), name='detail'),
]
