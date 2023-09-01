from rest_framework import serializers, status
from django.db import models

from ..models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    employees_num = serializers.SerializerMethodField()
    amount_department = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = '__all__'

    @staticmethod
    def get_employees_num(obj):
        return Employee.objects.filter(department=obj).count()

    @staticmethod
    def get_amount_department(obj):
        total_salary = Employee.objects.filter(department=obj).aggregate(total_salary=models.Sum('salary'))[
            'total_salary']
        return total_salary