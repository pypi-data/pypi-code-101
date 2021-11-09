from . import StatusCode

from . import StatusCode

# General
successful_request = StatusCode(200, 'Successful Request')
bad_request = StatusCode(400, 'Bad Request')
unauthorized_request = StatusCode(401, 'Unauthorized Request')
forbidden_request = StatusCode(403, 'Forbidden Request')
resource_not_found = StatusCode(404, 'The required resource is not found')
request_args_validation_error = StatusCode(422, 'Request arguments (query string or body) validation error')

# JWT
expired_token = StatusCode(432, 'The token is expired')
logged_out = StatusCode(433, 'You have logged out. Please log in again (Expired Session)')
wrong_token = StatusCode(434, 'Wrong token error (related to refresh and access tokens)')

# Account
account_deleted = StatusCode(435, 'Your account has been deleted')
inactive_account = StatusCode(436, 'Your account is inactive')

# Database
duplicate_entry = StatusCode(600, 'This record already exists')
related_existing_record = StatusCode(601, 'This record is related to other records. Therefore, it cannot be deleted')

