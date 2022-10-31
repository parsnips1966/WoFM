"""The main file which contains the storyline and calls all the functions."""

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

if __name__ != "__main__":
    raise Exception

vars.background = "mountain"
consts.screen.fill(consts.BLACK)
surf = pygame.image.load("./images/" + vars.background + ".jpg").convert()
consts.screen.blit(surf, surf.get_rect())
decision_1 = story("Welcome to The Warlock of Firetop Mountain.\nWould you like to create a NEW account or LOAD an existing one?")
if decision_1 == "NEW":
    while True:
        vars.profile_name = story("What would you like to call it?", any_input=True).lower()
        with open("profile_list.json", "r") as file:
            profile_list = load(file)
        if vars.profile_name in profile_list:
            story("That account already exists.")
        else:
            break
elif decision_1 == "LOAD":
    with open("profile_list.json", "r") as file:
        profile_list = load(file)
    while True:
        account = story("Which account would you like to use?", any_input=True).lower()
        if account in profile_list["profiles"]:
            with open(account + ".json", "r") as file:
                user_data = load(file)
            vars.gold = user_data["gold"]
            vars.provs = user_data["provs"]
            vars.hero = user_data["hero"]
            vars.init_hero = user_data["init_hero"]
            vars.equipment = user_data["equipment"]
            vars.river = user_data["river"]
            vars.fight_tuto_done = user_data["fight_tuto_done"]
            vars.provs_tuto_done = user_data["provs_tuto_done"]
            vars.checkpoint = user_data["checkpoint"]
            vars.profile_name = user_data["profile_name"]
            vars.decision_1 = user_data["decision_1"]
            vars.decision_2 = user_data["decision_2"]
            vars.decision_3 = user_data["decision_3"]
            vars.decision_4 = user_data["decision_4"]
            vars.decision_5 = user_data["decision_5"]
            vars.decision_6 = user_data["decision_6"]
            vars.decision_7 = user_data["decision_7"]
            vars.decision_8 = user_data["decision_8"]
            vars.decision_9 = user_data["decision_9"]
            vars.decision_10 = user_data["decision_10"]
            vars.decision_11 = user_data["decision_11"]
            vars.decision_12 = user_data["decision_12"]
            vars.decision_13 = user_data["decision_13"]
            vars.decision_14 = user_data["decision_14"]
            vars.decision_15 = user_data["decision_15"]
            vars.decision_16 = user_data["decision_16"]
            vars.decision_17 = user_data["decision_17"]
            vars.decision_18 = user_data["decision_18"]
            vars.decision_19 = user_data["decision_19"]
            break
        else:
            story("That account doesn't exist.")
            

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

if vars.checkpoint == 5:
    checkpoint5()

if vars.checkpoint == 6:
    checkpoint6()

if vars.checkpoint == 7:
    checkpoint7()

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
#got to end of rp1 with different decisions
#set background at beginnning of checkpoints