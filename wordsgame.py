#!/bin/bash /usr/bin/env python3


# -*- coding: utf-8 -*-


# Copyright (C) 2021 cGIfl300, <cgifl300@gmail.com>


# Under GPLv3 see LICENSE.md


import json
import re

from unidecode import unidecode

from clean_string import clean_string
from get_from_url import get_from_url


class WordsGame:
    """WordsGames



    This class is the all-in-one tool for this project."""

    words_list = []  # The global words list

    data_base_path = "data\\mydb.json"

    def acquirer(self, filename):

        """Acquirer every words from a filename.



        filename:string : filename location, absolute path should be unicode"""

        print(f"Reading {filename}")

        file_content = ""

        try:

            file = open(filename, "r")

            file_content = file.read()
            file.close()

        except UnicodeDecodeError:

            print(f"I can't open the file {filename}. Let's continue anyway.")

            return

        self.__add_words(file_content)

    def get_from_url(self, url):
        """Get words from a given url"""
        content = ""
        content = get_from_url(url)
        self.__add_words(content)

    def __add_words(self, data):
        """Adding words from a string."""
        tmp_words_list = []
        if len(data) == 0:
            # exit if the file is empty
            print("Nothing to add.")
            return

        data = " ".join(data.splitlines())

        # convert french specific characters to latins
        allowed = "abcdefghijklmnopqrstuvwxyz- "
        data = unidecode(data, errors="ignore")
        data = data.lower()

        # Cleaning the file from illegal characters

        data = clean_string(allowed, data)

        tmp_words_list = data.split(" ")

        for word in tmp_words_list:

            if len(word.strip(" ")) > 2:
                self.words_list.append(word)

        # Delete twins

        self.words_list = list(set(self.words_list))

        # Sort by alphabetical
        self.words_list.sort()

    def save(self):

        """Save the words list to disk"""

        with open(self.data_base_path, "w") as file:
            json.dump(self.words_list, file)
            file.close()

        print(f"{len(self.words_list)} words saved.")

    def load(self):

        """Load the words list from disk"""

        with open(self.data_base_path, "r") as file:
            self.words_list = json.load(file)
            file.close()

        print(f"{len(self.words_list)} words loaded.")

    def find_word(self, pattern):

        """Search for a word.


        pattern: only . or a letter


        return: a list of words, [] if none
        """

        # Clean pattern from unwanted characters

        allowed = "abcdefghijklmnopqrstuvwxyz."

        pattern = pattern.lower()

        pattern = clean_string(allowed, pattern)

        result = re.compile(f"^{pattern}$")

        return list(filter(result.match, self.words_list))
