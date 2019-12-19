import requests
from yandex.errors import YandexFormatError, YandexRequestError


class Yandex:
    """ Yandex python wrapper. """

    def __init__(self, api_token):
        """
            :param api_token: API token from yandex.
            :type api_token: str
        """
        self.token = api_token

    def guess_language(self, text, possible_languages=None):
        """
        Guesses the language from a text sample

        :param text: text sample
        :type text: str
        :param possible_languages: (default : []) possible languages the text might be in
        :type possible_languages: list or int

        :returns: language code of the text sample
        :rtype: str
        :raises: yandex.YandexRequestError
        """
        if possible_languages is None:
            possible_languages = []

        url = "https://translate.yandex.net/api/v1.5/tr.json/detect"
        payload = {"key": self.token,
                   "text": text,
                   "hint": possible_languages}
        resp = requests.post(url, data=payload)
        if resp.status_code == 200:
            return resp.json()['lang']
        else:
            raise YandexRequestError(resp.status_code)

    def translate(self, text, to_lang, from_lang="", format='plain'):
        """
        Translates text from a language into another one.

        :param text: text to translate
        :type text: str
        :param to_lang: language code to translate to.
        :type to_lang: str
        :param from_lang: (default: "") language code of the original language. Yandex will guess the language if omitted.
        :type from_lang: str
        :param format: (default: 'plain') format of the text. One of either ('plain', 'html')
        :type format: str

        :returns: translated text
        :rtype: str
        :raises: yandex.YandexFormatError
        :raises: yandex.YandexRequestError
        """
        if format not in ('plain', 'html'):
            raise YandexFormatError("Format is not one of ('plain', 'html') : {}".format(format))
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"

        if from_lang:
            lang_code = "{}-{}".format(from_lang.lower(), to_lang.lower())
        else:
            lang_code = to_lang.lower()

        payload = {"key": self.token,
                   "text": text,
                   "lang": lang_code,
                   "format": format,
                   }
        resp = requests.post(url, data=payload)
        if resp.status_code == 200:
            return resp.json()['text'][0]
        else:
            raise YandexRequestError(resp.status_code)

    def get_language_map(self, lang='en'):
        """
        Gets a dictionary mapping of all supported languages

        :param lang: (default: 'en') language in which the lang names will be.

        :returns: dictionary of supported languages in the format {'lang_code': 'lang_name'}
        :rytpe: dict<str, str>
        :raises: yandex.YandexRequestError
        """
        url = "https://translate.yandex.net/api/v1.5/tr.json/getLangs"

        payload = {"key": self.token,
                   "ui": lang}

        resp = requests.post(url, data=payload)
        if resp.status_code == 200:
            return resp.json()['langs']
        else:
            raise YandexRequestError(resp.status_code)

    def get_language_pairs(self, lang='en'):
        """
        Gets a list of all supported languages pairs

        :param lang: (default: 'en') language in which the lang names will be.

        :returns: list of all supported language pairs in the format 'from-to'
        :rytpe: list<str>
        :raises: yandex.YandexRequestError
        """
        url = "https://translate.yandex.net/api/v1.5/tr.json/getLangs"

        payload = {"key": self.token,
                   "ui": lang}

        resp = requests.post(url, data=payload)
        if resp.status_code == 200:
            return resp.json()['dirs']
        else:
            raise YandexRequestError(resp.status_code)
