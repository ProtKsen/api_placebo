from rest_framework.generics import ListAPIView

from . import models, serializers


class DepartmentListAPIView(ListAPIView):
    serializer_class = serializers.DepartmentSerializer

    def get_queryset(self):
        return models.Department.objects.all()
