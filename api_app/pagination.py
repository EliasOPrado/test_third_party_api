from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class CustomPagination:
    def __init__(self, list_of_objects: list, limit: str, offset: str, request) -> str:
        self.results = list_of_objects
        self.limit = limit
        self.request = request
        self.offset = offset

    def pagination(self):

        limit = self.request.query_params.get(self.limit, 10)
        offset = self.request.query_params.get(self.offset, 1)

        try:
            paginator = Paginator(self.results, limit)
        except Exception:
            paginator = Paginator(self.results, limit)

        try:
            results = paginator.page(offset)
        except PageNotAnInteger:
            results = paginator.page(offset)
        except EmptyPage:
            results = []

        # pagination metadata:
        api_count = paginator.count

        # get domain + path wothout querystrings.
        domain_and_path = self.request.build_absolute_uri(self.request.path)

        api_next = results.next_page_number() if results.has_next() else None
        api_previous = (
            results.previous_page_number() if results.has_previous() else None
        )

        # created a url link to browse around the pages in the api.
        next_page_link = f"{domain_and_path}?offset={api_next}"
        previous_page_link = (
            f"{domain_and_path}?offset={api_previous}" if api_previous else None
        )

        # SEND TO DATA AND ADD THE RESPONSE IN THE VIEW>...

        return {
            "pageNumber": api_next - 1,
            "pageSize": limit,
            "totalCount": api_count,
            "nextPage": next_page_link,
            "previousPage": previous_page_link,
            "users": list(results),
        }
