# Copyright (c) RedFantom 2017
# For license see LICENSE
from setuptools import setup

long_description = """
yandex
==========

A python wrapper around the Yandex API


License
-------

MIT License

Copyright (c) 2019 Dogeek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

setup(
    name="yandex",
    packages=["yandex"],
    py_modules=["yandex"],
    version="0.0.2",
    description=" A python wrapper around the Yandex API ",
    long_description=long_description,
    author="Dogeek",
    url="https://www.github.com/Dogeek/yandex",
    download_url="https://www.github.com/Dogeek/yandex/releases",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License"],
    install_requires=["requests"]
)
