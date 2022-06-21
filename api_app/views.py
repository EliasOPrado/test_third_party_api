from rest_framework.views import APIView

from .pagination import CustomPagination
from .serializers import ProfileSerializer
from .api_connection import data

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

class ListProfiles(APIView):
    # TODO
    # 1. Add tests coverage,
    # 2. Add authentication,
    # 4. Create a front-end page with Reactjs.

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        for dictionaries in data.values():
            dicts = list(dictionaries)

        serializer = ProfileSerializer(data=dicts, many=True)
        serializer.is_valid()
        results = serializer.data

    
        return CustomPagination(results, "limit", "offset", request).pagination()
