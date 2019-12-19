import unittest
import yandex
from test_config import API_KEY

class TestYandex(unittest.TestCase):
    def setUp(self):
        self.tr = yandex.Yandex(API_KEY)

    def test_translate(self):
        self.assertEqual(self.tr.translate("Hello World!", "fr"), "Bonjour Tout Le Monde!")

    def test_guess_language(self):
        self.assertEqual(self.tr.guess_language("Hello World!"), "en")
