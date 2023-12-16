from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=100)
    chief_department = models.ForeignKey(
        "Department", on_delete=models.DO_NOTHING, blank=True, null=True
    )


class Position(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    ADMIN, MODERATOR, USER = 10, 20, 30
    permission_choices = [("administrator", ADMIN), ("moderator", MODERATOR), ("user", USER)]
    permission = models.PositiveIntegerField(choices=permission_choices, default=USER)

    class Meta:
        unique_together = (
            "title",
            "department",
        )


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.ManyToManyField(Position)
