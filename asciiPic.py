# -*- coding: utf-8 -*-
# built for python 2.7
#created in 2019 while the programer was learning python
try:
    from PIL import Image
    from PIL import GifImagePlugin
    import time
except:
    print("proper lib not installed")
    quit()
    pass
#^^^ check for required libs
#wrapper method to handle image still printing
def printImgStill(blackChars,whiteChars,fileN):
    blackChar = blackChars
    whiteChar = whiteChars
    imgFilePath = fileN
    col = Image.open(imgFilePath)
    textOutPut = printImg(blackChar,whiteChar,col)
    print (textOutPut)
#main image printing method
def printImg(blackChars,whiteChars,fileO):
    col = fileO
    h, w = col.size # image dimentions
    basewidth = 75 # the desired text width in chars
    ShinkFact = 0.75# the factor the the image should be scaled down in height.
    wpercent = (basewidth/float(w))# the precentage of the width that the base width is
    hsize = int((float(h)*float(wpercent))*ShinkFact)# the scale of the height
    #scale down
    col = col.resize((basewidth,hsize), Image.ANTIALIAS)
    # get new size
    h, w = col.size
    # make greyscale
    gray = col.convert('L')
    bw = gray.point(lambda x: 0 if x<128 else 255, '1')# performs a threshold for the grayscale
    # gets the pixel array for the threshold image
    px = bw.load()
    text = ""
    for i in range(w): # for every row
        Line =""
        for j in range(h):# for each element of the row
            if int(px[j,i]) == 255:
                Line = Line + whiteChars
            else:
                Line = Line + blackChars
        text = text + Line +"\n"
    return text

# a method for printing greyscale images with shading,doesnt work very well

def printImgWColor(fileO):
    col = fileO
    h, w = col.size # image dimentions
    basewidth = 75 # the desired text width in chars
    ShinkFact = 0.75# the factor the the image should be scaled down in height.
    wpercent = (basewidth/float(w))# the precentage of the width that the base width is
    hsize = int((float(h)*float(wpercent))*ShinkFact)# the scale of the height
    #scale down
    col = col.resize((basewidth,hsize), Image.ANTIALIAS)
    # get new size
    h, w = col.size
    ##^^^ same as printImg

    bw = col.convert('LA')
    px = bw.load()
    text = ""
    #same idea but just add value brackets
    for i in range(w):
        Line =""
        for j in range(h):
            num = px[j,i]
            if int(str(num[0])) > 190:
                Line = Line + MostToLeast[0]
            elif int(str(num[0])) > 180:
                Line = Line + MostToLeast[1]
            elif int(str(num[0])) > 160:
                Line = Line + MostToLeast[2]
            elif int(str(num[0])) > 125:
                Line = Line + MostToLeast[3]
            elif int(str(num[0])) > 100:
                Line = Line + MostToLeast[4]
            elif int(str(num[0])) > 85:
                Line = Line + MostToLeast[5]
            elif int(str(num[0])) > 70:
                Line = Line + MostToLeast[6]
            else:
                Line = Line + MostToLeast[7]

        text = text + Line +"\n"
    return text

def playGif(blackChars,whiteChars,fileN):
    imageObject = Image.open(fileN)
    while True:# plays animation
      for frame in range(0,imageObject.n_frames):# loops through frams in a gif
        imageObject.seek(frame)
        print printImgWColor(imageObject)
        time.sleep(0.2)

# playGif("*"," ","falcon.gif")
