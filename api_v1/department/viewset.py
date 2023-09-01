from rest_framework import viewsets, filters, status

from .serializer import DepartmentSerializer
from api_v1.models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
