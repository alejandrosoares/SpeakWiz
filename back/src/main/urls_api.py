from django.urls import path, include


urlpatterns = [
    path('topics/', include('topics.urls')),
    path('users/', include('users.urls')),
    path('preferences/', include('preferences.urls')),
    path('favorites/', include('favorites.urls')),
]
