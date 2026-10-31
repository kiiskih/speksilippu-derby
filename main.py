import csv

def readData():
    with open('data/circus_orders.csv', newline='') as csvfile:
        orderReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        orderData = {}
        for row in orderReader:
            print(', '.join(row))


readData()

