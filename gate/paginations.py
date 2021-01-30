from rest_framework.pagination import PageNumberPagination

class UserPagination(PageNumberPagination):
    page_size = 5 # default page size
    page_size_query_param = 'limit'  # ?page=:page&limit=:limit
    max_page_size = 9 # max page siz

class UserLogPagination(PageNumberPagination):
    page_size = 10 # default page size