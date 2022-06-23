from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class TestUsersAPI(APITestCase):
    def setUp(self):
        self.client = APIClient()
        user = User(
            username="admin",
            password="@adr153",
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )
        user.save()

        self.token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.response = self.client.get(reverse("profiles_api:api"), format="json")

    def test_profile_endpoint(self):
        # test if endpoint is returning what is needed.
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_if_initial_endpoint_page_is_none(self):
        self.assertEqual(self.response.data["previousPage"], None)

    def test_if_users_is_a_list(self):
        self.assertEqual(type(self.response.data["users"]), list)

    def test_if_endpont_has_page_number(self):
        self.assertTrue(self.response.data["pageNumber"])

    def test_if_endpont_has_page_size(self):
        self.assertTrue(self.response.data["pageSize"])

    def test_if_endpont_has_total_count(self):
        self.assertTrue(self.response.data["totalCount"])
