from django.urls import path, include

from .views import TopicListView, TopicDetailView


app_name = 'topic'
urlpatterns = [
    path('', TopicListView.as_view(), name='list'),
    path('<int:pk>/', TopicDetailView.as_view(), name='detail'),
]
