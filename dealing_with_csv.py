import csv


def dealer_csv(max_val):
    filename = 'coordinates_of_images/coordinates_of_dealer.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

        x, y = max_val
        coor = [str(x), str(y)]

        if coor not in data:
            with open(filename, 'a', newline='') as fd:
                writer = csv.writer(fd)
                writer.writerow(coor)


def cards_csv(max_val):
    filename = 'coordinates_of_images/coordinates_of_cards.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

        x, y = max_val
        coor = [str(x), str(y)]
        print('coordinata:', coor)

        if coor not in data:
            with open(filename, 'a', newline='') as fd:
                writer = csv.writer(fd)
                writer.writerow(coor)


def suits_csv(max_val):
    filename = 'coordinates_of_images/coordinates_of_suits.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

        x, y = max_val
        coor = [str(x), str(y)]

        if coor not in data:
            print(data)
            with open(filename, 'a', newline='') as fd:
                writer = csv.writer(fd)
                writer.writerow(coor)