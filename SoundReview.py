import pygame
import os
from time import sleep
import subprocess
import time

path = os.getcwd()
folder = path.split("/")[-1]
files = os.listdir()

def Play(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.mixer.quit()


def Run(file):
    print(file)
    print()
    if os.path.isfile(file) and file.split(".")[-1] == "wav":
        Review(file)

def Review(file):
    Play(file)
    test = input("Do you hear a " + str(folder) + "\n" + "Select option - (Y)es/(N)o/(D)elete " )
    if test == "Y" or test =="y":
        if not os.path.isdir(folder):
            os.mkdir(folder)
        subprocess.run(["mv", str(file), str(folder) + "/" +str(file) ])
        pass
    elif test == "d" or test == "D":
        os.remove(str(file))
    elif test =="N" or test == "n":
        print("Making new class")
        newdir = input("Enter a category name ")
        newdir = newdir.lower()
        if not os.path.isdir(newdir):
            os.mkdir(newdir)
        subprocess.run(["mv", str(file), str(newdir) + "/" +str(file) ])
    else:
        print()
        print("Invalid Key - try again")
        Review(file)


[Run(y) for x,y  in enumerate(files)]

