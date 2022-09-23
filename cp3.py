from functions import *
import variables as vars
from rp1 import repeat1
from rp2 import repeat2
from rp3 import repeat3
from rp4 import repeat4

def checkpoint3():
    if vars.decision_5 == "YES":
        vars.background = "room"
        story("The door opens to reveal a small room with dirty walls. In the centre\nof the room is a makeshift wooden table on which is standing a lit candle.")
        vars.decision_6 = story("Under the table is a small box.\nWill you either OPEN the box or LEAVE the room?")
        if vars.decision_6 == "OPEN":
            vars.background = "box"
            story("The box is light, but something rattles within.\nYou open the lid and a small Snake darts out to bite at your wrist!")
            vars.background = "snake"
            story("You must fight the snake.")
            fight_tuto()
            vars.monster = [5, 2]
            if fight("Snake"):
                vars.background = "key"
                story("The box has fallen to the ground during your fight with the Snake and\nout of it has fallen a bronze-coloured key with the number 99 carved into it.")
                vars.equipment.append("99 Key")
                story("You take this key with you and leave the room.")
                vars.decision_5 = "NO"
        elif vars.decision_6 == "LEAVE":
            vars.decision_5 = "NO"

    if vars.decision_5 == "NO":
        vars.background = "door"
        story("Further up the passage on the west wall you see another similar door. You listen\nand grimace to hear the worst singing you have ever heard in your life!")
        vars.decision_7 = story("Do you want to go into the room to investigate this hideous din?")
    vars.checkpoint = 4