import csv


def dealer_csv(max_loc):
    """

    :param max_val: tuple of coordinates got out of
            res = cv.matchTemplate(img_table, temp_suit, cv.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res). If these coordinates arent already in filenam,
            func adds new ones in
    :return: None, saves new coordinates in filename
    """
    filename = 'coordinates_of_images/coordinates_of_dealer.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

        x, y = max_loc
        coor = [str(x), str(y)]

        if coor not in data:
            with open(filename, 'a', newline='') as fd:
                writer = csv.writer(fd)
                writer.writerow(coor)


def cards_csv(max_loc):
    """

        :param max_val: tuple of coordinates got out of
                res = cv.matchTemplate(img_table, temp_suit, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res). If these coordinates arent already in filenam,
                func adds new ones in
        :return: None, saves new coordinates in filename
        """
    filename = 'coordinates_of_images/coordinates_of_cards.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

        x, y = max_loc
        coor = [str(x), str(y)]
        print('coordinata:', coor)

        if coor not in data:
            with open(filename, 'a', newline='') as fd:
                writer = csv.writer(fd)
                writer.writerow(coor)


def suits_csv(max_loc):
    """

        :param max_val: tuple of coordinates got out of
                res = cv.matchTemplate(img_table, temp_suit, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res). If these coordinates arent already in filenam,
                func adds new ones in
        :return: None, saves new coordinates in filename
        """
    filename = 'coordinates_of_images/coordinates_of_suits.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

        x, y = max_loc
        coor = [str(x), str(y)]

        if coor not in data:
            print(data)
            with open(filename, 'a', newline='') as fd:
                writer = csv.writer(fd)
                writer.writerow(coor)



def money_csv(max_loc):
    """

    :param max_val: tuple of coordinates got out of
            res = cv.matchTemplate(img_table, temp_suit, cv.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res). If these coordinates arent already in filenam,
            func adds new ones in
    :return: None, saves new coordinates in filename
    """
    filename = 'coordinates_of_images/coordinates_of_money.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

        x, y = max_loc
        coor = [str(x), str(y)]

        if coor not in data:
            with open(filename, 'a', newline='') as fd:
                writer = csv.writer(fd)
                writer.writerow(coor)


def number_of_coordinates(csv_file):
    """
    func counts number of coordinates (rows) in csv_file
    :param csv_file: path of file
    :return: number of rows (coordinates)
    """
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        return len(data)