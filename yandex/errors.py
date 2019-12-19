class YandexError(Exception):
    pass


class YandexFormatError(YandexError):
    pass


class YandexRequestError(YandexError):
    def __init__(self, status_code):
        messages = {400: "Invalid language code.",
                    401: "Invalid API key.",
                    402: "Blocked API key.",
                    404: "Daily limit on the amount of translated text exceeded.",
                    413: "Exceeded the maximum text size.",
                    422: "The text cannot be translated.",
                    501: "The specified translation direction is not supported."}
        self.status_code = status_code
        self.message = 'YandexRequestError : {}'.format(messages[status_code])

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message
