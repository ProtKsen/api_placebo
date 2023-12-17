from rest_framework import serializers

from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = models.Position
        fields = "__all__"


class PositionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        exclude = ["department"]


class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = models.Employee
        fields = "__all__"
