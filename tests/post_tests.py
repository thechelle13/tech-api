# import json
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from techpowerapi.models import TechUser

# class PostTests(APITestCase):

#     fixtures = ['user', 'token','tech_user', 'posts', 'skills']

#     def setUp(self):
#         self.user = User.objects.first()
#         self.tech_user = TechUser.objects.get(user=self.user)
#         token = Token.objects.get(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")


#     def test_create_posts(self):
#         url = "/posts"

#         data = {
           
           
#             "title": "New Test Post",
#             "publication_date": "2023-03-01",
#             "image_url": "http://www.testimage.jpeg",
#             "content": "Here is the content for test post",
#             "affliate": "Company or Cohort",
#             "approved": True,
#             "skills": [2, 3],
#             "area": 1,
#         }

#         response = self.client.post(url, data, format='json')

#         json_response = json.loads(response.content)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         self.assertEqual(json_response["tech_user"]["user"]["id"], self.user.id)
#         self.assertEqual(json_response["title"], "New Test Post")
#         self.assertEqual(json_response["image_url"], "http://www.testimage.jpeg")
#         self.assertEqual(json_response["affliate"], "Company or Cohort")
#         self.assertEqual(json_response["content"], "Here is the content for test post")
#         self.assertEqual(json_response["approved"], True)
#         self.assertEqual(json_response["skills"], [{'id': 2, 'label': 'Python'}, {'id': 3, 'label': 'React'}])
        

#     def test_get_all_posts(self):
#         response = self.client.get("/posts")

#         json_response = json.loads(response.content)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         self.assertEqual(json_response[0]["title"], "Post Title 1")
#         # self.assertEqual(json_response[1]["title"], "Post Title 2")
#         # self.assertEqual(json_response[2]["title"], "Post Title 3")
