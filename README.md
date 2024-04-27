# font2img

this is a simple python script that will take a sitelen pona font and turn every glyph into an individual image. please note this will only work if the font has UCSUR support.

```
python3 font2img.py (input file) (output path) (output format) (pixel size)
```

the input file is required and should point to the font file to be converted. output path will default to the subdirectory "out" within the current working path. output format will default to .svg, which doesn't use pixel size. if you specify an non-vector output format, you'll need to specify a pixel size.

wordlist.py is a python dictionary based on UCSUR.txt, which is indexed by unicode codepoints and contains the names of the glyphs. this is used by font2img.py in creating the names of the files. you can comment out words you don't want, or add codepoints for ones you do.
