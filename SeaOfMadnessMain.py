#This is the sea of madness horror game
import time
import sys

Sanity = 0
Health = 100

while True:
    print("The Sea of Madness")
    userStart = input("Please enter start to start the game, or escape to quit: \n")
    if userStart.lower() == "start":
        print ("\nWelcome to the Sea of Madness")
        break
    elif userStart.lower() == "escape":
        print("Closing Game")
        sys.exit()
    else:
        print("Incorrect Input")
time.sleep(2)
print("In the mining town of Ishimura, most of the habitants are miners who work for the Hyperion Corporation")
time.sleep(3)
print(" \nYou are no different. . .")
characterName = input("What is your name? ")
time.sleep(3)
print("You lie in bed, staring at the white ceiling of your dormitory. One of your colleagues, Scott, walks in.")
print("\n\"Hey",characterName,"it's time to get up\"")
time.sleep(2)
while True:
    getUp = input("Do you get up? Y/N")
    if getUp.upper() == "Y":
        print("Alright, we're already late, get your gear and let's get to the mines")
        break
    elif getUp.upper() == "N":
        print("Hey jackass, do you want to get fired? Let's go.")
    else: 
        print("What is that supposed to mean?")

print("You grab your mining helmet, hand-drill, uniform, and head to the elevator.")
time.sleep(3)
print("You walk by workers coming back to the dormitory from the night shift, they have a blank stare in their eyes.")
print("")
time.sleep(3)
print("As you find your seat in the elevator, Scott sits next to you.")
print("\"Hey",characterName,", I've been having nightmares about the mines.")
time.sleep(3)
while True:
    answer1 = input("Enter number for your response \n1.Laugh it off\n2.Inquire about his nightmares ")
    time.sleep(3)
    if answer1 == "1":
        print("Alright. . . nevermind, forget I said anything")
        break
    elif answer1 == "2":
        print("I've been seeing these. . . monsters. I feel like I can almost hear them when I'm in the deep of the mines. I feel like they're watching me from the darkness.")
        break
    else:
        print("Invalid Input")
time.sleep(3)
print("The elevator comes to a stop. The foreman comes up to the gate")
time.sleep(3)
print("\"ITS TIME TO WORK BOYS, Scott, Darren, John, you're on deep drill duty.", characterName,", Isom, Toby, you guys are on tunnel duty.\"")
time.sleep(3)
print("Scott looks at you with a petrified face, and starts to walk away")