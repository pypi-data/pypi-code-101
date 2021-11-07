class ConnectionError(Exception):

   def __init__(self, message):
      super().__init__(message)
      self.message = message

   def __str__(self):
      return self.message

class NetworkPlaneFailure(Exception):

   def __init__(self, message):
      super().__init__(message)
      self.message = message

   def __str__(self):
      return self.message

class InterfaceAttachFailed(Exception):

   def __init__(self, message):
      super().__init__(message)
      self.message = message

   def __str__(self):
      return self.message

class InterfaceRegistrationFailed(Exception):

   def __init__(self, message):
      super().__init__(message)
      self.message = message

   def __str__(self):
      return self.message



class UpdateRejected(Exception):

   def __init__(self, message):
      super().__init__(message)
      self.message = message

   def __str__(self):
      return self.message

class UpdateFailed(Exception):

   def __init__(self, message):
      super().__init__(message)
      self.message = message

   def __str__(self):
      return self.message