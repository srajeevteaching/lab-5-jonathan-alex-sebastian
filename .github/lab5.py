# Programmers: Jonathan, Sebastian, Alex
# Course: CS151, Dr. Rajeev
# Date: October 21st, 2021
# Lab Number: 5
# Program Inputs: Dimensions of each room, Desired type of flooring
# Program Outputs: Cost of each room, and the total cost

# Finding Area function
def findDimensions(l,w):
    area = l * w
    return area

# Find cost of flooring type per SQ ft
def chooseFlooring(flooring):
    if flooring == "hardwood":
        costPerFt = 1.39
    elif flooring == "carpet":
        costPerFt = 3.99
    elif flooring == "tile":
        costPerFt = 4.99
    else:
        costPerFt = 0
    return costPerFt

def main():
    # Array to store room costs
    roomPrices = []
    # Finding cost per individual room
    room = 1
    while room <= 5:
        # User Inputs
        length = int(input("Enter length of room: "))
        width = int(input("Enter width of room: "))
        flooringChoice = input("Enter your choice of flooring: ").lower().strip()

        # Finding cost of sq ft depending on flooring choice
        flooringPriceSQFT = chooseFlooring(flooringChoice)

        # Finding area of one room
        area = findDimensions(length,width)

        # Finding cost based on flooring choice and area of room
        costOfRoom = flooringPriceSQFT * area
        print("Cost of this room is $%.2f" %costOfRoom)

        # Adding the cost of one room to the array of all rooms
        roomPrices.append(costOfRoom)

        # Updating loop counter
        room += 1

    # Finding total cost for all rooms
    total = sum(roomPrices)
    #print(roomPrices)
    print("\nTotal cost of all rooms is $%.2f" %total)

main()
