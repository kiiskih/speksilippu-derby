import csv

def readData():
    with open('data/circus_orders.csv', newline='') as csvfile:
        orderData = csv.DictReader(csvfile, delimiter=';')
        for row in orderData:
            print(f'{row['Tilauksen päivämäärä']} {row['Päivämäärä']}')
        return orderData

orderData = readData()
