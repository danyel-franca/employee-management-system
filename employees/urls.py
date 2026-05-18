from django.urls import path

from .views import (
    home,
    delete_employee,
    update_employee
)

urlpatterns = [

    path('', home, name='home'),

    path(
        'delete/<int:id>/',
        delete_employee,
        name='delete_employee'
    ),

    path(
        'update/<int:id>/',
        update_employee,
        name='update_employee'
    ),
]