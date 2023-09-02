from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .serializer import EmployeeSerializer
from .filter import EmployeeFilter
from .service import PaginationEmployees
from api_v1.models import Employee, Department


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('surname')
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter
    pagination_class = PaginationEmployees

    def create(self, request, *args, **kwargs):
        department_id = request.data.get('department_id')
        try:
            department = Department.objects.get(pk=department_id)
        except Department.DoesNotExist:
            return Response({"detail": "Department does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(department=department)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
