#encoding =utf-8

import os
from PIL import Image

#设置常量，程序更加易读
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
LOGO_SIZE = 80

logoIm = Image.open(LOGO_FILENAME)
logoIm = logoIm.resize((LOGO_SIZE, LOGO_SIZE))
logoWidth, logoHeight = logoIm.size

#Loop over all files in the working directory
os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png')
            or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size

    #Check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        #Calculate the new width and heigth resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

    #Resize the image.
    print('Resizing %s...' % (filename))
    im = im.resize((width, height))

    #in a 300*300 square, and adds catlogo.png to the lower-right corner

    #Add the logo.
    
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    #Save changes
    im.save(os.path.join('withLogo', filename))
