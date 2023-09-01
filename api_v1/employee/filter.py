import django_filters
from api_v1.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    surname = django_filters.CharFilter(lookup_expr='icontains', label='Фамилия')
    department_id = django_filters.NumberFilter(label='ID департамента')

    class Meta:
        model = Employee
        fields = ['surname', 'department_id']
