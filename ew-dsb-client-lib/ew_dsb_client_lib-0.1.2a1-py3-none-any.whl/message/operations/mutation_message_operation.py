from typing import List

PublishMessageMutation: List[str] = ["""
  mutation publishMessage ($publishMessageDto: PublishMessageDto!) {
    publishMessage (publishMessageDto: $publishMessageDto)
  }
  """
]

SendMessageMutation: List[str] = ["""
  mutation sendMessage ($sendMessageDto: SendMessageDto!) {
    sendMessage (sendMessageDto: $sendMessageDto) 
  }
  """
]

