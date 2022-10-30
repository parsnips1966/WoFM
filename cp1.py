from functions import *
import variables as vars
from rp1 import repeat1
from rp2 import repeat2
from rp3 import repeat3
from rp4 import repeat4

def checkpoint1():
    vars.background = "passage"
    vars.decision_2 = story("You enter the caverns of Firetop Mountain and within a few metres\nyou arrive at a junction, do you want to go EAST or WEST?")
    if vars.decision_2 == "EAST":
        vars.background = "door"
        vars.decision_3 = story("The passageway soon comes to an end at a locked wooden door.\nYou listen at the door but hear nothing. Will you try to charge it down?")
        if vars.decision_3 == "YES":
            story("You charge the door with your shoulder. Test your Skill by rolling two dice\nto see if it's less than or equal to your Skill score.")
            if stat_test(0):
                vars.background = "pit"
                story("The door bursts open and you fall headlong into a room.")
                story("But your heart jumps as you realise you are not landing on\nthe floor, but plunging down a pit of some kind!")
                change_stats(1, 1, "subtract")
                story("Luckily it's not very deep.")
                vars.background = "passage"
                story("You climb out and leave through the door heading westwards.")
            else:
                story("You rub your bruised shoulder and decide against\ntrying again. You turn around and head back to the junction.")
                vars.background = "passage"
        elif vars.decision_3 == "NO":
            vars.background = "passage"
            story("You turn around and head back to the junction.")
        vars.background = "archtooutside"
        story("You arrive back at the junction. You look left to see the\ncave entrance in the dim distance but walk straight on.")
        vars.decision_1 = "WEST"
    if vars.decision_2 == "WEST":
        vars.background = "passage"
        story("There's a right-hand turn to the north. Cautiously you approach a sentry post\non the corner and see a strange goblin-like creature wearing leather armour.")
        vars.background = "sleepingorc"
        story("He is asleep at his post so you try to tiptoe past him. Test your Luck\nby rolling 2 dice to see if it's less than or equal to your Luck score.")
        story("Each time you Test your Luck one point\nwill be subtracted from your Luck score.")
        if stat_test(2):
            vars.background = "door"
            story("You make it past. On your left,\nthe west face of the passage, there is a rough-cut wooden door.")
        else:
            vars.background = "orc"
            story("You step with a crunch on some loose ground and his eyes flick open.")
            story("The creature that has just awakened is an Orc! He scrambles to his feet\nand turns to grasp an alarm bell. You must attack him quickly.")
            fight_tuto()
            vars.monster = [6, 5]
            if fight("Orc"):
                vars.background = "door"
                story("On your left, the west face of the passage,\nthere is a rough-cut wooden door.")
        vars.decision_4 = story("You listen at the door and can hear a rasping sound which\nmay be some kind of creature snoring. Do you want to open the door?")
    vars.checkpoint = 2