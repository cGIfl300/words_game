#!/bin/bash /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 cGIfl300, <cgifl300@gmail.com>
# Under GPLv3 see LICENSE.md

from sys import argv

import requests
from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema


class URLError(Exception):
    """Any error related to URL, raised when the http response is not 2XX."""
    pass


def get_from_url(URL):
    """Return a text from an URL.
    URL: URL String
    """
    try:
        request = requests.get(URL)
    except MissingSchema:
        print("BAD url")
        return

    # Continue if status is ok, else raise an error
    if request.status_code < 200 or request.status_code > 299:
        raise URLError("Cannot retrieves URL.")
        return

    # Cleaning HTML to get the text only
    soup = BeautifulSoup(request.text, "html.parser")
    return soup.get_text()


if __name__ == "__main__":
    from wordsgame import WordsGame

    app = WordsGame()
    content = ""

    try:
        url = argv[1]
    except IndexError:
        print("I need one url.")
        exit()

    print(f"Retrieving {url}")
    app.get_from_url(url)
    print(app.words_list)
