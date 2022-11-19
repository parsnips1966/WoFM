"""The main file which contains the storyline and calls all the functions."""

from json import dumps, load

import pygame
from pygame.locals import *

import variables as vars
from cp0 import checkpoint_0
from cp1 import checkpoint_1
from cp2 import checkpoint_2
from cp3 import checkpoint_3
from cp4 import checkpoint_4
from cp5 import checkpoint_5
from cp6 import checkpoint_6
from cp7 import checkpoint_7
from cp8 import checkpoint_8
from cp9 import checkpoint_9
from cp10 import checkpoint_10
from cp11 import checkpoint_11
from cp12 import checkpoint_12
from cp13 import checkpoint_13
from functions import *

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
            vars.checkpoint = 0
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
            vars.decision_10 = user_data["decision_20"]
            vars.decision_11 = user_data["decision_21"]
            vars.decision_12 = user_data["decision_22"]
            vars.decision_13 = user_data["decision_23"]
            vars.decision_14 = user_data["decision_24"]
            vars.decision_15 = user_data["decision_25"]
            vars.decision_16 = user_data["decision_26"]
            vars.decision_17 = user_data["decision_27"]
            vars.decision_18 = user_data["decision_28"]
            vars.decision_19 = user_data["decision_29"]
            vars.decision_10 = user_data["decision_30"]
            vars.decision_11 = user_data["decision_31"]
            vars.decision_12 = user_data["decision_32"]
            vars.decision_13 = user_data["decision_33"]
            vars.decision_14 = user_data["decision_34"]
            vars.decision_15 = user_data["decision_35"]
            vars.decision_16 = user_data["decision_36"]
            vars.decision_17 = user_data["decision_37"]
            vars.decision_18 = user_data["decision_38"]
            vars.decision_19 = user_data["decision_39"]
            vars.decision_10 = user_data["decision_40"]
            vars.decision_11 = user_data["decision_41"]
            vars.decision_12 = user_data["decision_42"]
            vars.decision_13 = user_data["decision_43"]
            vars.decision_14 = user_data["decision_44"]
            vars.decision_15 = user_data["decision_45"]
            vars.decision_16 = user_data["decision_46"]
            vars.decision_17 = user_data["decision_47"]
            vars.decision_18 = user_data["decision_48"]
            vars.decision_19 = user_data["decision_49"]
            vars.decision_10 = user_data["decision_50"]
            vars.decision_11 = user_data["decision_51"]
            vars.decision_12 = user_data["decision_52"]
            vars.decision_13 = user_data["decision_53"]
            vars.decision_14 = user_data["decision_54"]
            vars.decision_15 = user_data["decision_55"]
            vars.decision_16 = user_data["decision_56"]
            vars.decision_17 = user_data["decision_57"]
            vars.decision_18 = user_data["decision_58"]
            vars.decision_19 = user_data["decision_59"]
            vars.decision_10 = user_data["decision_60"]
            vars.decision_11 = user_data["decision_61"]
            vars.decision_12 = user_data["decision_62"]
            vars.decision_13 = user_data["decision_63"]
            vars.decision_14 = user_data["decision_64"]
            vars.decision_15 = user_data["decision_65"]
            vars.decision_16 = user_data["decision_66"]
            vars.decision_17 = user_data["decision_67"]
            vars.decision_18 = user_data["decision_68"]
            vars.decision_19 = user_data["decision_69"]
            vars.decision_10 = user_data["decision_70"]
            vars.decision_11 = user_data["decision_71"]
            vars.decision_12 = user_data["decision_72"]
            vars.decision_13 = user_data["decision_73"]
            vars.decision_14 = user_data["decision_74"]
            vars.decision_15 = user_data["decision_75"]
            vars.decision_16 = user_data["decision_76"]
            vars.decision_17 = user_data["decision_77"]
            vars.decision_18 = user_data["decision_78"]
            vars.decision_19 = user_data["decision_79"]
            vars.decision_10 = user_data["decision_80"]
            vars.decision_11 = user_data["decision_81"]
            vars.decision_12 = user_data["decision_82"]
            vars.decision_13 = user_data["decision_83"]
            vars.decision_14 = user_data["decision_84"]
            vars.decision_15 = user_data["decision_85"]
            vars.decision_16 = user_data["decision_86"]
            vars.decision_17 = user_data["decision_87"]
            vars.decision_18 = user_data["decision_88"]
            vars.decision_19 = user_data["decision_89"]
            vars.decision_10 = user_data["decision_90"]
            vars.decision_11 = user_data["decision_91"]
            vars.decision_12 = user_data["decision_92"]
            vars.decision_13 = user_data["decision_93"]
            vars.decision_14 = user_data["decision_94"]
            vars.decision_15 = user_data["decision_95"]
            vars.decision_16 = user_data["decision_96"]
            vars.decision_17 = user_data["decision_97"]
            vars.decision_18 = user_data["decision_98"]
            vars.decision_19 = user_data["decision_99"]
            break
        else:
            story("That account doesn't exist.")
            
cp_funcs = {
    0: checkpoint_0,
    1: checkpoint_1,
    2: checkpoint_2,
    3: checkpoint_3,
    4: checkpoint_4,
    5: checkpoint_5,
    6: checkpoint_6,
    7: checkpoint_7,
    8: checkpoint_8,
    9: checkpoint_9,
    10: checkpoint_10,
    11: checkpoint_11,
    12: checkpoint_12,
    13: checkpoint_13
}

while True:
    try:
        cp_func = cp_funcs[vars.checkpoint]
    except KeyError as e:
        pass  # Handle error
    else:
        cp_func()

pygame.quit()
#add animations when changing stats
#make it so you can go to all 3 walls
#add sound
#add more images
#fix dice
#set background at beginnning of checkpoints
#end of cp8 has to get back to start
#make Crocodile fight only 2 rounds