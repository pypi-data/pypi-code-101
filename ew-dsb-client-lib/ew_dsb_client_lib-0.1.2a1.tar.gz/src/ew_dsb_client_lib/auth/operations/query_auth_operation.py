from typing import List

GetUserAuthQuery: List[str] = ["""
    query getUser {
        getUser {
            did
            verifiedRoles {
                name
                namespace
            }
        }
    }
    """
]

GetUserDIDAuthQuery: List[str] = ["""
    query getUserDID {
        getUserDID 
    }
    """
]

GetUserRolesAuthQuery: List[str] = ["""
    query getUserRoles {
        getUserRoles {
            name
            namespace
        }
    }
    """
]