from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'profiles_api'

urlpatterns = [
    path("", views.ListProfiles.as_view(), name='api'),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
