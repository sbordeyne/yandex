.. yandex documentation master file, created by
   sphinx-quickstart on Fri Dec 20 19:02:16 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to yandex's documentation!
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _yandex:

yandex
==========

.. currentmodule:: yandex

.. rubric:: Classes

.. autosummary::
    :nosignatures:
    :toctree: yandex

    Yandex


.. _errors:

errors
==========

.. currentmodule:: yandex.errors

.. rubric:: Exceptions

.. autosummary::
    :nosignatures:
    :toctree: errors

    YandexError
    YandexFormatError
    YandexRequestError
    YandexTranslationError
    YandexTranslationImpossible
    YandexNotSupportedTranslationDirection
    YandexInvalidLanguageCode
    YandexAPIKeyError
    YandexInvalidAPIKey
    YandexBlockedAPIKey
    YandexAPIExceededError
    YandexDailyLimitExceeded
    YandexTextSizeExceeded
    raise_exception
