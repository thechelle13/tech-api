import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from techpowerapi.models import Skill

class SkillTests(APITestCase):

    fixtures = ['skills', 'user', 'token']

    def setUp(self):
        self.user = User.objects.first()
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_tag(self):
        url = "/skills"

        data = {
            "label": "JavaScript"
        }

        response = self.client.post(url, data, format='json')

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json_response["label"], "JavaScript")
        self.assertEqual(json_response["id"], 4)

    def test_get_skill(self):
        skill = Skill()
        skill.label = "GitHub"
        skill.save()

        response = self.client.get(f"/tags/{skill.id}")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(json_response["label"], "GitHub")
        self.assertEqual(json_response["id"], skill.id)
        
    def test_get_tags(self):
        response = self.client.get("/tags")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code,status.HTTP_200_OK)

        self.assertEqual(json_response[0]["label"], "Funny")
        self.assertEqual(json_response[1]["label"], "Sad")

    def test_change_tag(self):
        tag = Skill()
        tag.label = "Hilarious"
        tag.save()

        data = {
            "label": "Not Hilarious"
        }
        response = self.client.put(f"/tags/{tag.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f"/tags/{tag.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["label"], "Not Hilarious")

    def test_delete_tag(self):
        tag = Skill()
        tag.label = "Hilarious"
        tag.save()
        
        response = self.client.delete(f"/tags/{tag.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f"/tags/{tag.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)