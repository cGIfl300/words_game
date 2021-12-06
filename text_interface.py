#!/bin/bash /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 cGIfl300, <cgifl300@gmail.com>
# Under GPLv3 see LICENSE.md

import re
from wordsgame import WordsGame

result = []

app = WordsGame()


def play():
    print("""We do use regex, example: .ch. => echo, tcho.
NOT NEEDED : ^start
NOT NEEDED : end$
. any char\n
exit: exit the software""")
    pattern = input("Pattern : ")

    if pattern == "":
        # My own easter :-)
        pattern = "..."

    if pattern == "exit":
        print("Exiting software, thank you for playing.")
        exit()

    print("\n==========")
    print(app.find_word(pattern))
    print("==========\n")


print("Loading dictionnary")
# If there are no initial db, that's not a problem, just ignore.
try:
    app.load()
except FileNotFoundError:
    pass

# Acquire a new file
# app.acquirer("data\\liste_francais.txt")
# app.save()

while True:
    play()