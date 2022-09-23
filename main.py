"""The main file which contains the storyline and calls all the functions."""

from random import randint
import pygame
from pygame.locals import *
from json import load, dumps
from functions import *
import variables as vars
from cp0 import checkpoint0
from cp1 import checkpoint1
from cp2 import checkpoint2
from cp3 import checkpoint3
from cp4 import checkpoint4
from cp5 import checkpoint5
from cp6 import checkpoint6
from cp7 import checkpoint7
from cp8 import checkpoint8
from rp1 import repeat1
from rp2 import repeat2
from rp3 import repeat3
from rp4 import repeat4
from time import sleep

print("Joseph is right")

if __name__ != "__main__":
    raise Exception

vars.background = "mountain"
consts.screen.fill(consts.BLACK)
surf = pygame.image.load("./images/" + vars.background + ".jpg").convert()
consts.screen.blit(surf, surf.get_rect())
decision_1 = story("Welcome to The Warlock of Firetop Mountain.\nWould you like to create a NEW account or LOAD an existing one?")
if decision_1 == "NEW":
    vars.profile_name = story("What would you like to call it?", any_input=True).lower()
    with open("profile_list.json", "r") as file:
        profile_list = load(file)
    if vars.profile_name not in profile_list["profiles"]:
        profile_list["profiles"].append(vars.profile_name)
        save = dumps(profile_list)
        with open("profile_list.json", "w") as file: 
            file.write(save)
    else:
        story("That account already exists. Go and cry in a hole.")
elif decision_1 == "LOAD":
    with open("profile_list.json", "r") as file:
        profile_list = load(file)
    account = story("Which account would you like to use?", any_input=True)
    if account in profile_list["profiles"]:
        with open(account + ".json", "r") as user_data:
            variables_obj = load(user_data)
            vars.gold = user_data["gold"]
            vars.provs = user_data["provs"]
            vars.hero = user_data["hero"]
            vars.gold = user_data["gold"]
            vars.gold = user_data["gold"]
            vars.gold = user_data["gold"]
            #########HERREEEEEEEEEEEEERBJABKAkjbaK!!!!!!!!!!!!!!!

print(vars.checkpoint)

if vars.checkpoint == 0:
    checkpoint0()

if vars.checkpoint == 1:
    checkpoint1()

if vars.checkpoint == 2:
    checkpoint2()
  
if vars.checkpoint == 3:
    checkpoint3()

if vars.checkpoint == 4:
    checkpoint4()

vars.checkpoint = 5
if vars.checkpoint == 5:
    checkpoint5()

vars.checkpoint = 6
if vars.checkpoint == 6:
    checkpoint6()

vars.checkpoint = 7
if vars.checkpoint == 7:
    checkpoint7()

vars.checkpoint = 8
if vars.checkpoint == 8:
    checkpoint8()

pygame.quit()
#you can face the Winged Gremlin twice
#add animations when changing stats
#make it so you can go to all 3 walls
#add sound
#add more images
#I've a feeling I'm missing a bit maybe with a vampire
#fix dice

#line 243, in change_stats
#    if vars.hero[stat] + amount > vars.init_hero[stat]:
#TypeError: '>' not supported between instances of 'int' and 'list'
