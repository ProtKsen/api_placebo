from rest_framework import serializers

from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = (
            "pk",
            "title",
            "chief_department",
        )


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
