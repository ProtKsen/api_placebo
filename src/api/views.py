from django.forms.models import model_to_dict
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Department, Employee, Position
from .serializers import (DepartmentSerializer, EmployeeCreateSerializer,
                          EmployeeSerializer, EmployeeUpdateSerializer,
                          PositionCreateSerializer, PositionSerializer)


class DepartmentAPIView(generics.ListAPIView, APIView):
    serializer_class = DepartmentSerializer
    model = Department
    queryset = Department.objects.all()

    def post(self, request):
        data = DepartmentSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetailAPIView(generics.ListAPIView, APIView):
    serializer_class = DepartmentSerializer

    def get(self, request, department_id):
        department = Department.objects.filter(id=department_id).first()
        if department:
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, department_id):
        department = Department.objects.filter(id=department_id).first()
        if department:
            data = DepartmentSerializer(data=request.data)
            if data.is_valid():
                data.update(instance=department, validated_data=request.data)
                return Response(data.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, department_id):
        department = Department.objects.filter(id=department_id).first()
        if department:
            department.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class PositionListAPIView(generics.ListAPIView, APIView):
    model = Position

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return PositionCreateSerializer
        return PositionSerializer

    def get_queryset(self):
        department_id = self.kwargs["department_id"]
        if Department.objects.filter(id=department_id).exists():
            return Position.objects.select_related("department").filter(
                department__id=department_id
            )
        raise NotFound

    def post(self, request, department_id):
        department_id = self.kwargs["department_id"]
        department = Department.objects.filter(id=department_id).first()
        if department:
            data = PositionCreateSerializer(data=request.data)
            if data.is_valid():
                position = Position.objects.create(**data.data, department=department)
                position.save()
                return Response(model_to_dict(position), status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)


class PositionDetailAPIView(generics.ListAPIView, APIView):
    serializer_class = PositionCreateSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "PUT":
            return PositionCreateSerializer
        return PositionSerializer

    def get(self, request, department_id, position_id):
        department = Department.objects.filter(id=department_id).first()
        if department:
            position = Position.objects.filter(id=position_id, department=department).first()
            if position:
                serializer = PositionSerializer(position)
                return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, department_id, position_id):
        department = Department.objects.filter(id=department_id).first()
        if department:
            position = Position.objects.filter(id=position_id, department=department).first()
            if position:
                data = PositionCreateSerializer(data=request.data)
                if data.is_valid():
                    for attr, value in data.data.items():
                        setattr(position, attr, value)
                    position.department = department
                    position.save()
                    return Response(model_to_dict(position), status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, department_id, position_id):
        department = Department.objects.filter(id=department_id).first()
        if department:
            position = Position.objects.filter(id=position_id, department=department).first()
            if position:
                position.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class EmployeesListApiView(generics.ListAPIView, APIView):
    model = Employee
    queryset = Employee.objects.prefetch_related("position", "position__department").all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return EmployeeCreateSerializer
        return EmployeeSerializer

    def post(self, request):
        data = EmployeeCreateSerializer(data=request.data)
        if data.is_valid():
            employee, created = Employee.objects.get_or_create(**data.data)
            if created:
                return Response(model_to_dict(employee), status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailAPIView(generics.ListAPIView, APIView):
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "PUT":
            return EmployeeUpdateSerializer
        return EmployeeSerializer

    def get(self, request, employee_id):
        employee = Employee.objects.filter(id=employee_id).first()
        if employee:
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, employee_id):
        employee = Employee.objects.filter(id=employee_id).first()
        if employee:
            data = EmployeeUpdateSerializer(data=request.data)
            if data.is_valid():
                for attr, value in data.data.items():
                    setattr(employee, attr, value)
                position = Position.objects.filter(id=data.data["position_id"]).first()
                if position:
                    employee.position.add(position)
                employee.save()
                return Response(model_to_dict(position), status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, employee_id):
        employee = Employee.objects.filter(id=employee_id).first()
        if employee:
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
