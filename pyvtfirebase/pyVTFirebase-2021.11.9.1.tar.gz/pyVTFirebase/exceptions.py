import json
from httpx import Response
from httpx import HTTPStatusError, RequestError


def check_response(response: Response):
    try:
        response.raise_for_status()
    except HTTPStatusError as exc:
        raise HTTPStatusError(
            message=f'Error response {exc.response.status_code} while requesting {exc.request.url!r}.\n'
                    f'Returned Response:\n'
                    f'{json.dumps(exc.response.json(), indent=4, sort_keys=True)}',
            request=exc.request, response=exc.response)
    except RequestError as exc:
        raise RequestError(message=f'An error occurred while requesting {exc.request.url!r}.')
