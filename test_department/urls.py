from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from api_v1.department.viewset import DepartmentViewSet
from api_v1.employee.viewset import EmployeeViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = routers.SimpleRouter()
router.register(f'employees', EmployeeViewSet, basename='employee')
router.register(f'departments', DepartmentViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API Структура компании",
        default_version='v1',
        description="REST API ",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # В режиме разработки можно использовать AllowAny, но в production это стоит изменить.
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


