from functions import *
import variables as vars

def checkpoint_6():
    if vars.decision_23 == "YES":
        vars.decision_24 = story("The door is firmly locked. You may try to force it open, will you?")
        if vars.decision_24 == "YES":
            story("You charge at the door, hitting it squarely with your shoulder. Test your Skill.")
            if not stat_test(0):
                change_stats(1, 1, "subtract")
                story("The door shudders but does not budge\nand you wince in pain.")
                vars.background = "passage"
                story("You continue up the corridor.")
                vars.decision_23 = "NO"
            else:
                story("The door splits along its length and you can\nwrench the timbers apart to let yourself in.")
                vars.background = "room"
                story("A torch hangs from one wall lighting up a small armoury room stocked with\nswords, shields, helmets, daggers, breastplates and the like.")
                story("You examine the weaponry and find nothing superior to your sword. However,\nan iron shield with a golden crescent at its centre catches your eye.")
                story("You pick it up and feel its weight on your arm. If you wish to take this shield\nit will aid you in battles by helping to fend off wound damage.")
                story("If, in future during a battle in which you are using this shield,\na creature wounds you, you may throw one die.")
                story("If you throw a 6, the creature inflicts 1 less\npoint of damage than it would usually do.")
                vars.equipment.append("Shield")
                if len(vars.equipment) > 0:
                    vars.decision_25 = story("However, the shield is heavy so you must choose a piece of\nequipment to leave behind. Which will you pick?")
                    while vars.decision_25.title() not in vars.equipment:
                        vars.decision_25 = story("You don't have that. Which piece of equipment will you choose from your pack?")
                    vars.equipment.remove(vars.decision_25.title())
                story("You now leave the room and continue up the corridor.")
                vars.decision_23 = "NO"

    if vars.decision_23 == "NO":
        vars.background = "door"
        story("On the east wall of the passage you see another door, this time made of solid metal.\nListening at the door you hear tortured screams coming from within.")
        vars.decision_26 = story("Do you wish to try opening the door?")
        if vars.decision_26 == "YES":
            vars.background = "room"
            story("The door is not locked and opens. The room in front of you seems to be a\nsmall torture chamber, with various torture devices around the walls.")
            story("In the centre, two small, hunchbacked creatures are having their fiendish way\nwith a Dwarf, who is tied to a hook in the ceiling by his wrists.")
            story("The two hunchbacks are poking and cutting him viciously with their swords.\nThe Dwarf lets out a final scream and falls silent, eyes closed.")
            story("His captors make disappointed noises and look round angrily as if it were\nyour fault that the Dwarf has collapsed. You must act quickly. Will you:")
            vars.decision_27 = story("CLOSE the door quickly and continue on?\nDraw your sword and FIGHT?\nJAB the Dwarf with your sword and put on an evil laugh?")
            if vars.decision_27 == "CLOSE":
                vars.decision_26 = "NO"
            elif vars.decision_27 == "FIGHT":
                story("These two evil creatures are Goblins.\nThey attack you one at a time.")
                vars.monster = [5, 5]
                if fight("Goblin"):
                    if fight("Goblin"):
                        story("You cut down the Dwarf. He is, as you guessed, dead. Going through the\nGoblins' pockets, you find a large piece of sweet-smelling Cheese.")
                        story("You put it in your pack and leave the room northwards.")
                        vars.equipment.append("Cheese")
                        vars.decision_26 = "NO"
            elif vars.decision_27 == "JAB":
                story("The two Goblins look at each other amazed. They chatter to themselves and\nthen indicate for you to wait while they go off and get another Dwarf.")
                story("They disappear out of the room and you cut down the Dwarf who is, as you guessed,\nquite dead. You decide it best to leave and press on northwards.")
                vars.decision_26 = "NO"
        if vars.decision_26 == "NO":
            vars.background = "passage"
            story("You arrive at the passage's end, where it meets another going east-west.\nAn iron portcullis blocks your way and no amount of charging will budge it.")
            vars.decision_28 = story("On the wall are two levers and it seems these have something to do\nwith the portcullis. Do you wish to pull the RIGHT or LEFT lever?")
    vars.checkpoint = 7