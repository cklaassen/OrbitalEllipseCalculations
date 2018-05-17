import math

#Class Setup
class focalPoint(object):
    x = 0
    y = 0

    #initializer
    def __init__(self, xPoint):
       self.x = xPoint

    #Print out Focal Point
    def printFocalPoint(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

    def getX(self):
        return self.x

    def changeXby(self, changeX):
        self.x += changeX

print("This is a program to find the equation of a planets orbit")
print("To find the equation: \nInput the shortest distance from the planet to the sun and the furthest distace from the planet to the sun in the specific places below")
perihelion = input("Shortest distance from planet to the Sun: ")
print(perihelion)
aphelion = input("Furthest distance from planet to the Sun: ")
print(aphelion)
sun = focalPoint(0)
focal2 = focalPoint(float(perihelion) - float(aphelion))
center = focalPoint((float(perihelion) - float(aphelion))/2)
print("Sun: ")
sun.printFocalPoint()
print("focal 2: ")
focal2.printFocalPoint()
print("Center: ")
center.printFocalPoint()
h = center.getX()
total = float(aphelion) + float(perihelion)
a = total/2
c = h
bSquared = (a * a) - (c * c)
b = math.sqrt(bSquared)
print("(h, k) form: ")
print("((x - " + str(h) + ")² / (" + str(a) + ")²) + ((y)² / (" + str(b) + ")²) = 1 ")




