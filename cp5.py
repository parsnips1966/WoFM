from functions import *
import variables as vars

def checkpoint5():
    if vars.decision_11 == "EAST":
        vars.background = "door"
        story("The passage ends at a solid wooden door with metal hinges. Listening at the door,\nyou hear strange mutterings and the clatter of what could be pots and pans.")
        vars.decision_12 = story("Whatever is in there, there are several of them.\nDo you want to go through the door?")
        if vars.decision_12 == "YES":
            vars.background = "fiveorcs"
            story("You open the door into a large room which can only only be the dining room\nof the same warty-faced creatures you now recognise.")
            story("Sitting around a large table are five Orcs busily drinking\nand dribbling their bowls of rat-gizzard soup.")
            story("All are involved in a rowdy arguement as to who will get to chew the rat bones\nleft in the large soup cauldron, so they do not see you enter.")
            vars.decision_13 = story("Will you be bold and prepare to ATTACK them or, if you don't relish the prospect\nof taking on five of these creatures, try to ESCAPE?")
            if vars.decision_13 == "ESCAPE":
                story("Test your Luck.")
                if stat_test(2):
                   vars.decision_12 == "NO"
                else:
                    #explanation
                    vars.decision_13 = "ATTACK"
            if vars.decision_13 == "ATTACK":
                story("The Orcs attack you one at a time.")
                vars.background = "orc"
                vars.monster = [6, 4]
                if fight("First Orc", 1):
                    vars.monster = [5, 3]
                    if fight("Second Orc", 1):
                        vars.monster = [6, 4]
                        if fight("Third Orc", 1):
                            vars.monster = [5, 2]
                            if fight("Fourth Orc", 1):
                                vars.monster = [4, 4]
                                if fight("Fifth Orc", 1):
                                    change_stats(0, 1)
                                    change_stats(1, 5)
                                    story("You are proud of your victory.")
                                    story("You search the bodies of the dead Orcs but find only\na few teeth, nails, bones and knives in their pockets.")
                                    story("You search the cupboards around the room\nbut find only crude bowls, plates and spoons.")
                                    vars.decision_13 = story("But under the serving hatch you find a thin leather\ncase half a metre long. Do you want to open it?")
                                    if vars.decision_13 == "YES":
                                        story("The case opens easily and inside you find a magnificent bow and one silver arrow.")
                                        story("An inscription on the case says: 'The giver of sleep to those who never can'.")
                                        vars.decision_13 = story("Do you want to eat Provisions" + provs_tuto() + "here?")
                                        if vars.decision_13 == "YES":
                                            take_provs()
                                        change_stats(2, 1)
                                        vars.equipment.append("Bow And Arrow")
                                        story("You put the bow, arrow and case in your pack and leave the room.")
                                        vars.decision_12 = "NO"
                                    elif vars.decision_13 == "NO":
                                        story("You leave it behind and walk out of the door.")
                                        vars.decision_12 = "NO"
                if vars.escape:
                    vars.decision_12 = "NO"
                    vars.escape = False
        if vars.decision_12 == "NO":
            vars.background = "passage"
            story("You move swiftly down the passage and arrive back\nat the junction. You turn northwards this time.")
            vars.decision_11 = "NORTH"

    if vars.decision_11 == "NORTH":
        vars.background = "door"
        story("You see a well-used door on the right-hand(east) side of the passageway.\nWith your ear to the keyhole, you hear a man screaming for help from inside.")
        vars.decision_11 = story("Will you OPEN the door or WALK on?")
        if vars.decision_11 == "OPEN":
            story("The door is locked so you try to charge it down. Test your Skill.")
            if not stat_test(0):
                story("The door remains locked, you bruise your\nshoulder and you must progress up the passage.")
                vars.decision_11 = "WALK"
            else:
                vars.background = "darkroom"
                story("The locked door bursts open and a nauseating stench hits your nostrils.\nInside, the floor is covered with bones, rotting vegetation and slime.")
                story("A wild-haired old man, clothed in rags, rushes at you screaming.\nHis beard is long and grey, and he is waving an old wooden chair-leg.")
                vars.decision_12 = story("Is he as insane as he appears, or is this some kind of trap?\nWill you either SHOUT to try to calm him down or draw your sword and ATTACK?")
                if vars.decision_12 == "SHOUT":
                    story("You shout: 'You are freed, old man!' at the top of your voice.\nInstantly, his rantings cease. He stops and sinks to the floor, weeping loudly.")
                    story("As he composes himself, he thanks you many times. You talk in the hope of\ndiscovering secrets of the mountain and he begins to tell his story.")
                    story("Many years ago he was an adventurer like you\nin search of the Warlock's treasure.")
                    story("He was captured by Orcs and thrown into his\nsolitary cell as a sort of pet for the creatures.")
                    story("You ask whether he would like to accompany you into the mountain,\nbut he simply wants to leave and see the world again.")
                    story("You ask him for advice but he says he knows little.\nHe advises you to pay your respects to the boatman.")
                    story("He tells you that you must pull the right-hand lever on the wall ahead\nto open the iron gate at the end of the passage.")
                    story("He has also learned that the keys to the Boat House are guarded by a\nman and his dog. You shake hands, leave the room and go your separate ways.")
                    vars.decision_11 = "WALK"
                elif vars.decision_12 == "ATTACK":
                    story("You lunge at the old man as he leaps towards you with outstretched arms\n- and run him through the chest with your sword.")
                    story("You curse as you realise he was making no attempt to attack; his wild excitement\nmust merely have been relief after being imprisoned for so long.")
                    story("You will now get no information out of him on the perils of\nthe adventure ahead. You progress up the passageway.")
                    vars.background = "passage"
                    vars.decision_11 = "WALK"
        if vars.decision_11 == "WALK":
            vars.background = "door"
            vars.decision_14 = story("Further up the passage you see a door in the east wall. You listen hard\nbut can hear no sound. Do you want to investigate?")
    vars.checkpoint = 6