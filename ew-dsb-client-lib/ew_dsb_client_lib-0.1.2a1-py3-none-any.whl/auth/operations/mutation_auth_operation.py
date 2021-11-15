from typing import List

SignInAuthMutation: List[str] = ["""
  mutation signIn ($identityToken: String!) {
      signIn (identityToken: $identityToken) {
          token
      }
  }
  """
]