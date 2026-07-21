from math import dist

totalCenters = int(input("Enter number of points: "))

if totalCenters < 1 or totalCenters > 100:
    print("Invalid input")
    exit()

centerList = []

for i in range(totalCenters):
    name = input("Center name: ")
    xPoint = int(input("x point: "))
    yPoint = int(input("y point: "))

    if xPoint < 1 or xPoint > 1000 or yPoint < 1 or yPoint > 1000:
        print("Invalid input")
        exit()

    centerList.append((name, xPoint, yPoint))

print("Enter Last line value")

targetX = int(input("x point: "))
targetY = int(input("y point: "))

if targetX < 1 or targetX > 1000 or targetY < 1 or targetY > 1000:
    print("Invalid input")
    exit()

nearestCenter = ""
minimumDistance = None

for center in centerList:
    currentDistance = dist((center[1], center[2]), (targetX, targetY))

    if minimumDistance is None or currentDistance < minimumDistance:
        minimumDistance = currentDistance
        nearestCenter = center[0]

print(nearestCenter)