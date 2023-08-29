from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import EmployeeSerializer
from .models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('initials')
    serializer_class = EmployeeSerializer

