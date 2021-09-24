import sys

class Parking_lot:
    def __init__(self, space):
        self.space = space
        self.lot = [None] * space
        print("Created parking of %d slots" % (space))
        self.filled = 0

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

    def slots_with_age(self, age):
        ans = []
        for i in range(self.space):
            if self.lot[i] != None and self.lot[i][1] == age:
                ans.append(i + 1)
        if len(ans) == 0:
            print("No driver here with age %d" % (age))
        else:
            print(*ans)

    def slots_with_reg_no(self, car):
        for i in range(self.space):
            if self.lot[i] != None and self.lot[i][0] == car:
                print(i + 1)
                break
        else:
            print(
                "Car with vehicle registration number %s is not parked here" %(car))

    def registration_no_with_age(self, age):
        ans = []
        for i in range(self.space):
            if self.lot[i] != None and self.lot[i][1] == age:
                ans.append(self.lot[i][0])

        print(*ans)

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


with open('input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]
sys.stdout = open('output.txt', 'w')

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
sys.stdout.close()
