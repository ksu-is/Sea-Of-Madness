import sys
import os
import random
import time
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pygame

import logging
import logging.handlers as handlers
from datetime import datetime

import subprocess as s



pygame.init()
pygame.mixer.music.load("backingtrack.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

pygame.mixer.init()
jumpscare_sounds = pygame.mixer.Sound("Jumpscare Sound.mp3")
jumpscare_sounds.set_volume(0.02)

doorcreak = pygame.mixer.Sound("doorsound.mp3")
doorcreak.set_volume(0.02)

underwater = pygame.mixer.Sound("underwatersound.mp3")
underwater.set_volume(0.05)

foghorn = pygame.mixer.Sound("scaryfoghorn.mp3")
foghorn.set_volume(0.05)

endmusic = pygame.mixer.Sound("end_theme.mp3")
endmusic.set_volume(0.05)

footsteps = pygame.mixer.Sound("foostep.mp3")
footsteps.set_volume(0.05)

whisper = pygame.mixer.Sound("whisper.mp3")
whisper.set_volume(0.05)

secondscare = pygame.mixer.Sound("scaryjumpscarenew.mp3")
secondscare.set_volume(0.05)

scaryotherend = pygame.mixer.Sound("scaryotherend.mp3")
scaryotherend.set_volume(0.05)

calmstudy = pygame.mixer.Sound("calmstudy.mp3")
calmstudy.set_volume(0.05)

waterfootstep = pygame.mixer.Sound("waterfootstep.mp3")
waterfootstep.set_volume(0.05)

game_over = False

# Setting up Log file name
time = str(datetime.now())
# print(time)

str_file = datetime.now().strftime('mylogfile_%Y-%m-%d_%H-%M')

# print(str_file)



# Creating Player Class for Adventurer
class player:
    def __init__(self, location, items, sanity):
        self.location = location
        self.sanity = sanity    
        self.items = items
        self.waited = False

hero = player("entry", 0, 100)

class GUI:
    
    # Initialzing main window for GUI
    def __init__(self, window):
        self.window = window

        self.waited = False
    
        choices = 0

        window.title("Sea of Madness")

        window.geometry("966x745+0+0")
        window.minsize(width=966, height=745)
        window.maxsize(width=966, height=745)
        window.configure(bg="black")


        frame = Frame(window)
        frame.pack()
        
        print("Medkits", hero.items)


        # Getting and setting up image
        
        self.img = ImageTk.PhotoImage(Image.open("Untitled-1.gif"))
        
        # Loading Background Image
        self.label = tkinter.Label(frame, image=self.img)
        self.label.pack()

        # Setting Basic buttons and Labels
        self.l1 = tkinter.Label(frame, text="Welcome, to the Sea of Madness")
        self.l1.pack()

        #health_text = "HEALTH = " + str(hero.health)

        sanity_text = "SANITY =" + str(hero.sanity)

        #self.l2 = tkinter.Label(frame, text=health_text, bg="Black", fg="White")
        #self.l2.pack()

        self.l4 = tkinter.Label(frame, text=sanity_text, bg="Black", fg="White")
        self.l4.pack()

        #medkit_text = "MEDKITS = " + str(hero.items)
        
        #self.l3 = tkinter.Label(frame, text=medkit_text, bg="Black", fg="White")
        #self.l3.pack()

        self.b1 = tkinter.Button(frame, width=15, height=3, text="START", command=self.Entry)
        self.b1.pack()

        self.yes_1 = tkinter.Button(frame, width=15, height=1, text="Enter Door")
        # yes_1.pack()

        self.no_1 = tkinter.Button(frame, width=15, height=1, text="Stand Still")
        # no_1.pack()

        #self.use_medkit = tkinter.Button(frame, width=15, height=1, text="USE MEDKIT")

    # Function to make Medkit

    def game_over (self, message):
            logging.info("GAME OVER")
            self.l1.config(text=message)
            self.yes_1.config(state='disabled')
            self.no_1.config(state='disabled')

    # Function to allow use of Medkit
    

    # Function to handle Bat Attack
    def bat_attack(self):
        bat_attack = random.choice([True, False])
        if bat_attack is True:
            self.change_img("scary_inhead.jpg")
            jumpscare_sounds.play()
            tkinter.messagebox.showinfo( "Psychological Attack", "Your Sanity Weakens")
            #hero.health -= random.randint(1, 100)
            hero.sanity -= random.randint(1, 40)
            sanity_text = "SANITY = " + str(hero.sanity)
            #health_text = "HEALTH = " + str(hero.health)
            self.l4.configure(text=sanity_text)
            #self.l2.configure(text=health_text)
            

            # Killing the Game
            
            if hero.sanity <= 0:
                game_over = True
                print(game_over)
                logging.info("You succumbed to the darkness and lost your sanity")
                tkinter.messagebox.showinfo( "You Lost Your Mind", "You have lost your way. . .")
                self.window.destroy()

    
    # Creating Button function
    def create_btn(self, str, cmd):
        btn = self.tkinter.Button(self.frame, width=15, height=1, text=str, command=cmd)
        return btn


    # Clearin Frame of all widgets
    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    # Function to change image
    def change_img(self,str):
        self.img2=ImageTk.PhotoImage(Image.open(str))
        self.label.configure(image=self.img2)
        self.label.image=self.img2



    # Starting of Game with 1st Stage
    def Entry(self):
        logging.info("Starting Game")
        self.change_img("hallwaydoor.jpg")
        self.b1.destroy()
        self.yes_1.pack()
        self.no_1.pack()
        
        self.l4.pack()
        self.l1.config(text="You wake up, lost, confused, in a hallway with dim lighting. Do you go enter one of the doors infront of you? or Do you stand still?")


        self.yes_1.configure(command=self.yes_kick)
        self.yes_1.pack()
        

        self.no_1.configure(command=self.no_kick)
        self.no_1.pack()



    # Choosing option YES
    def yes_kick(self):
        logging.info("YES")
        print("Location", hero.location)
        doorcreak.play()
        #self.bat_attack()

        self.change_img("staircase.jpg")
        self.l1.config(text="You eventually find your way near a staircase that seems oddly familiar, do you go down the stairs?")
        self.yes_1.configure(command=self.Door)
        self.yes_1.config(text="Yes")
        self.no_1.config(text="No")
        #yes_1.pack()

    # Choosing option NO
    def no_kick(self):
        logging.info("NO")
        hero.sanity -= 40
        sanity_text = "SANITY = " + str(hero.sanity)
        self.l4.configure(text=sanity_text)
        self.change_img("scary_inhead.jpg")
        self.yes_1.config(text="RUN")
        self.no_1.config(text="Stand Still")
        self.l1.config(text="The lights flash and all you can see is some kind of creature in front of you. Do you run or continue to stand still?. . .")

    # Choosing option YES
    def Door(self):
        logging.info("YES")
       
        self.bat_attack()
        footsteps.play()
        self.change_img("end_tunnel.jpg")
        self.l1.config(text="After climbing down the stairs you open a door. You see a long tunnel in front of you, with what looks like a light infront of you. Do you walk ahead? Or do you stand still?")
        self.l4.pack()
        self.yes_1.config(text="Keep Going")
        self.no_1.config(text="Stand Still")
        self.no_1.configure(command=self.no_Door)
        self.yes_1.configure(command=self.Alarming)

    # Choosing option NO
    def no_Door(self):
        logging.info("NO")
        self.bat_attack()
        self.l1.config(text="It's too dark. . . keep moving")
        
        self.l4.pack()

    # Choosing option YES
    def Alarming(self):
        logging.info("YES")
        self.change_img("old_study.jpg ")
        pygame.mixer.music.stop()
        footsteps.play()
        calmstudy.play()
        self.l1.config(text="As you get to the end of the tunnel, you feel like it transported you to a different place, a calm place. Looks like an old study. Snoop around or keep going?")
        self.l4.pack()
        self.yes_1.config(text="Keep Going")
        self.no_1.config(text="Snoop Around")
        self.no_1.configure(command=self.no_Alarming)
        self.yes_1.configure(command=self.Cavern)

    # Choosing option NO
    def no_Alarming(self):
        logging.info("NO")
        self.l1.config(text="You look around for a while, you find a note with the message \"Don't touch the book, Follow the light\" \n After enjoying the warmth a little longer, you decide that you should keep going.")
        footsteps.play()
        hero.sanity += 20
        sanity_text = "SANITY = " + str(hero.sanity)
        self.l4.configure(text=sanity_text)
        self.l4.pack()

    # Choosing option YES
    def Cavern(self):
        logging.info("YES")
        calmstudy.stop()
        pygame.mixer.music.play()
        self.change_img("dark_wet.jpg")
        footsteps.play()
        self.l1.config(text="After leaving the study, you stumble into a dark wet room, you hear whispers coming from the darkness, do you keep going? or stand still?")
        whisper.play()
        self.yes_1.config(text="Keep Going")
        self.no_1.config(text="Stand Still")
        self.l4.pack()
        self.no_1.configure(command=self.no_Cavern)
        self.yes_1.configure(command=self.Hallway)

    # Choosing option NO
    def no_Cavern(self):
        logging.info("NO")
        self.waited = True
        waterfootstep.play()
        self.l1.config(text="You hear something slowly walking past you in the pitch black darkness. After waiting for a minute it seems like the coast is clear, keep moving. ")
        self.l4.pack()
        
    # Choosing option YES
    def Hallway(self):
        logging.info("YES")
        if not self.waited:
            self.bat_attack()
        footsteps.play()
        self.change_img("library.jpg")
        self.l1.config(text="You find yourself in a large, dark library of some sort. You see a book named \"The Sea of Madness\" Do you pick it up?")
        self.l4.pack()
        self.yes_1.config(text="Continue walking")
        self.no_1.config(text="Pick up the book")
        self.no_1.configure(command=self.no_Hallway)
        self.yes_1.configure(command=self.Pit)

    # Choosing option NO
    def no_Hallway(self):
        logging.info("NO")
        self.change_img("scaryinheaddead.jpg")
        secondscare.play()
        self.l1.config(text="You grab the book and you start to shudder, you start losing consciousness as your vision fades to black.")
        hero.sanity -= 1000
        sanity_text = "SANITY = " + str(hero.sanity)
        self.game_over("The Sea of Madness has overtaken your mind.")
        self.l4.configure(text=sanity_text)
        self.l4.pack()

    # Choosing option YES
    def Pit(self):
        logging.info("YES")
       
        self.bat_attack()

        self.change_img("waterphoto.jpg")
        self.l1.config(text="As you walk down the hallway, you fall deep into a body of water. You see a light deeper in the water. Swim up or down? ")
        underwater.play()
        self.yes_1.config(text="Swim down")
        self.no_1.config(text="Swim up")
        self.l4.pack()
        self.no_1.configure(command=self.no_Pit)
        self.yes_1.configure(command=self.Gold)

    # Choosing option NO
    def no_Pit(self):
        logging.info("NO")
        self.change_img("underwater.jpg")
        pygame.mixer.music.stop()
        scaryotherend.play()
        hero.sanity -= 81375910
        sanity_text = "SANITY = " + str(hero.sanity)
        self.l4.configure(text=sanity_text)
        self.l1.config(text="You start to swim up, you slowly realize that the surface is getting farther and farther away, running out of oxygen. You succumb to the Sea of Madness.")
        self.game_over("You try to swim up, but the surface continues to get futher away, as you run out of oxygen. You succumb to the Sea of Madness")
        
        self.l4.pack()

    # Choosing option YES
    def Gold(self):
        logging.info("YES")
        self.change_img("Lighthouse.jpg")
        self.l1.config(text="As you get closer to the light, you realize it's a way out of the water. As you surface you see a lighthouse, do you swim towards the lighthouse?")
        self.yes_1.config(text="Away From Lighthouse")
        self.no_1.config(text="Toward lighthouse")
        self.l4.pack()
        self.no_1.configure(command=self.Lose)
        self.yes_1.configure(command=self.Win)

    # Choosing option NO
    def Lose(self):
        logging.info("LOSE")
        self.change_img("lighthouse2.jpg")
        pygame.mixer.music.stop()
        foghorn.play()
        hero.sanity -= 81375910
        sanity_text = "SANITY = " + str(hero.sanity)
        self.l4.configure(text=sanity_text)
        self.l1.config(text="You swim towards the lighthouse, and as you get closer the light turns red.")
        self.game_over("The Sea of Madness has overtaken your mind.")

    # Choosing option YES
    def Win(self):
        logging.info("WON")
        self.change_img("forestwater.jpg")
        self.l1.config(text="As you swim away, you realize it's getting brighter and you start to feel safe again.")
        pygame.mixer.music.stop()
        underwater.stop()
        endmusic.play()
        self.l4.pack()
        self.game_over("You've escaped the Sea of Madness.")


class Game:

    def print_slow(self, str, delay=0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")

    def game_over (self, message):
            gui.game_over(message)

    def reset_console(self):
        print("\n")
        os.system('cls||clear')


    def fprint(self, str, delay=0):
        print("\n" + str)
        time.sleep(delay)


    def sprint(self, str, delay=0):
        print(str)
        time.sleep(delay)

game_functions = Game()
class World:

    

    def test_run():
        root = Tk()
        gui = GUI(root)
        root.mainloop()
        pass

if __name__ == '__main__':
    # Running the main GUI object
    root = Tk()
    gui = GUI(root)
    root.mainloop()
    game_functions = Game()
    

    # new_world = World()


    # new_world.entry()
