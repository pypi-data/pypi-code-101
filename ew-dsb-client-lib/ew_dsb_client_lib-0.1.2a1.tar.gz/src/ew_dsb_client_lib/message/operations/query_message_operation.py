from typing import List

FindAllMessagesQuery: List[str] = ["""
  query findAllMessages ($findAllMessagesDto: FindAllMessagesDto!) {
    findAllMessages (findAllMessagesDto: $findAllMessagesDto) {
      payload
      signature
    }
  }
  """
]