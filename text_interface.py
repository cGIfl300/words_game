#!/bin/bash /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 cGIfl300, <cgifl300@gmail.com>
# Under GPLv3 see LICENSE.md

from wordsgame import WordsGame

result = []

app = WordsGame()


def demo_acquirer():
    # Acquire a new file
    app.acquirer("data\\liste_francais.txt")
    app.save()


def play():
    print(
        """We do use regex, example: .ch. => echo, tcho.
NOT NEEDED : ^start
NOT NEEDED : end$
. any char\n
exit: exit the software\n"""
    )
    pattern = input("Pattern : ")

    if pattern == "":
        # My own easter :-)
        pattern = "..."

    if pattern == "exit":
        print("Exiting software, thank you for playing.")
        exit()

    print("\n==========")
    print(app.find_word(pattern))
    print(f"{len(app.find_word(pattern))} match")
    print("==========\n")


print("Loading dictionary")
# If there are no initial db, that's not a problem, just ignore.
try:
    app.load()
except FileNotFoundError:
    pass

# demo_acquirer()

while True:
    play()
