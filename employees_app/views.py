from django.shortcuts import render

from .models import Employee


def employee_overview(request):
    employees = Employee.objects.select_related('department').order_by('name')

    context = {
        'employees': employees,
        'employees_over_3000': employees.filter(salary__gt=3000),
    }

    return render(request, 'employee_list.html', context)