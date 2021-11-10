from exceptions.base_exception import BaseCustomHttpException


class ItemNotFound(BaseCustomHttpException):
    pass



class DontHavePermission(BaseCustomHttpException):
    pass


class OTPWrongException(BaseCustomHttpException):
    pass

class OtpCodeExpiredException(BaseCustomHttpException):
    pass


class OtpSentLastTime(BaseCustomHttpException):
    pass

class SMSNotSent(BaseCustomHttpException):
    pass

class MessageNotSend(BaseCustomHttpException):
    pass

class InvalidInputException(BaseCustomHttpException):
    pass

class ReplyYourSelf(BaseCustomHttpException):
    pass

class TicketClose(BaseCustomHttpException):
    pass


