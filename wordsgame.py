#!/bin/bash /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 cGIfl300, <cgifl300@gmail.com>
# Under GPLv3 see LICENSE.md

from unidecode import unidecode
import json


class WordsGame():
    '''WordsGames
    This class is the all-in-one tool for this project.'''
    words_list = []  # The global words list

    def acquiert(self, filename):
        '''Acquiert every words from a filename.
        filename:string : filename location, absolute path should be unicode'''
        file_content = ""
        tmp_file_content = ""
        tmp_words_list = []
        offset = 0

        file = open(filename, "r")
        file_content = file.read()
        file.close()

        if len(file_content) == 0:
            # exit if the file is empty
            print("The file is empty.")
            return
        file_content = " ".join(file_content.splitlines())
        # convert french specific characters to latins
        allowed = "abcdefghijklmnopqrstuvwxyz- "
        file_content = unidecode(file_content)
        file_content = file_content.lower()
        # Cleaning the file from illegal characters
        for character in file_content:
            if character in allowed:
                tmp_file_content = tmp_file_content + character
        file_content = tmp_file_content
        tmp_file_content = ""

        tmp_words_list = file_content.split(" ")
        for word in tmp_words_list:
            if len(word.strip(" ")) < 2:
                self.words_list.append(word.strip(" "))
        # Delete twins
        self.words_list = list(set(self.words_list))
        # Sort by alphabetical
        self.words_list.sort()

    def save(self):
        ''' Save the words list to disk '''
        with open("data\mydb.json", "w") as file:
            json.dump(self.words_list, file)
            file.close()
        print(f"{len(self.words_list)} words saved.")

    def load(self):
        ''' Load the words list from disk '''
        with open("data\mydb.json", "r") as file:
            self.words_list = json.load(file)
            file.close()
        print(f"{len(self.words_list)} words loaded.")
