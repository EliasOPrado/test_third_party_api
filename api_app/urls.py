from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("", views.ListProfiles.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
