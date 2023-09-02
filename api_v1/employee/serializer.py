from rest_framework import serializers, status
from datetime import date
from rest_framework.response import Response

from api_v1.models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    photo = serializers.URLField()
    department_id = serializers.IntegerField(write_only=True)
    birthday = serializers.DateField(write_only=True)
    surname = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['full_name', 'photo', 'position', 'salary', 'age', 'department_name', 'department_id', 'birthday',
                  'surname',
                  'first_name', 'last_name']

    @staticmethod
    def get_full_name(obj):
        return f"{obj.surname} {obj.first_name} {obj.last_name}"

    @staticmethod
    def get_age(obj):
        today = date.today()
        age = today.year - obj.birthday.year - ((today.month, today.day) < (obj.birthday.month, obj.birthday.day))
        return age

    @staticmethod
    def get_department_name(obj):
        return obj.department.name

    def create(self, validated_data):
        department_id = validated_data.pop('department_id')
        try:
            department = Department.objects.get(pk=department_id)
        except Department.DoesNotExist:
            return Response({"detail": "Department does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        employee = Employee.objects.create(**validated_data)
        employee.department = department
        employee.save()
        return employee
