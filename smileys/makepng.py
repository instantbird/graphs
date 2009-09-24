#!/usr/bin/env python
import os

listefichier = os.listdir("svg/")

for fichier in listefichier:
    os.system("inkscape svg/%s --export-png=png/%spng" % (fichier, fichier[:-3]))

print "Fini !"
