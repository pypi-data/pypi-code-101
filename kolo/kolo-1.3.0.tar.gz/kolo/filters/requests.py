import json
import logging
import types
from typing import Dict, List, Optional, TYPE_CHECKING

from django.utils import timezone

from ..serialize import decode_header_value


logger = logging.getLogger("kolo")


if TYPE_CHECKING:
    # TypedDict only exists on python 3.8+
    # We run mypy using a high enough version, so this is ok!
    from typing import TypedDict

    class ApiRequest(TypedDict):
        method: str
        url: str
        method_and_full_url: str
        body: Optional[str]
        headers: Dict[str, str]
        timestamp: str

    class ApiResponse(TypedDict):
        timestamp: str
        body: str
        status_code: int
        headers: Dict[str, str]

    class ApiInfo(TypedDict, total=False):
        request: ApiRequest
        response: ApiResponse


class ApiRequestFilter:
    use_frames_of_interest = True

    def __init__(self) -> None:
        self.data: Dict[str, List[ApiInfo]] = {"api_requests_made": []}

    def __call__(self, frame: types.FrameType, event: str, arg: object) -> bool:
        return self.match_request(frame) or self.match_response(frame)

    def process(
        self,
        frame: types.FrameType,
        event: str,
        arg: object,
        call_frame_ids: List[Dict[str, str]],
    ):
        if event == "call" and self.match_request(frame):
            self.process_api_request_made(frame)
        elif event == "return" and self.match_response(frame):
            self.process_api_response(frame)

    def match_request(self, frame: types.FrameType) -> bool:
        filepath = frame.f_code.co_filename
        callable_name = frame.f_code.co_name
        return "urllib3/connectionpool" in filepath and callable_name == "urlopen"

    def match_response(self, frame: types.FrameType) -> bool:
        filepath = frame.f_code.co_filename
        callable_name = frame.f_code.co_name
        return "requests/sessions" in filepath and "request" == callable_name

    def process_api_request_made(self, frame: types.FrameType):
        frame_locals = frame.f_locals

        scheme = frame_locals["self"].scheme
        host = frame_locals["self"].host
        url = frame_locals["url"]
        full_url = f"{scheme}://{host}{url}"

        request_headers = {
            key: decode_header_value(value)
            for key, value in frame_locals["headers"].items()
        }

        request_body = frame_locals["body"]

        try:
            json.dumps(request_body)
        except TypeError:
            if isinstance(request_body, bytes):
                body = request_body.decode("utf-8")
            else:
                body = (
                    f"Error: Could not parse request body. Type: {type(request_body)}"
                )
        else:
            body = request_body

        method = frame_locals["method"].upper()
        method_and_full_url = f"{method} {full_url}"

        api_request: ApiInfo = {
            "request": {
                "method": method,
                "url": full_url,
                "method_and_full_url": method_and_full_url,
                "body": body,
                "headers": request_headers,
                "timestamp": timezone.now().isoformat(),
            }
        }

        self.data["api_requests_made"].append(api_request)

    def process_api_response(self, frame: types.FrameType):
        frame_locals = frame.f_locals

        method = frame_locals["method"].upper()
        url = frame_locals["prep"].url
        method_and_full_url = f"{method} {url}"

        relevant_api_request = None
        negative_target_index = None

        api_requests_made = self.data["api_requests_made"]
        for index, api_request in enumerate(reversed(api_requests_made), start=1):
            if method_and_full_url == api_request["request"]["method_and_full_url"]:
                if "response" not in api_request:
                    relevant_api_request = api_request
                    negative_target_index = index

        if relevant_api_request is not None:
            response = frame_locals["resp"]

            relevant_api_request["response"] = {
                "timestamp": timezone.now().isoformat(),
                "body": response.text,
                "status_code": response.status_code,
                "headers": dict(response.headers),
            }

            assert negative_target_index is not None
            api_requests_made[-negative_target_index] = relevant_api_request
        else:
            logger.debug(f"No matching request found for {method_and_full_url}")
