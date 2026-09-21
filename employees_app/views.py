from django.db.models import Avg
from django.shortcuts import render

from .models import Employee


def employee_overview(request):
    employees = Employee.objects.select_related('department').order_by('name')

    context = {
        'employees': employees,
        'employees_over_3000': employees.filter(salary__gt=3000),
                'employees_at_least_5000_count': employees.filter(
            salary__gte=5000
        ).count(),
                'sales_average_salary': employees.filter(
            department__name='Sales'
        ).aggregate(
            average_salary=Avg('salary')
        )['average_salary'],
    }

    return render(request, 'employee_list.html', context)