#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

listefichiers=["wizHeader", "wizHeaderRTL", "wizWatermark"]

for fichier in listefichiers:
	os.system("inkscape svg/%s.svg --export-png=bmp/%s.png" % (fichier, fichier))
	os.system("convert bmp/%s.png bmp/%s.bmp" % (fichier, fichier))
	#os.system("rm bmp/%s.png" % fichier)

print "\nFini !"
