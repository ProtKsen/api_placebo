from django.urls import path

from . import views

urlpatterns = [
    path("departments", views.DepartmentListAPIView.as_view(), name="departments"),
]
