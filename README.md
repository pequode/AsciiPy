# AsciiPy

## Description
This program is a small method that I created in 2019 as part of my programming journey. I was still Learning Python for my job with WRDS at the time and this script was done in parallel with my work to help me get a handle on how to program in `Python`.  

## Purpose
I wanted to familiarize my self with a new language. I also wanted to start learning how to do image processing because that was something I had started to learn as part of my previous internship.

### Goal:
To create a program that would display image files on an ssh connection so that I could get an idea of what the underlying image represented in the absence of a good naming scheme.

### Thanks To:
To accomplish this project I used a stack overflow article explaining the PIL. Unfortunately I did not save the link to give the user proper credit.

## Getting Started
To run this in `Python2.7` you would first run `pip install PIL` then you would `import asciiPic`. However, this module has not been updated for `Python3.*`.
## Example Usage
```
>ls
2021-10-04-190744.jpg asciiPic.py
>python2
Python 2.7.17 (default, Feb 27 2021, 15:10:58)
[GCC 7.5.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import asciiPic
printImgStill(" ","*","2021-10-04-190744.jpg")









                      *******             *******                        
                     *********           *********                       
                     **********         ***********                      
                     **********         **********                       
                      *********           *********                       
                        *****               *****                         


                                                                        *

           ***                                         ***           *  
              **                                       **            *   
                **                                   **             *    
                 ****                            ****                    
                      ****                     ****               *       
                         *********** ***********                *         
                                  ***                        *           
                                                        *              
                                                   *                 
                                           **                     
                                     *                            
```
