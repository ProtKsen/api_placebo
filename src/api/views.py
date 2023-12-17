from django.http.response import JsonResponse
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Department
from .serializers import DepartmentSerializer


class DeaprtmentAPIView(generics.ListAPIView, APIView):
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

    def get(self, request, pk):
        department = Department.objects.filter(pk=pk).first()
        if department:
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        department = Department.objects.filter(pk=pk).first()
        if department:
            data = DepartmentSerializer(data=request.data)
            if data.is_valid():
                data.update()
                return Response(data.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        department = Department.objects.filter(pk=pk).first()
        if department:
            department.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
