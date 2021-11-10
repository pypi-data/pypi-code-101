import json

INTERNAL_ERROR = 1
TEMPORARILY_UNAVAILABLE = 2
BAD_REQUEST = 4
INVALID_PARAMETER_VALUE = 1000
ENDPOINT_NOT_FOUND = 1001
INVALID_STATE = 1003
PERMISSION_DENIED = 1004
REQUEST_LIMIT_EXCEEDED = 1007
RESOURCE_ALREADY_EXISTS = 3001
RESOURCE_DOES_NOT_EXIST = 3002

ERROR_CODE_TO_HTTP_STATUS = {
    INTERNAL_ERROR: 500,
    INVALID_STATE: 500,
    TEMPORARILY_UNAVAILABLE: 503,
    REQUEST_LIMIT_EXCEEDED: 429,
    ENDPOINT_NOT_FOUND: 404,
    RESOURCE_DOES_NOT_EXIST: 404,
    PERMISSION_DENIED: 403,
    BAD_REQUEST: 400,
    RESOURCE_ALREADY_EXISTS: 400,
    INVALID_PARAMETER_VALUE: 400
}


class OnebrainException(Exception):

    def __init__(self, message, error_code=INTERNAL_ERROR, **kwargs):
        self.error_code = error_code
        self.message = message
        self.json_kwargs = kwargs
        super().__init__(message)

    def serialize_as_json(self):
        exception_dict = {"error_code": self.error_code, "message": self.message}
        exception_dict.update(self.json_kwargs)
        return json.dumps(exception_dict)

    def get_http_status_code(self):
        return ERROR_CODE_TO_HTTP_STATUS.get(self.error_code, 500)


class RestException(OnebrainException):

    def __init__(self, json):
        error_code = json.get("error_code", INTERNAL_ERROR)
        message = "%s: %s" % (
            error_code,
            json["message"] if "message" in json else "Response: " + str(json),
        )
        super().__init__(message, error_code=error_code)
        self.json = json