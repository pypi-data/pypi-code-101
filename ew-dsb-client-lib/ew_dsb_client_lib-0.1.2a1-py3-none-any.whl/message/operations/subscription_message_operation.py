from typing import List

SubscribeMessageSubscription: List[str] = ["""
  subscription subscribeMessage ($subscribeMessageDto: SubscribeMessageDto!) {
    subscribeMessage (subscribeMessageDto: $subscribeMessageDto){
      payload
      signature
    }
  }
  """
]

ReceiveMessageSubscription: List[str] = ["""
  subscription receiveMessage ($receiveMessageDto: ReceiveMessageDto!) {
    receiveMessage (receiveMessageDto: $receiveMessageDto){
      payload
      signature
    }
  }
  """
]