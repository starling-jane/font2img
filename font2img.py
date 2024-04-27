import fontforge
import wordlist
import sys

if len(sys.argv) > 1:
    fontfile = sys.argv[1]
else:
    print("usage: python3 font2img.py (input file) (output path) (output format) (pixel size)")
    print("if not provided, output path will default to ./out, output format will default to .svg")

if len(sys.argv) > 2:
    out_path = sys.argv[2]
else:
    out_path = "out"
if len(sys.argv) > 3:
    out_format = sys.argv[3]
else:
    out_format = "svg"
if len(sys.argv) > 4:
    pixel_size = int(sys.argv[4])
else:
    pixel_size = -1

font = fontforge.open(fontfile)
for unicode in wordlist.words.keys():
    g = font.createChar(unicode)
    if pixel_size > -1:
        g.export(out_path+"/"+wordlist.words[unicode]+"."+out_format, pixelsize=pixel_size)
    else:
        g.export(out_path+"/"+wordlist.words[unicode]+"."+out_format)
