from MSApi.ObjectMS import ObjectMS, check_init


class Assortment(ObjectMS):

    def __init__(self, json):
        super().__init__(json)

    @check_init
    def get_id(self) -> str:
        return self._json.get('id')

    @check_init
    def get_name(self) -> str:
        return self._json.get('name')