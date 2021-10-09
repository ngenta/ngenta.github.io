import csv
def get_info():
    dict = {}
    with open(r'/Users/manue/OneDrive/Escritorio/datapartidos.csv', newline='') as file:
        reader = csv.reader(file, delimiter = ',')
        dict = {rows[0]:rows[1] for rows in reader}
        print(dict)   
get_info() 


