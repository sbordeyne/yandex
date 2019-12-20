class YandexError(Exception):
    """ Base Exception for all Yandex related errors """
    pass


class YandexFormatError(YandexError):
    """ Exception signaling an error in format for the `translate` method"""
    pass


class YandexRequestError(YandexError):
    """ Base Exception for all request related errors """
    message = ""

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message


class YandexTranslationError(YandexRequestError):
    """ Base Exception for all translation related errors. Inherits from YandexRequestError"""
    pass


class YandexTranslationImpossible(YandexTranslationError):
    """ The text cannot be translated. """
    message = "422 : The text cannot be translated."
    status_code = 422


class YandexNotSupportedTranslationDirection(YandexTranslationError):
    """ The translation direction is not supported """
    message = "501 : The specified translation direction is not supported."
    status_code = 501


class YandexInvalidLanguageCode(YandexTranslationError):
    """ The language code is invalid """
    message = "400 : Invalid language code."
    status_code = 400


class YandexAPIKeyError(YandexRequestError):
    """ Base Exception for all API Key errors """
    pass


class YandexInvalidAPIKey(YandexAPIKeyError):
    """ API Key is invalid """
    message = "401 : Invalid API key."
    status_code = 401


class YandexBlockedAPIKey(YandexAPIKeyError):
    """ API Key has been blocked """
    message = "402 : Blocked API key."
    status_code = 402


class YandexAPIExceededError(YandexRequestError):
    """ Base Exception for all rate-limit related errors """
    pass


class YandexDailyLimitExceeded(YandexAPIExceededError):
    """ The daily limit on the amount of text to be translated has been exceeded """
    message = "404 : Daily limit on the amount of translated text exceeded."
    status_code = 404


class YandexTextSizeExceeded(YandexAPIExceededError):
    """ The text amount to be translated at once is too large. """
    message = "413 : Exceeded the maximum text size."
    status_code = 413


def raise_exception(response):
    """
    Raises an appropriate YandexError exception based on the response.

    :param response: response from the request.
    :type response: requests.Response

    :raises: yandex.YandexError subclass
    """
    exceptions = {400: YandexInvalidLanguageCode,
                  401: YandexInvalidAPIKey,
                  402: YandexBlockedAPIKey,
                  404: YandexDailyLimitExceeded,
                  413: YandexTextSizeExceeded,
                  422: YandexTranslationImpossible,
                  501: YandexNotSupportedTranslationDirection}
    data = response.json()
    if data['code'] in exceptions.keys():
        raise exceptions[data['code']]()
    else:
        raise YandexError(str(data))
