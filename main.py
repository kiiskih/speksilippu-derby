import csv
from tkinter import * 
import time
from PIL import Image
from PIL import ImageTk
from datetime import date, timedelta

ALEKSANTERI = "Aleksanteri"
MK1 = "Messukylä I"
MK2 = "Messukylä II"
MK3 = "Messukylä III"
MK4 = "Messukylä IV"
MK5 = "Messukylä V"
TT1 = "Tampere-talo I"
TT2 = "Tampere-talo II"
EVENTS = [ALEKSANTERI, MK1, MK2, MK3, MK4, MK5, TT1, TT2]
QUOTAS = {
    ALEKSANTERI: 450,
    MK1: 160,
    MK2: 160,
    MK3: 160,
    MK4: 160,
    MK5: 160,
    TT1: 400,  # Don't include lippumafia quota.
    TT2: 400  # Don't include lippumafia quota.
}

X1_IDX = 0

DIVIDER = 30

SECS_BETWEEN_DATES = 1
MS_BETWEEN_DATES = SECS_BETWEEN_DATES * 1000  # milliseconds.

MS_BETWEEN_UPDATES = MS_BETWEEN_DATES / DIVIDER  # Aim for 30 fps. 
SECS_BETWEEN_UPDATES = SECS_BETWEEN_DATES / DIVIDER

def readData():
    with open('data/circus_orders.csv', newline='') as csvfile:
        orderData = csv.DictReader(csvfile, delimiter=';')
        retOrderData = {}
        emptyDict = {e: 0 for e in EVENTS}
        runningTotals = {e: 0 for e in EVENTS}
        date = ""
        for order in orderData:
            orderDate = order['Tilauksen päivämäärä']
            if orderDate != date:
                retOrderData[date] = runningTotals.copy()
                date = orderDate
            event = order['Päivämäärä']
            runningTotals[event] += 1
        return retOrderData


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
    displayDate = date(2026, 10, 4)

    dateText = Label(window, text=displayDate.strftime("%d/%m/%Y"), font=("Arial", 100))
    dateText.place(x=725, y=10)

    # Setting the starting positions
    START_POS_X = 100
    START_POS_Y = 300
    concerHallWidth = 85

    aleksanteri = canvas.create_image(START_POS_X, START_POS_Y, image=aleksanteriImage)
    messukyla1 = canvas.create_image(START_POS_X, START_POS_Y + concerHallWidth*1+30, image=messukylaImage)
    messukyla2 = canvas.create_image(START_POS_X, START_POS_Y + concerHallWidth*2+20, image=messukylaImage)
    messukyla3 = canvas.create_image(START_POS_X, START_POS_Y + concerHallWidth*3+20, image=messukylaImage)
    messukyla4 = canvas.create_image(START_POS_X, START_POS_Y + concerHallWidth*4+10, image=messukylaImage)
    messukyla5 = canvas.create_image(START_POS_X, START_POS_Y + concerHallWidth*5+10, image=messukylaImage)
    tamperetalo1 = canvas.create_image(START_POS_X, START_POS_Y + concerHallWidth*6+10, image=tamperetaloImage)
    tamperetalo2 = canvas.create_image(START_POS_X, START_POS_Y + concerHallWidth*7+10, image=tamperetaloImage)
    CANVAS_IMAGES = {
        ALEKSANTERI: aleksanteri,
        MK1: messukyla1,
        MK2: messukyla2,
        MK3: messukyla3,
        MK4: messukyla4,
        MK5: messukyla5,
        TT1: tamperetalo1,
        TT2: tamperetalo2
    }
    window.update()

    #Defining the length of track
    TRACK_LENGTH = 1750
    lengthOfTenth = 175

    # Read the data
    orderData = readData()

    previousDayTotals = {e: 0 for e in EVENTS}
    while True:
        # time.sleep(1)
        displayDate = displayDate + timedelta(days = 1)
        dateText.config(text=displayDate.strftime("%d/%m/%Y"))
        dtStr = displayDate.isoformat()
        if displayDate >= date.today():
            print("Current date reached!")
            break

        if dtStr not in orderData:
            # No sales for the given day.
            print(f"No sales in {dtStr}")
            window.update()
            continue

        print("")
        newXPositions = {e: START_POS_X + (TRACK_LENGTH / QUOTAS[e]) * orderData[dtStr][e] for e in EVENTS}
        xDeltas = {e: (START_POS_X + (TRACK_LENGTH / QUOTAS[e]) * orderData[dtStr][e]) - canvas.coords(CANVAS_IMAGES[e])[X1_IDX] for e in EVENTS}
        print(f"newXPositions: {newXPositions}")
        print(f"xDeltas: {xDeltas}")
        # for event in EVENTS:
        #     print(canvas.coords(CANVAS_IMAGES[event])[X1_IDX])
        for timeStep in range(0, MS_BETWEEN_DATES, int(MS_BETWEEN_UPDATES)):
            print(f"{dtStr}: Step {timeStep}")
            for event in EVENTS:
                currentCoords = canvas.coords(CANVAS_IMAGES[event])
                newX = currentCoords[X1_IDX] + (xDeltas[event] / DIVIDER)
                canvas.moveto(CANVAS_IMAGES[event], x=(newX - 50))
                print(f"  {event} newX: {newX}, step: {xDeltas[event] / DIVIDER}, currentX1: {currentCoords[X1_IDX]}")
            window.update() 
            time.sleep(SECS_BETWEEN_UPDATES)
        previousDayTotals = orderData[dtStr]

    window.mainloop()

animation()

