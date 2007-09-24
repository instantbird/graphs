#!/usr/bin/env python
import os

listefichier = os.listdir("svg/")

for fichier in listefichier:
    os.system("inkscape svg/%s --export-png=png/%spng --export-width=32 --export-height=32" % (fichier, fichier[:-3]))

print "Fini !"