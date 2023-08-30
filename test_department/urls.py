from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from api_v1.views import EmployeeViewSet, DepartmentViewSet

router = routers.SimpleRouter()
router.register(f'employees', EmployeeViewSet, basename='employee')
# router.register(f'users/add', UserAddView)
# router.register(f'users/delete', UserDeleteView)
router.register(f'departments', DepartmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
