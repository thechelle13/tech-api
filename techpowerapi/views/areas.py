from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from techpowerapi.models import Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ["id", "label"]


class AreaViewSet(viewsets.ViewSet):
    def list(self, request):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            area = Area.objects.get(pk=pk)
            serializer = AreaSerializer(area)
            return Response(serializer.data)
        except Area.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    

  