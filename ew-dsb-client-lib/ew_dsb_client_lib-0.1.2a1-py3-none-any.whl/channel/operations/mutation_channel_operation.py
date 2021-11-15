from typing import List

CreateChannelMutation: List[str] = ["""
  mutation createChannel ($createChannelDto: CreateChannelDto!) {
    createChannel (createChannelDto: $createChannelDto) {
      fqcn
      description
      publicKey
      privateKey
      maxTimeout
      defaultTimeout
    }
  }
  """
]

RemoveChannelMutation: List[str] = ["""
  mutation removeChannel ($removeChannelDto: RemoveChannelDto!) {
    removeChannel (removeChannelDto: $removeChannelDto)
  }
  """
]