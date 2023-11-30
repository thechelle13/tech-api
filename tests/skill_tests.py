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

    def test_create_skill(self):
        url = "/skills"

        data = {
            "label": "Git Bash"
        }

        response = self.client.post(url, data, format='json')

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json_response["label"], "Git Bash")
        self.assertEqual(json_response["id"], 12)

    def test_get_skill(self):
        skill = Skill()
        skill.label = "GitHub"
        skill.save()

        response = self.client.get(f"/skills/{skill.id}")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(json_response["label"], "GitHub")
        self.assertEqual(json_response["id"], skill.id)
        
    def test_get_skills(self):
        response = self.client.get("/skills")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code,status.HTTP_200_OK)

        self.assertEqual(json_response[0]["label"], "React")
        self.assertEqual(json_response[1]["label"], "Django")

    

    def test_delete_skill(self):
        skill = Skill()
        skill.label = "AWS"
        skill.save()
        
        response = self.client.delete(f"/skills/{skill.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f"/skills/{skill.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)