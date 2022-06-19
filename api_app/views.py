from rest_framework.views import APIView

from .pagination import CustomPagination
from .serializers import ProfileSerializer
from .api_connection import data


class ListProfiles(APIView):
    # TODO
    # 1. Install cache as Redis,
    # 2. Add app to docker,
    # 3. Add tests
    # 4. Create a front-end page with Reactjs.

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
