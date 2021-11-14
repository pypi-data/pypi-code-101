import requests


class SmartThingsError(Exception):
    pass


class SmartThings:
    def __init__(self, personal_access_token):
        # include api_key in all requested url the session
        self.url = "https://api.smartthings.com/v1/"

        self._s = requests.Session()
        self._s.headers = {"Authorization": f"Bearer {personal_access_token}"}

    def _get(self, path):
        """
        Makes GET request, (auth is baked in to the session)
        Returns response as object
        """
        r = self._s.get(f"{self.url}/{path}")

        if r.ok:
            return r.json()
        else:
            if r.status_code == 401:
                raise SmartThingsError("Unauthorized")

            # We got a bad error, raise it and wrapp the error msg for sending it up
            # this way we get a good error msg on every bad request
            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as error_msg:
                raise SmartThingsError(error_msg) from error_msg

    def capabilities(self):
        return self._get("capabilities")

    def devices(self):
        """Returns devices"""
        r = self._get("devices")
        return r["items"]

    def device(self, id_key, id_value):
        devices = self._get("devices")
        for device in devices:
            if device[id_key] == id_value:
                return device[id_value]


# class raw_st():
#     def __init__(self, personal_access_token):
#         self.url = "https://api.smartthings.com/v1/"
#         self._s = requests.Session()
#         self._s.headers = {"Authorization": f"Bearer {personal_access_token}"}
    



# class Device:
#     def __init__(self, id) -> None:
#         self.id = id

