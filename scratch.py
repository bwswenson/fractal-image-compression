from PIL import Image

infile = r"Jerry_Rice.jpg"
im = Image.open(infile)

size = (128, 128)
resized_im = im.thumbnail(size)

outfile = r"resized.jpg"
im.save(outfile, "JPEG")

import os

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r