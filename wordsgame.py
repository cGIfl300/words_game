#!/bin/bash /usr/bin/env python3

# -*- coding: utf-8 -*-

# Copyright (C) 2021 cGIfl300, <cgifl300@gmail.com>

# Under GPLv3 see LICENSE.md


from unidecode import unidecode
from clean_string import clean_string
import json
import re


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

        tmp_words_list = []

        try:
            file = open(filename, "r")
            file_content = file.read()
            file.close()
        except UnicodeDecodeError:
            print(f"I can't open the file {filename}. Let's continue anyway.")
            return

        if len(file_content) == 0:

            # exit if the file is empty

            print("The file is empty.")

            return

        file_content = " ".join(file_content.splitlines())

        # convert french specific characters to latins

        allowed = "abcdefghijklmnopqrstuvwxyz- "

        file_content = unidecode(file_content, errors="ignore")

        file_content = file_content.lower()

        # Cleaning the file from illegal characters

        file_content = clean_string(allowed, file_content)

        tmp_words_list = file_content.split(" ")

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
