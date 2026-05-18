from django.shortcuts import render, redirect

from .models import Employee
from .forms import EmployeeForm


def home(request):

    employees = Employee.objects.all()

    form = EmployeeForm()

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

    context = {
        'employees': employees,
        'form': form
    }

    return render(request, 'employees/home.html', context)

def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('home')

def update_employee(request, id):

    employee = Employee.objects.get(id=id)

    form = EmployeeForm(instance=employee)

    if request.method == 'POST':

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():

            form.save()

            return redirect('home')

    context = {
        'form': form
    }

    return render(
        request,
        'employees/update.html',
        context
    )