# Class Parking_lot
class Parking_lot:

    def __init__(self, space):
        self.space = space  # The space to be allocated to the lot
        self.lot = [None] * space # An array of size space to store the details of the parking lot
        print("Created parking of %d slots" % (space))
        self.filled = 0  # To keep track of the filled slots

# Function to park the car in the parking lot
    def park(self, car, age): 
        if self.filled == self.space:
            print("Parking lot is Full")
        else:
            nearest = -1
            for i in range(self.space):
                if self.lot[i] == None:
                    nearest = i
                    break
            if nearest != -1:
                self.lot[nearest] = (car, age)
                self.filled += 1
                print(
                    "Car with vehicle registration number %s has been parked at slot number %d"
                    % (car, nearest + 1))
            else:
                print("Parking lot is Full")

# Function to return Slot numbers of all slots where cars of drivers of a particular age are parked.
    def slots_with_age(self, age): 
        ans = []
        for i in range(self.space):
            if self.lot[i] != None and self.lot[i][1] == age:
                ans.append(i + 1)
        if len(ans) == 0:
            print("No driver here with age %d" % (age))
        else:
            print(*ans)

# Function to return Slot numbers in which a car with a given vehicle registration plate is parked.
    def slots_with_reg_no(self, car): 
        for i in range(self.space):
            if self.lot[i] != None and self.lot[i][0] == car:
                print(i + 1)
                break
        else:
            print(
                "Car with vehicle registration number %s is not parked here" %(car))

# Function to return Vehicle Registration numbers for all cars which are parked by the driver of a certain age.
    def registration_no_with_age(self, age):
        ans = []
        for i in range(self.space):
            if self.lot[i] != None and self.lot[i][1] == age:
                ans.append(self.lot[i][0])

        print(*ans)

# Function to vacate the slot
    def leave(self, slot):
        if self.lot[slot - 1] == None:
            print("Slot %d is vacant" % (slot))
        else:
            car = self.lot[slot - 1][0]
            age = self.lot[slot - 1][1]
            self.lot[slot - 1] = None
            self.filled -= 1
            print(
                "Slot number %d vacated, the car with vehicle registration number %s left the space, the driver of the car was of age %d"
                % (slot, car, age))

# Reading the input from input.txt
with open('input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]


for i in range(len(input_lines)):
    if i == 0:
        spaces = input_lines[i].split()
        obj = Parking_lot(int(spaces[1]))
    else:
        query = input_lines[i].split()
        if query[0] == "Park":
            obj.park(query[1], int(query[3]))
        elif query[0] == "Slot_numbers_for_driver_of_age":
            obj.slots_with_age(int(query[1]))
        elif query[0] == "Slot_number_for_car_with_number":
            obj.slots_with_reg_no(query[1])
        elif query[0] == "Leave":
            obj.leave(int(query[1]))
        elif query[0] == "Vehicle_registration_number_for_driver_of_age":
            obj.registration_no_with_age(int(query[1]))

