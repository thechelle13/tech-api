from django.db import models
from .area import Area



class Post(models.Model):
    """Database model for tracking events"""

    tech_user = models.ForeignKey("TechUser", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200)
    publication_date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=200)
    approved = models.BooleanField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="posts")
    skills = models.ManyToManyField("Skill", through="PostSkill", related_name="posts")