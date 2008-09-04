#!/usr/bin/env python
import os

liste = [["generic-protocol", "generic-protocol_16.svg", "generic-protocol.svg", "generic-protocol.svg"], ["unknown-protocol", "unknown-protocol_16.svg", "unknown-protocol.svg", "unknown-protocol.svg"]]

for sublist in liste:
    os.system("inkscape svg/%s --export-png=png/%s.png --export-width=16 --export-height=16" % (sublist[1], sublist[0]))
    os.system("inkscape svg/%s --export-png=png/%s-32.png --export-width=32 --export-height=32" % (sublist[2], sublist[0]))
    os.system("inkscape svg/%s --export-png=png/%s-48.png --export-width=48 --export-height=48" % (sublist[3], sublist[0]))

os.system("inkscape svg/accountError.svg --export-png=png/accountError.png")

print "Fini !"
