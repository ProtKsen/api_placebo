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
    positions = serializers.ListSerializer(child=PositionSerializer())

    class Meta:
        model = models.Employee
        fields = "__all__"


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        exclude = ["position"]


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    position_id = serializers.IntegerField()

    class Meta:
        model = models.Employee
        exclude = ["position"]
