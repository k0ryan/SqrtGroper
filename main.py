import math, time

number = input("Input the number of which you want to know the square root\n >>> ")
movement1 = 1.01
guess1 = number
guess2 = 1
direction1 = 0
direction2 = 0
done = False

while (done == False):

    guess2 = guess1
    guesspwr = guess1 ** 2
    direction2 = direction1

    if (guesspwr < number):

        guess1 = guess1 * movement1
        direction1 = 0

    if (guesspwr > number):

        guess1 = guess1 / movement1
        direction1 = 1

    if ((guesspwr > number - 0.0001) and (guesspwr < number + 0.0001)):
        done = True

    if (guess1 == guess2):
        done = True

    if (direction1 != direction2):
        movement1 = movement1 / 1.011

    if (direction1 == direction2):
        movement1 = movement1 * 1.011

print guess1
