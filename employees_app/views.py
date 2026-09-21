from django.shortcuts import render

from .models import Employee


def employee_overview(request):
    employees = Employee.objects.select_related('department').order_by('name')

    context = {
        'employees': employees,
    }

    return render(request, 'employee_list.html', context)