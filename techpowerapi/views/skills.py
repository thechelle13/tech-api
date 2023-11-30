from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from techpowerapi.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "label"]


class SkillViewSet(viewsets.ViewSet):
    def list(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            skill = Skill.objects.get(pk=pk)
            serializer = SkillSerializer(skill)
            return Response(serializer.data)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        # Get the data from the client's JSON payload
        label = request.data.get("label")

        # Create a comment database row first, so you have a
        # primary key to work with
        skill = Skill.objects.create(
            # maybe issues with label /  request.user
            label=label
        )

        serializer = SkillSerializer(skill, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            skill = Skill.objects.get(pk=pk)

            # Is the authenticated user allowed to edit this tag?
            self.check_object_permissions(request, skill)

            serializer = SkillSerializer(data=request.data)
            if serializer.is_valid():
                skill.label = serializer.validated_data["label"]
                # tag.created_on = serializer.validated_data["created_on"]
                skill.save()

                serializer = SkillSerializer(skill, context={"request": request})
                return Response(None, status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        except skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            skill = Skill.objects.get(pk=pk)
            self.check_object_permissions(request, skill)
            skill.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)