from rest_framework import serializers
from datetime import date
from .models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class EmployeeSerializer(serializers.ModelSerializer):
    departament = DepartmentSerializer()
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    photo = serializers.URLField()

    class Meta:
        model = Employee
        fields = '__all__'

    @staticmethod
    def get_full_name(obj):
        return f"{obj.surname} {obj.first_name} {obj.last_name}"

    @staticmethod
    def get_age(obj):
        today = date.today()
        age = today.year - obj.birthday.year - ((today.month, today.day) < (obj.birthday.month, obj.birthday.day))
        return age

    def create(self, validated_data):
        departament_data = validated_data.pop('departament')
        employee = Employee.objects.create(departament=Department.objects.create(**departament_data), **validated_data)
        return employee
