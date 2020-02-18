# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:20:22 2020

@author: dell
"""

import sys
import tkinter as tk

def callGUI():
    def makeThePDF():
        a = nameContent.get()
        b = dobContent.get()
        c = hsContent.get()
        d = hsMarkContent.get()
        e = cgpaContent.get()
        f = phoneContent.get()
        g = emailContent.get()
        print(a)
        print(b)
        print(c)



    def startThis():
        a = vara.get()
        sys.stdout.write(str(a))
        exit(0)

    def updateTheGUI():
        sys.stdout.write(str(updateReturnVal))
        exit(0)

    root = tk.Tk()
    root.title("CV maker")

    namelabel = tk.Label(root, text="Name  : ",font=('Algerian',16,'bold')).grid(row = 0,column = 0)
    nameContent=tk.StringVar()
    nameEntryField = tk.Entry(root, textvariable = nameContent).grid(row = 0,column = 1)
    
    dobLabel = tk.Label(root, text="D.O.B  : ",font=('Algerian',16,'bold')).grid(row = 1,column = 0)
    dobContent=tk.StringVar()
    dobEntryField = tk.Entry(root, textvariable = dobContent).grid(row = 1,column = 1)
    
    hsLabel = tk.Label(root, text="High School Name  : ",font=('Algerian',16,'bold')).grid(row = 2,column = 0)
    hsContent=tk.StringVar()
    hsEntryField = tk.Entry(root, textvariable = hsContent).grid(row = 2,column = 1)
    
    hsMarkLabel = tk.Label(root, text="High School Marks : ",font=('Algerian',16,'bold')).grid(row = 3,column = 0)
    hsMarkContent=tk.StringVar()
    hsMarkEntryField = tk.Entry(root, textvariable = hsMarkContent).grid(row = 3,column = 1)
    
    cgpaLabel = tk.Label(root, text="Agg CGPA : ",font=('Algerian',16,'bold')).grid(row = 4,column = 0)
    cgpaContent=tk.StringVar()
    cgpaEntryField = tk.Entry(root, textvariable = cgpaContent).grid(row = 4,column = 1)
    
    phoneLabel = tk.Label(root, text="Contact NO : ",font=('Algerian',16,'bold')).grid(row = 5,column = 0)
    phoneContent=tk.StringVar()
    phoneEntryField = tk.Entry(root, textvariable = phoneContent).grid(row = 5,column = 1)
     
    emailLabel =  tk.Label(root, text="Email : ",font=('Algerian',16,'bold')).grid(row = 6,column = 0)
    emailContent=tk.StringVar()
    emailEntryField = tk.Entry(root, textvariable = emailContent).grid(row = 6,column = 1)
     

    makeIt = tk.Button(root, text="    START WIH THESE DETAILS    ", fg="blue",font=('Californian FB',18,'bold'), command=makeThePDF).grid(row = 7,column = 1)
    quitButton = tk.Button(root, text="QUIT", fg="red",font=('Californian FB',18,'bold'), command=quit).grid(row = 7,column = 0)

    root.mainloop()



if __name__ == "__main__":
    callGUI()
