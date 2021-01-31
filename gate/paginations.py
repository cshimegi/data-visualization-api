from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

class GateBasePagination(PageNumberPagination):
    def get_paginated_response(self, data):
        ''' @override

        '''
        next_page_number = self.page.next_page_number() if self.page.has_next() else None
        previous_page_number = self.page.previous_page_number() if self.page.has_previous() else None

        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', next_page_number),
            ('previous', previous_page_number),
            ('results', data)
        ]))

class UserPagination(GateBasePagination):
    page_size = 5 # default page size
    page_size_query_param = 'limit'  # ?page=:page&limit=:limit
    max_page_size = 9 # max page siz

class UserLogPagination(GateBasePagination):
    page_size = 9 # default page size