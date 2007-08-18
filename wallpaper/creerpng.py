#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

listedimensions=[["4-3", 800, 600], ["4-3", 1024, 768], ["5-4", 1280, 1024], ["16-10", 1280, 800], ["16-10", 1440, 900], ["16-10", 1680, 1050]]

for a in range(5):
	for dimensions in listedimensions:
		os.system("inkscape svg/instantbird_wallpaper%s_%s.svg --export-png=png/instantbird_wallpaper%s_%sx%s.png --export-width=%s --export-height=%s" % (a+1, dimensions[0], a+1, dimensions[1], dimensions[2], dimensions[1], dimensions[2]))

print "\nFini !"
