import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from techpowerapi.models import Area

class AreaTests(APITestCase):

    fixtures = ['areas', 'user', 'token']

    def setUp(self):
        self.user = User.objects.first()
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        
    def test_get_areas(self):
        response = self.client.get("/areas")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code,status.HTTP_200_OK)

        self.assertEqual(json_response[0]["label"], "Data")
        self.assertEqual(json_response[1]["label"], "WebDev")