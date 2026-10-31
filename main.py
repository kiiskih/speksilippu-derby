import csv
from tkinter import *
import time
from PIL import Image
from PIL import ImageTk

#def readData():
#    with open('data/circus_orders.csv', newline='') as csvfile:
#        orderData = csv.DictReader(csvfile, delimiter=';')
#        for row in orderData:
#            print(f'{row['Tilauksen päivämäärä']} {row['Päivämäärä']}')
#        return orderData


#readData()

def animation():

    window = Tk()

    WIDTH = 2000
    HEIGHT = 1000

    frame=Frame(window,width=WIDTH,height=HEIGHT)
    frame.pack(expand = True, fill=BOTH)
    canvas = Canvas(frame,width=WIDTH,height=HEIGHT)
    canvas.pack(expand = True, fill = BOTH)

    backgroundImage = Image.open("background.png")
    #backgroundImage = backgroundImage.resize((3550,700))
    backgroundImage = ImageTk.PhotoImage(backgroundImage)

    messukylaImage = Image.open("MK.png")
    messukylaImage = messukylaImage.resize((100,50))
    messukylaImage = ImageTk.PhotoImage(messukylaImage)

    tamperetaloImage = Image.open("TT.png")
    tamperetaloImage = tamperetaloImage.resize((100,50))
    tamperetaloImage = ImageTk.PhotoImage(tamperetaloImage)
  
    aleksanteriImage = Image.open("A.png")
    aleksanteriImage = aleksanteriImage.resize((100,50))
    aleksanteriImage = ImageTk.PhotoImage(aleksanteriImage)
  
    StartingPosition = 300
    concerHallWidth = 85

    background = canvas.create_image(1000,600, image=backgroundImage)
    aleksanteri = canvas.create_image(100,StartingPosition, image=aleksanteriImage)
    messukyla1 = canvas.create_image(100,StartingPosition+concerHallWidth*1+40, image=messukylaImage)
    messukyla2 = canvas.create_image(100,StartingPosition+concerHallWidth*2+30, image=messukylaImage)
    messukyla3 = canvas.create_image(100,StartingPosition+concerHallWidth*3+20, image=messukylaImage)
    messukyla4 = canvas.create_image(100,StartingPosition+concerHallWidth*4+10, image=messukylaImage)
    messukyla5 = canvas.create_image(100,StartingPosition+concerHallWidth*5+10, image=messukylaImage)
    tamperetalo1 = canvas.create_image(100,StartingPosition+concerHallWidth*6+10, image=tamperetaloImage)
    tamperetalo2= canvas.create_image(100,StartingPosition+concerHallWidth*7+20, image=tamperetaloImage)
    
    window.update()

    lengthOfTenth = 175
    
    while True:
        time.sleep(30)

        canvas.move(aleksanteri, lengthOfTenth*1, 0)
        canvas.move(messukyla1, lengthOfTenth*2, 0)
        canvas.move(messukyla2, lengthOfTenth*3, 0)
        canvas.move(messukyla3, lengthOfTenth*4, 0)
        canvas.move(messukyla4, lengthOfTenth*5, 0)
        canvas.move(messukyla5, lengthOfTenth*6, 0)
        canvas.move(tamperetalo1, lengthOfTenth*7, 0)
        canvas.move(tamperetalo2, lengthOfTenth*8, 0)
        window.update()
           

    window.mainloop()

#orderData = readData()
animation()

