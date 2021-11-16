class WebServerIsDead(Exception):
    pass


class KeyTypeUnresolved(Exception):
    pass


class MethodMissing(Exception):
    pass


class Rejected(Exception):
    pass


class AuthorizationMissing(Exception):
    pass


class AuthorizationValidationFailed(Exception):
    pass


class AuthorizationTokenDoesNotExist(Exception):
    pass


class RateLimit(Exception):
    pass


class TokenDisabled(Exception):
    pass


class UserNotFound(Exception):
    pass


class ImageMissing(Exception):
    pass


def recognizeError(error_code):
    if error_code == -3:
        return WebServerIsDead("Веб сервер умер, сообщите об этой ситуации в поддержку.")
    elif error_code == -2:
        return KeyTypeUnresolved("Ключ с таким типом не поддерживается.")
    elif error_code == -1:
        return MethodMissing("Метод не найден.")
    elif error_code == 0:
        return Rejected("Токен авторизации не обладает запрашиваемыми правами доступа.")
    elif error_code == 1:
        return AuthorizationMissing("Указан неверный ключ.")
    elif error_code == 2:
        return AuthorizationValidationFailed("Указан неверный ключ.")
    elif error_code == 3:
        return AuthorizationTokenDoesNotExist("Токен авторизации не существует.")
    elif error_code == 4:
        return RateLimit("Превышен лимит запросов в минуту.")
    elif error_code == 5:
        return TokenDisabled("Токен авторизации отключен.")
    elif error_code == 6:
        return UserNotFound("Запрашиваемый пользователь не найден.")
    elif error_code == 7:
        return ImageMissing("Изображение не найдено, попробуйте изменить параметры поиска.")
