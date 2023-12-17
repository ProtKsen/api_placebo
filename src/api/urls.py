from django.urls import path

from . import views

urlpatterns = [
    path("departments", views.DepartmentAPIView.as_view(), name="departments"),
    path(
        "departments/<int:department_id>/",
        views.DepartmentDetailAPIView.as_view(),
        name="department_details",
    ),
    path(
        "departments/<int:department_id>/positions",
        views.PositionListAPIView.as_view(),
        name="positions",
    ),
    path(
        "departments/<int:department_id>/positions/<int:position_id>/",
        views.PositionDetailAPIView.as_view(),
        name="position_details",
    ),
    path(
        "employees",
        views.EmployeesListApiView.as_view(),
        name="employees",
    ),
    path(
        "employees/<int:employee_id>/",
        views.EmployeeDetailAPIView.as_view(),
        name="employee_details",
    ),
]
