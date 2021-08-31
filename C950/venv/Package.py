#Benjamin Ekern #000982749
#Overall, the project is O(N ^ 2) time, since that is the worst time complexitiy out of every single method
import csv
import math
from datetime import datetime, timedelta

#Creates instances of datetime to keep track of the time for each truck
truck_1_time = datetime(2020, 5, 8)
truck_2_time = datetime(2020, 5, 8)

#Creates instances of datetime to keep track of when items are loaded onto their respective trucks
loadtime_1 = None
loadtime_2 = None

#Sets the appropriate start times for each truck
truck_1_time = truck_1_time.replace(hour = 9, minute = 5)
truck_2_time = truck_2_time.replace(hour = 8)

#Sets up a class of packages and their attributes/methods
class Package:
    def __init__(self, ID, address, city, state, zip, deadline, weight, notes):
        self.ID = int(ID)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = 'In Hub'
        self.has_not_moved = True
        self.has_been_loaded = False
        self.true_time_delivered = None
        self.time_loaded = None

    #O(1) time
    def get_ID(self):
        return int(self.ID)

    #O(1) time
    def get_address(self):
        return self.address

    #O(1) time
    def get_city(self):
        return self.city

    #O(1) time
    def get_state(self):
        return self.state

    #O(1) time
    def get_zip(self):
        return self.zip

    #O(1) time
    def get_deadline(self):
        return self.deadline

    #O(1) time
    def get_weight(self):
        return self.weight

    #O(1) time
    def get_notes(self):
        return self.notes

    #O(1) time
    def get_status(self):
        return self.status

    #O(1) time
    def get_has_not_moved(self):
        return self.has_not_moved

    #O(1) time
    def get_true_time_delivered(self):
        return self.true_time_delivered

    #O(1) time
    def get_time_loaded(self):
        return self.time_loaded

    #O(1) time
    def set_ID(self, val):
        self.ID = int(val)

    #O(1) time
    def set_address(self, val):
        self.address = val

    #O(1) time
    def set_city(self, val):
        self.city = val

    #O(1) time
    def set_state(self, val):
        self.state = val

    #O(1) time
    def set_zip(self, val):
        self.zip = val

    #O(1) time
    def set_deadline(self, val):
        self.deadline = val

    #O(1) time
    def set_weight(self, val):
        self.weight = val

    #O(1) time
    def set_notes(self, val):
        self.notes = val

    #O(1) time
    def set_status(self, val):
        self.status = val

    #O(1) time
    def set_has_not_moved(self, val):
        self.has_not_moved = val

    #O(1) time
    def set_true_time_delivered(self, val):
        self.true_time_delivered = val

    #O(1) time
    def set_time_loaded(self, val):
        self.time_loaded = val

#Sets up a class of distances between destinations
class Distance:
    def __init__(self, args):
        self.dist = []
        self.address = []

        #O(N) time, goes through each item in loop once
        for each in args:
            if (is_float(each) or each == 'HUB' or each == ''):
                self.dist.append(each)

        #O(N) time, goes through each item in loop once
        for each in args:
            if(not is_float(each) and each != ''):
                self.address.append(each)

    #O(1) time
    def get_dist(self):
        return self.dist

    #O(1) time
    def set_dist(self, args):
        self.dist = args

    #O(1) time
    def get_address(self):
        return self.address

    #O(1) time
    def set_address(self, args):
        self.address = args

#    def get_indexes(self, nextAddress, dict):
#        return self.get_dist()[dict[nextAddress]];

#Creates a class of trucks to deliver packages
class Truck:
    def __init__(self):
        self.package_num = 16
        self.speed = 18
        self.packages = []
        self.current_package = None
        self.delivered_packages = []

    #Returns the average speed of the truck
    #O(1) time
    def get_speed(self):
        return self.speed

    #Returns the number of packages that the truck can carry
    #O(1) time
    def get_package_num(self):
        return self.package_num

    #Gets all packages in truck
    #O(1) time
    def get_packages(self):
        return self.packages

    #Returns all packages that have been delivered
    #O(1) time
    def get_delivered_packages(self):
        return self.delivered_packages

    #Sets package number
    #O(1) time
    def set_package_num(self, val):
        self.package_num = val

    #Adds a package
    #O(1) time
    def add_package(self, val):
        self.packages.append(val)

    #Loads list of packages into truck
    #O(N) time, 2 seperate loops
    def load(self, deliveries, load_time):
        count = 0
        for i in range (0, self.get_package_num()):
            if ((i < len(deliveries)) and (len(self.get_packages()) <= self.get_package_num())):
                deliveries[i].set_status("En route")
                deliveries[i].set_time_loaded(load_time)
                self.add_package(deliveries[i])
                count += 1
        for i in range(0, count):
            deliveries.pop(0)

    #Removes item from truck and stores its data in delivered_packages
    #O(1) time
    def deliver(self, index = 0):
        self.delivered_packages.append(self.packages[index])
        self.packages.pop(index)

    #Pops item
    # O(1) time
    def pop_item(self, index = 0):
        self.packages.pop(index)

    #Swaps indexes, lower index must be placed first
    # O(1) time
    def swap(self, index1, index2):
        temp2 = self.packages.pop(index2)
        temp1 = self.packages.pop(index1)

        self.packages.insert(index1, temp2)
        self.packages.insert(index2, temp1)

#Returns true if a value is an integer
#O(1) time, no looping, only atomic expressions
def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

#Returns true if a value is a float
#O(1) time, no looping, only atomic expressions
def is_float(val):
    try:
        num = float(val)
    except ValueError:
        return False
    return True

#Takes ID as input, returns corresponding package
#O(N) time, goes through list until item is found
def lookup(num):
    for row in deliveries:
        if (int(row.ID) == num):
            return row

#Swaps items within a list, when provided with the list and the 2 indexes that will be swapped
#Note, index 2 should be larger than index 1
#O(1) time, no looping, only atomic expressions
def swap_items(deliveries, index1, index2):
    temp2 = deliveries.pop(index2)
    temp1 = deliveries.pop(index1)

    deliveries.insert(index1, temp2)
    deliveries.insert(index2, temp1)
    return deliveries

#List of packages
deliveries = []

#List of distances between coordinates
distances = []

#Sets up the 2 instances of the truck class
truck_1 = Truck()
truck_2 = Truck()

#Imports PackageFile.csv
#O(N) time, every row is checked once
with open('PackageFile.csv') as packagefile:
    readfile = csv.reader(packagefile, delimiter=',')

    #Gets input from file and saves them into packages
    for row in readfile:
        if (is_int(row[0])):
            deliveries.append(Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

#Creates a list of every package, making is easier to run tests/access all packages efficiently
allPackages = deliveries[:]

#Imports Distancefile.csv
#O(N) time, as each item is checked once
with open('DistanceTable.csv') as distancefile:
    readfile = csv.reader(distancefile, delimiter=',')

    count = 0
    for row in readfile:
        if(count >= 8):
            distances.append(Distance(row))
        count += 1

temp = []
#Converts distances to floats from strings
#O(N ^ 2) time, as there is a for loop within a for loop
for i in range(0, distances.__len__()):
    for j in range(0, distances.__len__()):
        if (distances[i].get_dist()[j] != ''):
            temp.append(float(distances[i].get_dist()[j]))
        else:
            temp.append(distances[i].get_dist()[j])
    distances[i].set_dist(temp[:])
    temp.clear()

#Adds in all empty values
#O(N ^ 2) time, as there is a for loop within a for loop
for i in range(0, distances.__len__()):
    for j in range(0, distances.__len__()):
        temp.append(distances[j].get_dist()[i])
    distances[i].set_dist(temp[:])
    temp.clear()

#Sets up a dictionary linking address to indexes
dict = {"HUB" : 0, "4001 South 700 East" : 0}

#Sets indexes as values in dictionary
#O(N ^ 2) time, as there is a for loop within a for loop
for i in range(0, distances.__len__()):
    for j in range(0, deliveries.__len__()):
        if (deliveries[j].get_address() in distances[i].get_address()[1]):
            dict[deliveries[j].get_address()] = i

#one-to-one mapping
#Creates a hashmap, will be used to keep track of packages and their value
class HashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    #Gets hash number for each method
    #O(1) time
    def get_hash(self, key):
        return (key - 1) % self.size

    #Adds a key and value pair to the map
    #O(1) time
    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                self.map[key_hash].append(key_value)
                return True

    #Returns a key and value pair
    #O(N) time, goes through loop until key is found
    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    #Deletes a key and value pair from the map
    #O(N) time, goes through loop until key is found
    def delete(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    #Prints out every hash
    #O(N) time, checks each item once
    def print(self):
        for pack in self.map:
            if pack is not None:
                print(str(pack))

#Creates an instance of this hashmap
map_of_packages = HashMap()

#Finishes setting up the addresses in distances
#O(N) time, as each item is checked once
for row in distances:
    row.set_address(row.address[1])
#O(N ^ 2) time, as there is a for loop within a for loop
for row in distances:
    for i in deliveries:
        if (i.get_address() in row.get_address()):
            row.set_address(i.get_address())
distances[0].set_address("HUB")

#Makes sure that each special delivery is on the correct truck
#O(1) time for each
swap_items(deliveries, 17, 39)
swap_items(deliveries, 20, 33)
swap_items(deliveries, 1, 6)
swap_items(deliveries, 12, 24)
swap_items(deliveries, 13, 14)
swap_items(deliveries, 8, 38)
swap_items(deliveries, 12, 35)

#THIS IS THE ALGORITHM THAT WILL BE USED
"""Sorts the entire list of deliveries before they are loaded,
the sorting is done via a greedy algorithm
O(N ^ 2) time, based on the for loop within a for loop,
meaning that the algorithm is exponential"""
for i in range(-1, len(deliveries) - 1):
    temp_1 = 0
    temp_2 = 0
    didSwap = False
    min = 20.0
    for j in range(i + 1, len(deliveries) - 1):
        if (i == -1):
            if (distances[dict["HUB"]].get_dist()[dict[deliveries[j].get_address()]] < min):
                min = distances[dict["HUB"]].get_dist()[dict[deliveries[j].get_address()]]
                temp_1 = i
                temp_2 = j
                didSwap = True
        elif (distances[dict[deliveries[i].get_address()]].get_dist()[dict[deliveries[j].get_address()]] < min ):
            min = distances[dict[deliveries[i].get_address()]].get_dist()[dict[deliveries[j].get_address()]]
            temp_1 = i
            temp_2 = j
            didSwap = True
    if (didSwap):
        swap_items(deliveries, temp_1 + 1, temp_2)

#Makes sure that each special delivery is on the correct truck
#O(1) time for each
swap_items(deliveries, 15, 28)
swap_items(deliveries, 27, 39)
swap_items(deliveries, 12, 26)
swap_items(deliveries, 5, 34)
swap_items(deliveries, 25, 34)
swap_items(deliveries, 21, 28)
swap_items(deliveries, 12, 22)
swap_items(deliveries, 31, 37)
swap_items(deliveries, 31, 36)
swap_items(deliveries, 31, 35)

#Load packages onto first trucks
truck_2.load(deliveries, truck_2_time)
truck_1.load(deliveries, truck_1_time)


#Delivers packages and calculates time taken
total_miles = 0
loadtime_1 = truck_1_time


#Sorts packages that are in truck 1
#O(N ^ 2) time, based on the for loop within a for loop,
#meaning that the algorithm is exponential
for i in range(-1, truck_1.get_package_num() - 1):
    temp_1 = 0
    temp_2 = 0
    didSwap = False
    min = 20.0
    for j in range(i + 1, truck_1.get_package_num()):
        if (i == -1):
            if (distances[dict["HUB"]].get_dist()[dict[truck_1.get_packages()[j].get_address()]] < min):
                min = distances[dict["HUB"]].get_dist()[dict[truck_1.get_packages()[j].get_address()]]
                temp_1 = i
                temp_2 = j
                didSwap = True
        elif (distances[dict[truck_1.get_packages()[i].get_address()]].get_dist()[dict[truck_1.get_packages()[j].get_address()]] < min  and \
              truck_1.get_packages()[j].get_has_not_moved()):
            min = distances[dict[truck_1.get_packages()[i].get_address()]].get_dist()[dict[truck_1.get_packages()[j].get_address()]]
            temp_1 = i
            temp_2 = j
            didSwap = True
    if (didSwap):
        truck_1.get_packages()[temp_2].set_has_not_moved(False)
        truck_1.swap(temp_1 + 1, temp_2)

#Sorts package that are in truck 2
#O(N ^ 2) time, based on the for loop within a for loop,
#meaning that the algorithm is exponential
for i in range(-1, truck_2.get_package_num()):
    temp_1 = 0
    temp_2 = 0
    didSwap = False
    priority = False
    min = 20.0
    for j in range(i + 1, truck_2.get_package_num() - 1):
        if (i == -1):
            if (distances[dict["HUB"]].get_dist()[dict[truck_2.get_packages()[j].get_address()]] < min):
                min = distances[dict["HUB"]].get_dist()[dict[truck_2.get_packages()[j].get_address()]]
                temp_1 = i
                temp_2 = j
                didSwap = True
        elif (distances[dict[truck_2.get_packages()[i].get_address()]].get_dist()[dict[truck_2.get_packages()[j].get_address()]] < min):
                min = distances[dict[truck_2.get_packages()[i].get_address()]].get_dist()[dict[truck_2.get_packages()[j].get_address()]]
                temp_1 = i
                temp_2 = j
                didSwap = True
    if(didSwap):
        truck_2.swap(temp_1 + 1, temp_2)

#Delivers packages until truck 1 runs out of them
#O(N) time, loop goes through each item once
while (len(truck_1.get_packages()) >= 0):
    if (len(truck_1.get_packages()) != truck_1.get_package_num() and len(truck_1.get_packages()) != 0):
        total_miles += distances[dict[truck_1.get_delivered_packages()[len(truck_1.get_delivered_packages()) - 1] \
            .get_address()]].get_dist()[dict[truck_1.get_packages()[0].get_address()]]
        truck_1_time += timedelta(hours=distances[dict[truck_1.get_delivered_packages()[len(truck_1.get_delivered_packages()) - 1].get_address()]] \
                                            .get_dist()[dict[truck_1.get_packages()[0].get_address()]] / 18)
        truck_1.get_packages()[0].set_status("Delivered at " + str(truck_1_time.time()))
        truck_1.get_packages()[0].set_true_time_delivered(truck_1_time.time())
        truck_1.deliver()

    elif (len(truck_1.get_packages()) == 0):
        total_miles += distances[dict[truck_1.get_delivered_packages()[len(truck_1.get_delivered_packages()) - 1].get_address()]].get_dist()[dict["HUB"]]
        truck_1_time += timedelta(hours=distances[dict[truck_1.get_delivered_packages()[len(truck_1.get_delivered_packages()) - 1].get_address()]].get_dist()[dict["HUB"]] / 18)
        break

    else:
        total_miles += distances[dict["HUB"]].get_dist()[dict[truck_1.get_packages()[0].get_address()]]
        truck_1_time += timedelta(hours=distances[dict["HUB"]].get_dist()[dict[truck_1.get_packages()[0].get_address()]] / 18)
        truck_1.get_packages()[0].set_status("Delivered at " + str(truck_1_time.time()))
        truck_1.get_packages()[0].set_true_time_delivered(truck_1_time.time())
        truck_1.deliver()

#Delivers packages until truck 2 runs out of them
#O(N) time, loop goes through each item once
while (len(truck_2.get_packages()) >= 0):
    if (len(truck_2.get_packages()) != truck_2.get_package_num() and len(truck_2.get_packages()) != 0):
        total_miles += distances[dict[truck_2.get_delivered_packages()[len(truck_2.get_delivered_packages()) - 1] \
            .get_address()]].get_dist()[dict[truck_2.get_packages()[0].get_address()]]
        truck_2_time += timedelta(hours=distances[dict[truck_2.get_delivered_packages()[len(truck_2.get_delivered_packages()) - 1].get_address()]] \
                                            .get_dist()[dict[truck_2.get_packages()[0].get_address()]] / 18)
        truck_2.get_packages()[0].set_status("Delivered at " + str(truck_2_time.time()))
        truck_2.get_packages()[0].set_true_time_delivered(truck_2_time.time())
        truck_2.deliver()

    elif (len(truck_2.get_packages()) == 0):
        total_miles += distances[dict[truck_2.get_delivered_packages()[len(truck_2.get_delivered_packages()) - 1].get_address()]].get_dist()[dict["HUB"]]
        truck_2_time += timedelta(hours=distances[dict[truck_2.get_delivered_packages()[len(truck_2.get_delivered_packages()) - 1].get_address()]].get_dist()[dict["HUB"]] / 18)
        loadtime_2 = truck_2_time
        break

    else:
        total_miles += distances[dict["HUB"]].get_dist()[dict[truck_2.get_packages()[0].get_address()]]
        truck_2_time += timedelta(hours=distances[dict["HUB"]].get_dist()[dict[truck_2.get_packages()[0].get_address()]] / 18)
        truck_2.get_packages()[0].set_status("Delivered at " + str(truck_2_time.time()))
        truck_2.get_packages()[0].set_true_time_delivered(truck_2_time.time())
        truck_2.deliver()

#Loads truck 2 for the second time, changes the max number of packages to the number it's loaded with
truck_2.load(deliveries, truck_2_time)
truck_2.set_package_num(len(truck_2.get_packages()))

#If time is later than 10:20, package 9's address is changed
#O(N) time, as the for loop will check every package once
at1020am = datetime(2020, 5, 8, hour=10, minute= 20)
for each in truck_2.get_packages():
    if (each.get_ID() == 9 and truck_2_time.time() >= at1020am.time()):
        each.set_address(("410 S State St"))

#Uses greedy algorithm to sort the final truck
#O(N ^ 2) time, based on the for loop within a for loop,
#meaning that the algorithm is exponential
for i in range(-1, truck_2.get_package_num() - 1):
    temp_1 = 0
    temp_2 = 0
    didSwap = False
    min = 20.0
    for j in range(i + 1, truck_2.get_package_num() - 1):
        if(i == -1):
            if(distances[dict["HUB"]].get_dist()[dict[truck_2.get_packages()[j].get_address()]] < min and \
                    truck_2.get_packages()[j].get_has_not_moved()):
                min = distances[dict["HUB"]].get_dist()[dict[truck_2.get_packages()[j].get_address()]]
                temp_1 = i
                temp_2 = j
                didSwap = True
        elif (distances[dict[truck_2.get_packages()[i].get_address()]].get_dist()[dict[truck_2.get_packages()[j].get_address()]] < min and \
                truck_2.get_packages()[i].get_has_not_moved() and truck_2.get_packages()[j].get_has_not_moved()):
            min = distances[dict[truck_2.get_packages()[i].get_address()]].get_dist()[dict[truck_2.get_packages()[j].get_address()]]
            temp_1 = i
            temp_2 = j
            didSwap = True
    if(didSwap):
        truck_2.swap(temp_1 + 1, temp_2)

#Delivers all final packages from truck 2
#O(N) time, loop checks every item once
while (len(truck_2.get_packages()) > 0):
    if (len(truck_2.get_packages()) != truck_2.get_package_num() and len(truck_2.get_packages()) != 0):
        total_miles += distances[dict[truck_2.get_delivered_packages()[len(truck_2.get_delivered_packages()) - 1] \
            .get_address()]].get_dist()[dict[truck_2.get_packages()[0].get_address()]]
        truck_2_time += timedelta(hours=distances[dict[truck_2.get_delivered_packages()[len(truck_2.get_delivered_packages()) - 1].get_address()]] \
                                            .get_dist()[dict[truck_2.get_packages()[0].get_address()]] / 18)
        truck_2.get_packages()[0].set_status("Delivered at " + str(truck_2_time.time()))
        truck_2.get_packages()[0].set_true_time_delivered(truck_2_time.time())
        truck_2.deliver()

    else:
        total_miles += distances[dict["HUB"]].get_dist()[dict[truck_2.get_packages()[0].get_address()]]
        truck_2_time += timedelta(hours=distances[dict["HUB"]].get_dist()[dict[truck_2.get_packages()[0].get_address()]] / 18)
        truck_2.get_packages()[0].set_status("Delivered at " + str(truck_2_time.time()))
        truck_2.get_packages()[0].set_true_time_delivered(truck_2_time.time())
        truck_2.deliver()

#Gets a time from the user; returns the status of all packages at this specific time
#Runs indefinitely
#O(N ^ 2) time since it is a loop within a loop, although this will actually be infinite as the while loop runs forever
print ("Total miles traveled: " + str(round(total_miles)))
while (True):
    user_time = datetime.strptime(input("\n\n\nPlease input time as HH:MM\n\n\n"), "%H:%M")
    for each in allPackages:
        if ( (user_time.time() < loadtime_2.time() and loadtime_2.time() < each.get_true_time_delivered() and truck_2.get_delivered_packages().__contains__(each))  \
                or (user_time.time() < loadtime_1.time() and loadtime_1.time() < each.get_true_time_delivered() and truck_1.get_delivered_packages().__contains__(each))):
            print('ID: '+ str(each.get_ID()) + ", Status: still at the hub" + ", Address: " + each.get_address() + ", Deadline: " + each.get_deadline() + \
                   ", City: " + each.get_city() + ", Zip code: " + each.get_zip() + ", Weight: " + each.get_weight())

        elif (user_time.time() < each.get_true_time_delivered()):
            print ('ID: '+ str(each.get_ID()) + ", Status: en route" + ", Address: " + each.get_address() + ", Deadline: " + each.get_deadline() + \
                   ", City: " + each.get_city() + ", Zip code: " + each.get_zip() + ", Weight: " + each.get_weight())

        else:
            print ('ID: '+ str(each.get_ID()) + ", Status: " + each.get_status() +", Address: " + each.get_address() + ", Deadline: " + each.get_deadline() + \
                   ", City: " + each.get_city() + ", Zip code: " + each.get_zip() + ", Weight: " + each.get_weight())





