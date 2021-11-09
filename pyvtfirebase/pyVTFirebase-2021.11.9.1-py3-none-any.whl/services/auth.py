import httpx

from pyVTFirebase.exceptions import check_response
from pyVTFirebase.services.helpers import build_url, build_params


class Auth:
    """ Authentication and User Management Service """

    def __init__(self, api_key: str, client: httpx.Client):
        self.api_key = api_key
        self.client = client
        self.base_url = 'https://identitytoolkit.googleapis.com/v1/accounts'
        self.header = {"Content-Type": "application/json; charset=UTF-8"}

    def exchange_custom_for_ID_and_refresh_token(self, token: str) -> httpx.Response:
        """
        Exchanges a custom Auth token for an ID and refresh token

        :param token: A Firebase Auth custom token
        :return: Request response from the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="signInWithCustomToken")
        params = build_params(key=self.api_key)
        data = {'token': token, 'returnSecureToken': True}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def exchange_refresh_token_for_ID_token(self, refresh_token: str) -> httpx.Response:
        """
        Refreshes a Firebase Auth ID token

        :param refresh_token: A Firebase Auth refresh token
        :return: Request response from the Firebase REST API

        Common Error Codes:
            . TOKEN_EXPIRED: The user's credential is no longer valid. The user must sign in again.
            . USER_DISABLED: The user account has been disabled by an administrator.
            . USER_NOT_FOUND: The user corresponding to the refresh token was not found. It is likely the user
                              was deleted.
            . API key not valid: The provided API key is invalid
            . INVALID_REFRESH_TOKEN: An invalid refresh token is provided.
            . Invalid JSON payload received. Unknown name "refresh_tokens": cannot bind query parameter.
                    Field "refresh_tokens" could not be found in request message.
            . INVALID_GRANT_TYPE: The grant type specified is invalid.
            . MISSING_REFRESH_TOKEN: No refresh toke provided.
        """

        url = 'https://securetoken.googleapis.com/v1/token'
        params = build_params(key=self.api_key)
        data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def signUp_with_email_and_password(self, email: str, password: str) -> httpx.Response:
        """
        Create a new email and password user

        :param email: User account email address
        :param password: User account password
        :return: Request response from the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="signUp")
        params = build_params(key=self.api_key)
        data = {'email': email, 'password': password, 'returnSecureToken': True}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def signIn_with_email_and_password(self, email: str, password: str) -> httpx.Response:
        """
        Sign in a user with their accounts email and password

        :param email: User account email address
        :param password: User account password
        :return: Request response from the Firebase REST API

        Common Error Codes:
            . EMAIL_NOT_FOUND: There is no user record corresponding to this identifier. The user may have been deleted.
            . INVALID_PASSWORD: The password is invalid or the user does not have a password.
            . USER_DISABLED: The user account has been disabled by an administrator.
        """

        url = build_url(self.base_url, delimiter="signInWithPassword")
        params = build_params(key=self.api_key)
        data = {"email": email, "password": password, "returnSecureToken": True}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def signIn_anonymously(self) -> httpx.Response:
        """
        Sign in a user anonymously without a email and password. This lets you enforce user-specific Security and
        Firebase rules without requiring credentials from your users.

        :return: Request response from the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="signUp")
        params = build_params(key=self.api_key)
        data = {'returnSecureToken': True}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def fetch_providers_for_email(self, email: str, continueUri: str) -> httpx.Response:
        """
        Check all authentication providers associated with a specified user

        :param email: User account email address
        :param continueUri: The URI to which the IDP redirects the user back. Typically the current URL.
        :return: Request response form the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="createAuthUri")
        params = build_params(key=self.api_key)
        data = {'identifier': email, 'continueUri': continueUri}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def send_password_reset_email(self, email: str) -> httpx.Response:
        """
        Sends a password reset email to a specified user from your Firebase authentication templates

        :param email: User account email address
        :return: Request response from the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="sendOobCode")
        params = build_params(key=self.api_key)
        data = {"requestType": "PASSWORD_RESET", "email": email}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def verify_password_reset_code(self, oobCode: str) -> httpx.Response:
        """
        Verifies a password reset code was issued for the correct request type

        :param oobCode: The email action code sent to the user's email for resetting the password
        :return: Request response from the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="resetPassword")
        params = build_params(key=self.api_key)
        data = {'oobCode': oobCode}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def confirm_password_reset(self, oobCode: str, newPassword: str) -> httpx.Response:
        """
        Apply a password reset for a specified user from a requested email action code

        :param oobCode: The email action code sent to the user's email for resetting the password
        :param newPassword: The new password for the user
        :return: Request response from the Firebase REST API

        Common Error Codes:
            . OPERATION_NOT_ALLOWED: Password sign in is disabled for this project
            . EXPIRED_OOB_CODE: The action code has expired
            . INVALID_OOB_CODE: The action code is invalid. This can happen if the code is malformed, expired, or has \
                                already been used
            . USER_DISABLED: The user account has been disabled by an administrator.
            . WEEK_PASSWORD: The password provided isn't strong enough
        """

        url = build_url(self.base_url, delimiter="resetPassword")
        params = build_params(key=self.api_key)
        data = {'oobCode': oobCode, 'newPassword': newPassword}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def change_email(self, idToken: str, email: str) -> httpx.Response:
        """
        Updates the email address associated with a specified user's account

        :param idToken: The Firebase Auth ID token for the specified user
        :param email: The new email address for the specified user
        :return: Request response from the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="update")
        params = build_params(key=self.api_key)
        data = {'idToken': idToken, 'email': email, 'returnSecureToken': True}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def change_password(self, idToken: str, password: str) -> httpx.Response:
        """
        Updates the password associated with a specified user's account

        :param idToken: The Firebase Auth ID token for the specified user
        :param password: The new password for a the specified user
        :return: Request response from the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="update")
        params = build_params(key=self.api_key)
        data = {'idToken': idToken, 'password': password, 'returnSecureToken': True}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def update_profile(self, idToken: str, **kwargs) -> httpx.Response:
        """
        Updates attributes of a profile for a specified user

        :param idToken: The Firebase Auth ID token for the specified user
        :keyword displayName: The new display name for the specified user
        :keyword photoUrl: The new photo url for the specified user
        :keyword deleteAttribute: List of attributes to delete from the specified user's account. This will nullify
        the listed attributes. EXAMPLES: ['DISPLAY_NAME', 'PHOTO_URL']
        :return: Request response form the Firebase REST API

        Common Error Codes:
            . INVALID_ID_TOKEN: The user's credential is no longer valid. The user must sign in again.
        """

        url = build_url(self.base_url, delimiter="update")
        params = build_params(key=self.api_key)
        data = {'idToken': idToken} | {x: kwargs[x] for x in kwargs}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def get_user_data(self, idToken: str) -> httpx.Response:
        """
        Retrieves account data for a specified user

        :param idToken: The Firebase Auth ID token for the specified user
        :return: Request response form the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="lookup")
        params = build_params(key=self.api_key)
        data = {'idToken': idToken}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def send_email_verification(self, idToken: str) -> httpx.Response:
        """
        Sends a email verification email to a specified user from your Firebase authentication templates

        :param idToken: The Firebase Auth ID token of the specified user
        :return: Request response from the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="sendOobCode")
        params = build_params(key=self.api_key)
        data = {"requestType": "VERIFY_EMAIL", "idToken": idToken}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def confirm_email_verification(self, oobCode: str) -> httpx.Response:
        """
        Confirms an email verification code is a valid email action code

        :param oobCode: The email action code sent to the user's email for email verification
        :return: Request response from the Firebase REST API

        Common Error Code:
            . EXPIRED_OOB_CODE: The action code has expired.
            . INVALID_OOB_CODE: The action code is invalid. This can happen if the code is malformed, expired, or
                                has already been used.
            . USER_DISABLED: The user account has been disabled by an administrator.
            . EMAIL_NOT_FOUND: There is no user record corresponding to this identifier. The user may have been deleted.
        """

        url = build_url(self.base_url, delimiter="update")
        params = build_params(key=self.api_key)
        data = {'oobCode': oobCode}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req

    def delete_account(self, idToken: str) -> httpx.Response:
        """
        Deletes a current user's account

        :param idToken: The Firebase Auth ID token of the specified user
        :return: Request response from the Firebase REST API
        """

        url = build_url(self.base_url, delimiter="delete")
        params = build_params(key=self.api_key)
        data = {'idToken': idToken}

        with self.client as request:
            req = request.post(url=url, headers=self.header, params=params, json=data, timeout=3)

        check_response(response=req)
        return req
