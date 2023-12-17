from django.urls import path

from . import views

urlpatterns = [
    path("departments", views.DepartmentAPIView.as_view(), name="departments"),
    path(
        "departments/<int:pk>/", views.DepartmentDetailAPIView.as_view(), name="department_details"
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
]
