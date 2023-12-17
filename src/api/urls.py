from django.urls import path

from . import views

urlpatterns = [
    path("departments", views.DeaprtmentAPIView.as_view(), name="departments"),
    path(
        "departments/<int:pk>/", views.DepartmentDetailAPIView.as_view(), name="department_details"
    ),
]
