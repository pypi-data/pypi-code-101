import requests
import json


class Client:
    def __init__(self, gatewayAddress):
        self.gatewayAddress = gatewayAddress

    def token(self, email, password):
        r = self.__http_do(
            path="/api-gw/v1/user/login",
            method="post",
            token="",
            data={"email": email, "password": password}
        )

        response = r.json()

        if not response.get("token"):
            raise Exception("invalid response: " + json.dumps(response))

        parts = response.get("token").split(" ")
        if len(parts) != 2:
            raise Exception("invalid response: " + json.dumps(response))

        return parts[1]

    def token_verify(self, token):
        try:
            self.__http_do(
                path="/api-gw/v1/user/verify",
                method="get",
                token=token,
                data=None
            )
            return True
        except:
            return False

    def reset_password(self, token, new_pw, old_pw):
        self.__http_do(
            path="/api-gw/v1/user/reset-password",
            method="post",
            token=token,
            data={
                "newPassword": new_pw,
                "oldPassword": old_pw,
            }
        )

    def user_profile(self, token):
        response = self.__http_do(
            path="/api-gw/v1/user/profile",
            method="get",
            token=token,
            data=None
        )

        jsonBody = response.json()

        return {
            "id": jsonBody.get("id"),
            "email": jsonBody.get("email"),
            "fullname": jsonBody.get("fullName"),
            "phone_number": jsonBody.get("phoneNumber"),
            "customer_id": jsonBody.get("customerId"),
            "user_type_id": jsonBody.get("userTypeId"),
            "user_status_id": jsonBody.get("userGroupId"),
            "created_by": jsonBody.get("createdBy")
        }

    def __http_do(self, path, method, token, data):
        headers = {}

        if token:
            headers["Authorization"] = "Bearer %s" % token

        r = requests.request(
            url=self.gatewayAddress + path,
            method=method,
            headers=headers,
            json=data,
        )

        if r.status_code != 200 and r.status_code != 201:
            raise Exception("aiot.client error: " + r.text)

        return r
