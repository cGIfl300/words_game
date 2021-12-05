#!/bin/bash /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 cGIfl300, <cgifl300@gmail.com>
# Under GPLv3 see LICENSE.md

import re
from wordsgame import WordsGame

result = []

app = WordsGame()
print("Loading dictionnary")
# app.acquiert("data\liste_francais.txt")
# app.save()
app.load()

print("""We do use regex, exemple: .ch. => echo, tcho.
NOT NEEDED : ^start
NOT NEEDED : end$
. any char\n""")
pattern = input("Votre patern : ")
result = re.compile(f"^{pattern}$")
wordlist = list(filter(result.match, app.words_list))
print(wordlist)
