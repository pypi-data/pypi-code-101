from typing import Any

from us_libraries.client.base_client import BaseClient
from us_libraries.graphite import client_timing

service_name = "usf-account-service"


class AccountClient(BaseClient):
    def __init__(self) -> None:
        super().__init__(service_name)

    @client_timing
    def get_driver(self, driver_id: int) -> Any:
        return self.get(f'driver/{driver_id}')

    @client_timing
    def add_user(self,
                   user_id: int = None,
                   user_first_name: str = None,
                   user_last_name: str = None,
                   user_type: str = None,
                   user_id_type: str = None,
                   user_id_number: str = None,
                   user_gender: str = None,
                   user_email: str = None,
                   user_phone: str = None,
                   user_date_of_birth: int = None,
                   user_profile_image_file_id: int = None,
                   # user_status: str = None, # default = 'ACTIVE'
                   # user_date_created: int = None,
                   # user_date_modified: int = None,

                   # driver_status: str = None, # default is = 'INCOMPLETE'
                   # driver_application_rejected_reason: bool = None,
                   driver_license_number: str = None,
                   # driver_is_online: bool = None, # default is = false
                   # driver_current_location_id: int = None,
                   # driver_account_balance: float = None,
                   ) -> Any:
        return self.post('user',
                         user_id=user_id,
                         user_first_name=user_first_name,
                         user_last_name=user_last_name,
                         user_type=user_type,
                         user_id_type=user_id_type,
                         user_id_number=user_id_number,
                         user_gender=user_gender,
                         user_email=user_email,
                         user_phone=user_phone,
                         user_date_of_birth=user_date_of_birth,
                         user_profile_image_file_id=user_profile_image_file_id,
                         driver_license_number=driver_license_number,
                         )
