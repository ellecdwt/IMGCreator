# Created by Laura DeWitt Copyright © 2013
#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
fields = 'Current Path', 'Destination Path'
names = []


def saveDir(entries):
    saveto = filedialog.askdirectory()
    entries[0][1].insert(0,str(saveto))

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries

def submit(entries):
    path = entries[0][1].get()
    end = entries[1][1].get()
    try:
        names = os.listdir(path)
    except:
        messagebox.showinfo("Error", "Invalid Path. Please Re-enter")
        entries[0][1].delete(0,END)
        return;
        
    with open('yourcode.txt', 'a') as newFile:
        newFile.write('<div class="highslide-gallery">\n<ul>\n')
        for item in names:
            newFile.write('<li><a class="highslide" href="'+ end + "/Large/" + item +'" onclick="return hs.expand(this, config1 )" title=""><img alt="" src="'+ end + "/Small/" + item +'" /> </a></li>\n')
        newFile.write('</ul>\n</div>')
    entries[0][1].delete(0,END)
    entries[1][1].delete(0,END)
    

if __name__ == '__main__':
    root = Tk()
    root.title("IMG Creator")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Submit', command=(lambda e=ents: submit(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Browse Dir...', command=(lambda e=ents: saveDir(e)))
    b3.pack(side=RIGHT, padx=5, pady=5)

    root.mainloop()
