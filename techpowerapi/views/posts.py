from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from techpowerapi.models import Post, TechUser
from django.contrib.auth.models import User
from .skills import SkillSerializer
from .users import TechUserSerializer




class SimplePostSerializer(serializers.ModelSerializer):
    
    
    # is_owner = serializers.SerializerMethodField()

    # def get_is_owner(self, obj):
    #     # Check if the authenticated user is the owner
    #     return self.context["request"].user == obj.tech_user.user

    class Meta:
        model = Post
        fields = [
            "skills",
            "title",
            "tech_user",
            "content",
            "approved",
            "area",
            # "is_owner",
        ]


class PostSerializer(serializers.ModelSerializer):
    tech_user = TechUserSerializer(many=False)
    is_owner = serializers.SerializerMethodField()
    skills = SkillSerializer(many=True)
   

    def get_is_owner(self, obj):
        # Check if the authenticated user is the owner
        return self.context["request"].user == obj.tech_user.user

    class Meta:
        model = Post
        fields = [
            "id",
            "tech_user",
            "title",
            "publication_date",
            "content",
            "approved",
            "area",
            "skills",
            "is_owner",
        ]


class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, context={"request": request})
            return Response(serializer.data)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        # Get the data from the client's JSON payload
        tech_user = TechUser.objects.get(user=request.auth.user)
       
        title = request.data.get("title")
        publication_date = request.data.get("publication_date")
        # image_url = request.data.get("image_url")
        content = request.data.get("content")
        approved = request.data.get("approved")
        area = request.data.get("area")

        # Create a post database row first, so you have a
        # primary key to work with
        post = Post.objects.create(
            tech_user=tech_user,
          
            title=title,
            publication_date=publication_date,
            # image_url=image_url,
            content=content,
            approved=approved,
            area=area,
        )

        # Establish the many-to-many relationships
        skill_ids = request.data.get("skills", [])
        post.skills.set(skill_ids)

        serializer = PostSerializer(post, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)

            # Is the authenticated user allowed to edit this post?
            self.check_object_permissions(request, post)

            serializer = SimplePostSerializer(data=request.data)
            if serializer.is_valid():
                # post.tech_user = serializer.validated_data["tech_user"]
                
                post.title = serializer.validated_data["title"]
                # post.publication_date = serializer.validated_data["publication_date"]
                # post.image_url = serializer.validated_data["image_url"]
                post.content = serializer.validated_data["content"]
                post.approved = serializer.validated_data["approved"]
                post.approved = serializer.validated_data["area"]
                post.save()

                skill_ids = request.data.get("skills", [])
                post.skills.set(skill_ids)

                serializer = PostSerializer(post, context={"request": request})
                return Response(None, status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(request, post)
            post.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
