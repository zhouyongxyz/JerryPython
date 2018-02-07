from pytesseract import *
import Image
# -*- coding: UTF-8 -*-

def main():
    im = Image.open('fonts_test.png')
    text = image_to_string(im)
    print "Using image_to_string(): "
    print text
#text = image_file_to_string('fonts_test.png', graceful_errors=True)
#print "Using image_file_to_string():"
#print text
if __name__ == "__main__":
    main()