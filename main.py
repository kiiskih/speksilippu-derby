import csv
from tkinter import * 
import time
from PIL import Image
from PIL import ImageTk
from datetime import datetime
from datetime import timedelta

#def readData():
#    with open('data/circus_orders.csv', newline='') as csvfile:
#        orderData = csv.DictReader(csvfile, delimiter=';')
#        for row in orderData:
#            print(f'{row['Tilauksen päivämäärä']} {row['Päivämäärä']}')
#        return orderData


#readData()

def loadImage(path, x = None, y = None):
    image = Image.open(path)
    if (x != None and y != None):
        image = image.resize((x,y))
    image = ImageTk.PhotoImage(image)
    return image

    
def animation():

    # Initiating the canvas
    window = Tk()

    WIDTH = 2000
    HEIGHT = 1000

    frame=Frame(window,width=WIDTH,height=HEIGHT)
    frame.pack(expand = True, fill=BOTH)
    canvas = Canvas(frame,width=WIDTH,height=HEIGHT)
    canvas.pack(expand = True, fill = BOTH)

    # loading the images
    backgroundImage = loadImage("background.png")
    messukylaImage = loadImage("MK.png", 100, 50)
    tamperetaloImage = loadImage("TT.png", 100, 50)
    aleksanteriImage = loadImage("A.png", 100, 50)
    
    #Adding the background and date text
    background = canvas.create_image(1000,600, image=backgroundImage)

    # Start date of ticket sale
    date = datetime(2026, 10, 1) 

    dateText = Label(window, text=date.strftime("%d/%m/%Y"), font=("Arial", 100))
    dateText.place(x=725, y=10)

    #Setting the starting positions
    StartingPosition = 300
    concerHallWidth = 85


    aleksanteri = canvas.create_image(100,StartingPosition, image=aleksanteriImage)
    messukyla1 = canvas.create_image(100,StartingPosition+concerHallWidth*1+30, image=messukylaImage)
    messukyla2 = canvas.create_image(100,StartingPosition+concerHallWidth*2+20, image=messukylaImage)
    messukyla3 = canvas.create_image(100,StartingPosition+concerHallWidth*3+20, image=messukylaImage)
    messukyla4 = canvas.create_image(100,StartingPosition+concerHallWidth*4+10, image=messukylaImage)
    messukyla5 = canvas.create_image(100,StartingPosition+concerHallWidth*5+10, image=messukylaImage)
    tamperetalo1 = canvas.create_image(100,StartingPosition+concerHallWidth*6+10, image=tamperetaloImage)
    tamperetalo2= canvas.create_image(100,StartingPosition+concerHallWidth*7+10, image=tamperetaloImage)
    
    window.update()

    #Defining the length of track
    lengthOfTenth = 175

    #TBD: read the data
    #orderData = readData()

    while True:
        time.sleep(5)
        date = date+timedelta(days = 1)
        dateText.config(text=date.strftime("%d/%m/%Y"))
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

animation()

