from rest_framework import routers
from .views import EmployeeViewSet

router = routers.SimpleRouter()
router.register(f'employees', EmployeeViewSet, basename='employee_view')
# router.register(f'users/add', UserAddView)
# router.register(f'users/delete', UserDeleteView)
# router.register(f'departments', DepartmentListView)


urlpatterns = router.urls
