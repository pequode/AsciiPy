# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
try: 
    #import os
    #import sys
    from PIL import Image 
    from PIL import GifImagePlugin
    import time
except: 
    print("proper lib not installed")
    quit()
    pass

def printImgStill(blackChars,whiteChars,fileN):
    blackChar = blackChars
    whiteChar = whiteChars
    imgFilePath = fileN 
    col = Image.open(imgFilePath)
    printImg(blackChar,whiteChar,col)
    
def printImg(blackChars,whiteChars,fileO):
    col = fileO
    h, w = col.size
    basewidth = 75
    ShinkFact = 0.75
    wpercent = (basewidth/float(col.size[0]))
    hsize = int((float(col.size[1])*float(wpercent))*ShinkFact)
    col = col.resize((basewidth,hsize), Image.ANTIALIAS) 
    h, w = col.size
    gray = col.convert('L')
    bw = gray.point(lambda x: 0 if x<128 else 255, '1')
    
    px = bw.load()
    #print(bw.size())
    text = ""
    for i in range(w):
        Line =""
        for j in range(h):
            
            if int(str(px[j,i])) == 255:
                Line = Line + whiteChars
            else:
                Line = Line + blackChars
                
        text = text + Line +"\n"
    print(text)
    
def printImgWColor(fileO):
    MostToLeast = [" "," ",".",".","%","%","#","#"]
    col = fileO
    h, w = col.size
    basewidth = 75
    ShinkFact = 0.75
    wpercent = (basewidth/float(col.size[0]))
    hsize = int((float(col.size[1])*float(wpercent))*ShinkFact)
    col = col.resize((basewidth,hsize), Image.ANTIALIAS) 
    h, w = col.size
    bw = col.convert('LA')
    #bw = gray.point(lambda x: 0 if x<128 else 255, '1')
    
    px = bw.load()
    #print(bw.size())
    text = ""
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
    print(text)
    
def playGif(blackChars,whiteChars,fileN):
    imageObject = Image.open(fileN)
    while True:
      for frame in range(0,imageObject.n_frames):
        imageObject.seek(frame)
        printImgWColor(imageObject)
        #printImg(blackChars,whiteChars,imageObject)
        time.sleep(0.2)

def ifMovie():
    print

playGif("*"," ","falcon.gif")



    



