from django.urls import path, include


from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
 

urlpatterns = [
    path('topics/', include('topics.urls')),
    path('users/', include('users.urls')),
    path('preferences/', include('preferences.urls')),
    path('favorites/', include('favorites.urls')),
]


urlpatterns += [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]