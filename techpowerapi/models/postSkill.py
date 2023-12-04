from django.db import models



class PostSkill(models.Model):
    """Database model for tracking events"""

    skill = models.ForeignKey("Skill", on_delete=models.CASCADE, related_name="post_skills")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_skills" )