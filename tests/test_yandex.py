import unittest
from unittest.mock import patch, MagicMock
import yandex
try:
    from .test_config import API_KEY
except ImportError:
    API_KEY = "TEST_API_KEY"

class MockResponse:
    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data

    def json(self):
        return self.data


class TestYandex(unittest.TestCase):
    def setUp(self):
        self.translate_mock_200 = MagicMock(return_value=MockResponse(200, {'text': ['Bonjour Tout Le Monde!']}))
        self.guess_mock_200 = MagicMock(return_value=MockResponse(200, {'lang': 'en'}))
        self.mock_401 = MagicMock(return_value=MockResponse(400, {"code": 401, "message": "API key is invalid"}))
        self.mock_402 = MagicMock(return_value=MockResponse(400, {"code": 402, "message": "API key is blocked"}))
        self.mock_404 = MagicMock(return_value=MockResponse(400, {"code": 404, "message": "Exceeded the daily limit on the amount of translated text"}))
        self.mock_413 = MagicMock(return_value=MockResponse(400, {"code": 413, "message": "Exceeded the maximum text size"}))
        self.mock_422 = MagicMock(return_value=MockResponse(400, {"code": 422, "message": "The text cannot be translated"}))
        self.mock_501 = MagicMock(return_value=MockResponse(400, {"code": 501, "message": "The specified translation direction is not supported"}))
        self.tr = yandex.Yandex(API_KEY)

    def test_translate(self):
        with patch('requests.post', self.translate_mock_200):
            self.assertEqual(self.tr.translate("Hello World!", "fr"), "Bonjour Tout Le Monde!")

    def test_guess_language(self):
        with patch('requests.post', self.guess_mock_200):
            self.assertEqual(self.tr.guess_language("Hello World!"), "en")

    def test_invalid_api_key(self):
        with patch('requests.post', self.mock_401):
            with self.assertRaises(yandex.YandexInvalidAPIKey):
                self.tr.guess_language("Hello World!")

    def test_blocked_api_key(self):
        with patch('requests.post', self.mock_402):
            with self.assertRaises(yandex.YandexBlockedAPIKey):
                self.tr.guess_language("Hello World!")

    def test_daily_limit_exceeded(self):
        with patch('requests.post', self.mock_404):
            with self.assertRaises(yandex.YandexDailyLimitExceeded):
                self.tr.translate('Hello World!', 'fr')

    def test_text_size_exceeded(self):
        with patch('requests.post', self.mock_422):
            with self.assertRaises(yandex.YandexTranslationImpossible):
                self.tr.translate('Hello World!', 'fr')

    def test_translation_impossible(self):
        with patch('requests.post', self.mock_422):
            with self.assertRaises(yandex.YandexTranslationImpossible):
                self.tr.translate('Hello World!', 'fr')

    def test_translation_direction_not_supported(self):
        with patch('requests.post', self.mock_501):
            with self.assertRaises(yandex.YandexNotSupportedTranslationDirection):
                self.tr.translate('Hello World!', 'fr')
