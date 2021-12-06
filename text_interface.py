#!/bin/bash /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 cGIfl300, <cgifl300@gmail.com>
# Under GPLv3 see LICENSE.md

import re
from wordsgame import WordsGame

result = []

app = WordsGame()
print("Loading dictionnary")

# If there are no initial db, that's not a problem, just ignore.
try:
    app.load()
except FileNotFoundError:
    pass

#pp.acquirer("data\\liste_francais.txt")
#app.save()

print("""We do use regex, exemple: .ch. => echo, tcho.
NOT NEEDED : ^start
NOT NEEDED : end$
. any char\n""")
pattern = input("Votre patern : ")
result = re.compile(f"^{pattern}$")
wordlist = list(filter(result.match, app.words_list))
print(wordlist)
