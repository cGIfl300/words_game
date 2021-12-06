#!/bin/bash /usr/bin/env python3

# -*- coding: utf-8 -*-

# Copyright (C) 2021 cGIfl300, <cgifl300@gmail.com>

# Under GPLv3 see LICENSE.md


def clean_string(allowed, string):
    """Clean a string from unwanted characters.
    allowed: list of allowed characters, if none we use [a-z]-(space)
    string: the string to clean
    """
    tmp_string = ""

    if allowed == "":
        allowed = "abcdefghijklmnopqrstuvwxyz- "

    if string == "":
        raise (ValueError("A string is needed."))

    for character in string:
        if character in allowed:
            tmp_string = tmp_string + character
    return tmp_string
