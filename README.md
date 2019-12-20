# yandex
[![Build Status](https://travis-ci.com/Dogeek/yandex.svg?branch=master)](https://travis-ci.com/Dogeek/yandex)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/15baf69736f14416b91fadba1524bc94)](https://www.codacy.com/manual/Dogeek/yandex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Dogeek/yandex&amp;utm_campaign=Badge_Grade)

 A python wrapper around the Yandex API

## Testing

Create a file named "test_config.py" in the tests/ folder, and paste in the following :

```python
API_KEY = "<your_api_token_here>"
```

You can get an API token here : https://translate.yandex.com/developers/keys

## Usage

Instantiate the `Yandex` object with your API token. You can then use the `translate` method to translate text from one language to another.

```python
from yandex import Yandex

tr = Yandex("MY_API_TOKEN")
tr.translate("Hello World", "fr")
tr.translate("Bonjour tout le monde!", to_lang="en", from_lang="fr")
```

Yandex can detect which language the text is in, therefore, the `from_lang` argument is optional. You can also translate text formatted in html

```python
tr.translate("<p>Hello World!</p>", "fr", format="html")
```

Or you can use the API to guess a language from a text sample :

```python
tr.guess_language("Hello World!")
```

You can get a list of all available language code pairs with the `get_language_pairs` method,
and a dictionary mapping all the language codes to their names with the `get_language_map` method
