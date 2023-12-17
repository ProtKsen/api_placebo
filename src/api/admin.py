from django.contrib import admin

from api import models

admin.site.register(models.Department)
admin.site.register(models.Position)
admin.site.register(models.Employee)
