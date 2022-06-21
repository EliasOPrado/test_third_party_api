from rest_framework.views import APIView

from .pagination import CustomPagination
from .serializers import ProfileSerializer
from .api_connection import data


class ListProfiles(APIView):
    # TODO
    # 1. Add tests coverage,
    # 2. Add authentication,
    # 2. Add app to docker,
    # 3. Install cache as Redis,
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


        from .geolocation import SPECIAL_2, SPECIAL_1, NORMAL

        new_special = {}

        for key, value in SPECIAL_1.items():
            for key2, value2 in SPECIAL_2.items():
                if key == 'minlon' and key2 == 'minlon':
                    if key > key2:
                        print("I am HERE...", {key: value} )

        


        return CustomPagination(results, "limit", "offset", request).pagination()
