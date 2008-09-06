#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

listedimensions=[16, 22, 24, 32, 48, 64, 125, 128]
listexpm=[16, 48]
listedimensions2=[16, 32, 48]

for dimension in listedimensions:
	if dimension == 16:
		os.system("inkscape svg/instantbird_16.svg --export-png=png/instantbird_%s.png --export-width=%s --export-height=%s" % (dimension, dimension, dimension))
	else:
		os.system("inkscape svg/instantbird.svg --export-png=png/instantbird_%s.png --export-width=%s --export-height=%s" % (dimension, dimension, dimension))

for dimension in listexpm:
	if dimension == 16:
		os.system("inkscape svg/instantbird_dur_16.svg --export-png=xpm/instantbird_%s.png --export-width=%s --export-height=%s" % (dimension, dimension, dimension))
	else:
		os.system("inkscape svg/instantbird_dur.svg --export-png=xpm/instantbird_%s.png --export-width=%s --export-height=%s" % (dimension, dimension, dimension))
	
	os.system("convert xpm/instantbird_%s.png xpm/instantbird_%s.xpm" % (dimension, dimension))
	os.system("rm xpm/instantbird_%s.png" % dimension)

for dimension in listedimensions2:
	os.system("inkscape svg/blist.svg --export-png=png/blist_%s.png --export-width=%s --export-height=%s" % (dimension, dimension, dimension))
	
	if dimension == 16:
		os.system("inkscape svg/conv_16.svg --export-png=png/conv_%s.png --export-width=%s --export-height=%s" % (dimension, dimension, dimension))
	else:
		os.system("inkscape svg/conv.svg --export-png=png/conv_%s.png --export-width=%s --export-height=%s" % (dimension, dimension, dimension))


os.system("inkscape svg/instantbird-logo.svg --export-png=png/instantbird-logo.png")
os.system("inkscape svg/instantbird-logo.svg --export-png=png/instantbird-logo_petit.png --export-width=128 --export-height=136")

print "\nFini !"
