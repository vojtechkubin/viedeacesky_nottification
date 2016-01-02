#!/usr/bin/env python
import urllib2
import re
import ctypes
import Tkinter
import tkMessageBox
import webbrowser
import io
import time
from PIL import Image, ImageTk

#-----------------file exist---------------
def fileexist(nazev):
    try:
        soubor = open(nazev, 'r')
    except IOError:
        return False
    else:
        soubor.close()
        return True
#------------------program------------
def program():
    root = Tkinter.Tk()
    say = ""
    libary = []
    message = []
    buttons = []
    pictures = []
    rating = []
    urls = []
    f = urllib2.urlopen("http://www.videacesky.cz/")
    content = f.read()
#------------------------------------- nazev ----------------------------------
    result = re.findall(ur'title=".*"><span>(.*)(&#\d*)?(.*)<\/span><\/a><\/h2>', content)
#-------------------------------------- hodnoceni----------------------------------
    result2 = re.findall(ur'\d*.*hodnocen.*,.*pr.*m.*r:.*<strong>([\d,\,]*)<\/strong>.*z 10', content)
#--------------------------------------- odkaz, obrazek ------------------------------
    result3 = re.findall(ur'<a href="(http:\/\/www\.videacesky\.cz\/.*)" class=".*"><img src="(http:\/\/img.youtube.com\/.*jpg)".*\/>', content)


    for x in result:
        message.append(re.sub(r'&#\d*;',"", x[0])+ '\n')

    for x in result2:
        rating.append(x[0])

    for x in result3:
        pictures.append(x[1])
        urls.append(x[0])


    if fileexist("videa.txt"):
        soubor = open("videa.txt", 'r')
        seznam = soubor.readlines()
        soubor.close()
    else:
        seznam = message
        
    y=-1
    for row in message:
        y+=1
        if (row in seznam) == False:
            say = ""
            say += row + "rate: " + rating[y] + "/10" + '\n'
            libary.append(say)

    
#-------------print------------------


    if say != "":
        for x in range (len(libary)):
            buttons.append(Tkinter.Button(root, text = libary[x], command = lambda url=urls[x]: webbrowser.open_new_tab(url)))
            buttons[x].pack()
        root.mainloop()
        soubor = open("videa.txt", 'w')
        for x in message:
            soubor.write(x)

    soubor.close()
    
while True:
    program()
    time.sleep(600)



