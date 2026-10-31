import csv
from tkinter import *
import time
from PIL import Image
from PIL import ImageTk

def readData():
    with open('data/circus_orders.csv', newline='') as csvfile:
        orderData = csv.DictReader(csvfile, delimiter=';')
        for row in orderData:
            print(f'{row['Tilauksen päivämäärä']} {row['Päivämäärä']}')
        return orderData


#readData()

def animation():

    window = Tk()

    WIDTH = 2000
    HEIGHT = 1000

    frame=Frame(window,width=WIDTH,height=HEIGHT)
    frame.pack(expand = True, fill=BOTH)
    canvas = Canvas(frame,width=WIDTH,height=HEIGHT)
    canvas.pack(expand = True, fill = BOTH)

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
    concerHallWidth = 75

    aleksanteri = canvas.create_image(100,StartingPosition, image=aleksanteriImage)
    messukyla1 = canvas.create_image(100,StartingPosition+concerHallWidth*1, image=messukylaImage)
    messukyla2 = canvas.create_image(100,StartingPosition+concerHallWidth*2, image=messukylaImage)
    messukyla3 = canvas.create_image(100,StartingPosition+concerHallWidth*3, image=messukylaImage)
    messukyla4 = canvas.create_image(100,StartingPosition+concerHallWidth*4, image=messukylaImage)
    messukyla5 = canvas.create_image(100,StartingPosition+concerHallWidth*5, image=messukylaImage)
    tamperetalo1 = canvas.create_image(100,StartingPosition+concerHallWidth*6, image=tamperetaloImage)
    tamperetalo2= canvas.create_image(100,StartingPosition+concerHallWidth*7, image=tamperetaloImage)
    
    window.update()

    while True:
        time.sleep(3)
        canvas.move(aleksanteri, 10, 0)
        canvas.move(messukyla1, 200, 0)
        canvas.move(messukyla2, 100, 0)
        canvas.move(messukyla3, 50, 0)
        canvas.move(messukyla4, 10, 0)
        canvas.move(messukyla5, 100, 0)
        canvas.move(tamperetalo1, 100, 0)
        canvas.move(tamperetalo2, 100, 0)
        window.update()
           

    window.mainloop()
    
orderData = readData()
animation()

