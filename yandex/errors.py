class YandexError(Exception):
    pass


class YandexFormatError(YandexError):
    pass


class YandexRequestError(YandexError):
    message = ""

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message


class YandexTranslationError(YandexRequestError):
    pass


class YandexTranslationImpossible(YandexTranslationError):
    message = "422 : The text cannot be translated."
    status_code = 422


class YandexNotSupportedTranslationDirection(YandexTranslationError):
    message = "501 : The specified translation direction is not supported."
    status_code = 501


class YandexInvalidLanguageCode(YandexTranslationError):
    message = "400 : Invalid language code."
    status_code = 400


class YandexAPIKeyError(YandexRequestError):
    pass


class YandexInvalidAPIKey(YandexAPIKeyError):
    message = "401 : Invalid API key."
    status_code = 401


class YandexBlockedAPIKey(YandexAPIKeyError):
    message = "402 : Blocked API key."
    status_code = 402


class YandexAPIExceededError(YandexRequestError):
    pass


class YandexDailyLimitExceeded(YandexAPIExceededError):
    message = "404 : Daily limit on the amount of translated text exceeded."
    status_code = 404


class YandexTextSizeExceeded(YandexAPIExceededError):
    message = "413 : Exceeded the maximum text size."
    status_code = 413


def raise_exception(response):
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
