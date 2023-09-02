from rest_framework.pagination import PageNumberPagination


class PaginationEmployees(PageNumberPagination):
    page_size = 5
