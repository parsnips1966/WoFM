from functions import *
import variables as vars

def checkpoint_0():
    story("Welcome to Firetop Mountain.")
    story("You have in your possession a sword and a shield\ntogether with a rucksack containing Provisions for the trip.")
    story("You have been preparing for this quest but to see how successful you have been\nyou must use the dice to determine your initial Skill, Stamina and Luck scores.")
    story("Roll 1 die to determine your Skill score.")
    dice_num = randint(1, 6)
    vars.hero[0] = dice_num + 6
    vars.init_hero.append(vars.hero[0])
    story("6 is added to your roll.")
    story("Roll 2 dice to determine your Stamina score.")
    dice_num = randint(2, 12)
    vars.hero[1] = dice_num + 12
    vars.init_hero.append(vars.hero[1])
    story("12 is added to your roll.")
    story("Roll 1 die to determine your Luck score.")
    dice_num = randint(1, 6)
    vars.hero[2] = dice_num + 6
    vars.init_hero.append(vars.hero[2])
    story("6 is added to your roll.")
    story("Your Skill, Stamina and Luck scores will change throughout the game\nbut rarely exceed these initial values.")
    vars.background = "archinside"
    story("You may now enter the mountain...")
    vars.checkpoint = 1