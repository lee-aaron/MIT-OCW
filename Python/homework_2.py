import math
import random

def getDegrees(rad):
    return rad * 180 / math.pi

def getRadians(deg):
    return deg / 360.0 * 2 * math.pi

def isDivisible(m, n):
    return m % n == 0

def rollDice(s,r):
    for i in range(1,r):
        print int(s * random.random() + 0.5)

print getDegrees(3 * math.pi/2)
print getRadians(270)
print isDivisible(6,3)
print isDivisible(7,3)
rollDice(6,6)
