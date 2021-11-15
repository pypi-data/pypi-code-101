#!/usr/bin/env python3

from typing import Any, Dict, List

from ew_dsb_client_lib.auth.dtos.get_user_did_response_dto import \
    GetUserDIDResponseDto
from ew_dsb_client_lib.auth.dtos.get_user_response_dto import \
    GetUserResponseDto
from ew_dsb_client_lib.auth.dtos.get_user_roles_response_dto import \
    GetUserRolesResponseDto
from ew_dsb_client_lib.auth.dtos.signin_response_dto import SignInResponseDto
from ew_dsb_client_lib.auth.entities.claim_data_entity import ClaimData
from ew_dsb_client_lib.auth.entities.public_claim_entity import PublicClaim
from ew_dsb_client_lib.auth.entities.user_entity import User
from ew_dsb_client_lib.auth.entities.user_jwt_entity import UserJwt
from ew_dsb_client_lib.auth.entities.user_role_entity import UserRole
from ew_dsb_client_lib.auth.operations.mutation_auth_operation import \
    SignInAuthMutation
from ew_dsb_client_lib.auth.operations.query_auth_operation import (
    GetUserAuthQuery, GetUserDIDAuthQuery, GetUserRolesAuthQuery)
from ew_dsb_client_lib.crypto.crypto_service import CryptoService
from ew_dsb_client_lib.gqls.gql_service import GQLService
from gql import Client, gql


class AuthService:
    http_client: Client
    crypto_service: CryptoService

    def __init__(self, gql_service:GQLService):
        self.http_client = gql_service.http_client
        self.crypto_service = CryptoService()

    def create_identity(self, user_DID:str, private_key:str) -> str:
        """Create Identity token

        Parameters
        ----------
        user_DID : str
        private_key : str

        Returns
        -------
        str
        """
        # TODO: Get the actual blockNumber from provider
        # https://web3py.readthedocs.io/en/stable/providers.html#httpprovider
        claim_data:ClaimData = ClaimData(
            # NB: Just for dev purposes. Avoids `LoginStrategy` "Claim outdated" validation.
            blockNumber=999999999999
        )
        claim:PublicClaim = PublicClaim(
            claimData=claim_data,
            iss=user_DID
        )
        payload:str = claim.to_json()
        
        jwt_identity_token:str = self.crypto_service.sign(payload, private_key)
        return jwt_identity_token

    async def sign_in(self, identityToken:str) -> UserJwt:
        """Sign in user 

        Parameters
        ----------
        identityToken : str

        Returns
        -------
        UserJwt
        """
        query = gql("".join(set(SignInAuthMutation)))
        variables: Dict[str, Any] = {
            'identityToken': identityToken
        }
        response_text = await self.http_client.execute_async(
            query, 
            variable_values=variables
        )
        res = SignInResponseDto.from_dict(response_text)
        return res.signIn

    async def get_user(self) -> User:
        """Get user metadata

        Returns
        -------
        User
        """
        query = gql("".join(set(GetUserAuthQuery)))
        response_text = await self.http_client.execute_async(
            query
        )
        res = GetUserResponseDto.from_dict(response_text)
        return res.getUser

    async def get_user_DID(self) -> str:
        """Get user DID

        Returns
        -------
        str
        """
        query = gql("".join(set(GetUserDIDAuthQuery)))
        response_text = await self.http_client.execute_async(
            query
        )
        res = GetUserDIDResponseDto.from_dict(response_text)
        return res.getUserDID

    async def get_user_roles(self) -> List[UserRole]:
        """Get user roles

        Returns
        -------
        List[UserRole]
        """
        query = gql("".join(set(GetUserRolesAuthQuery)))
        response_text = await self.http_client.execute_async(
            query
        )
        res = GetUserRolesResponseDto.from_dict(response_text)
        return res.getUserRoles
