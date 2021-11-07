from typing import List

from pyinaturalist.constants import IntOrStr
from pyinaturalist.controllers import BaseController
from pyinaturalist.docs import document_controller_params
from pyinaturalist.models import User
from pyinaturalist.paginator import IDPaginator, Paginator
from pyinaturalist.v1 import get_user_by_id, get_users_autocomplete


class UserController(BaseController):
    """:fa:`user` Controller for User requests"""

    def from_id(self, *user_ids: IntOrStr, **params) -> Paginator[User]:
        """Get users by ID

        Example:
            Get a user by ID:

            >>> user = client.users.from_id(1).one()

            Get multiple users by ID:

            >>> users = client.users.from_id(1).all()

        Args:
            user_ids: One or more project IDs
        """
        return IDPaginator(get_user_by_id, User, ids=user_ids, **params)

    @document_controller_params(get_users_autocomplete)
    def autocomplete(self, **params) -> List[User]:
        response = get_users_autocomplete(**params)
        return User.from_json_list(response)
