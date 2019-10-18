from pygameframe import framer

frame = framer()

while True:
    img = frame.frameread()
    frame.imshowrgb(img)