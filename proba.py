import csv

filename = 'coordinates_of_images/coordinates_of_suits.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]


coor = ('19', 'moeaw')

if coor in data:
    print(data)
    with open(filename, 'a', newline='') as fd:
        writer = csv.writer(fd)
        writer.writerow(coor)