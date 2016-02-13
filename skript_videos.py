#!/usr/bin/env python
import urllib2
import re
import Tkinter
import webbrowser
import time


def fileexist(nazev):
    try:
        soubor = open(nazev, 'r')
    except IOError:
        return False
    else:
        soubor.close()
        return True


def main():
    say = ""
    libary = []
    message = []
    buttons = []
    pictures = []
    rating = []
    urls = []

    f = urllib2.urlopen("http://www.videacesky.cz/")
    content = f.read()
    titles = re.findall(ur'title=".*"><span>(.*)(&#\d*)?(.*)<\/span><\/a><\/h2>', content)
    evaluvations = re.findall(ur'\d*.*hodnocen.*,.*pr.*m.*r:.*<strong>([\d,\,]*)<\/strong>.*z 10', content)
    linksAndPictures = re.findall(ur'<a href="(http:\/\/www\.videacesky\.cz\/.*)" class=".*"><img src="(http:\/\/.*jpg)".*\/>', content)

    for x in titles:
        message.append(re.sub(r'&#\d*;', "", x[0]) + '\n')

    for x in evaluvations:
        rating.append(x[0])

    for x in linksAndPictures:
        pictures.append(x[1])
        urls.append(x[0])

    if fileexist("videa.txt"):
        soubor = open("videa.txt", 'r')
        seznam = soubor.readlines()
        soubor.close()
    else:
        seznam = message

    y = -1
    for row in message:
        y += 1
        if (row in seznam) is False:
            say = ""
            say += row + "rate: " + rating[y] + "/10" + '\n'
            libary.append(say)

#-------------print------------------

    if say != "":
        root = Tkinter.Tk()
        root.wm_title("Videa_Links:")
        for x in range(len(libary)):
            buttons.append(Tkinter.Button(root, text=libary[x], command=lambda url=urls[x]: webbrowser.open_new_tab(url)))
            buttons[x].pack()
        root.mainloop()
        soubor = open("videa.txt", 'w')
        for x in message:
            soubor.write(x)

    soubor.close()

while True:
    main()
    time.sleep(600)
