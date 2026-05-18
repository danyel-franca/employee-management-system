from django.contrib import admin

from .models import Company, Position, Employee


admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Employee)