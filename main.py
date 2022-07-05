"""The main file which contains the storyline and calls all the functions."""

from random import randint
import pygame
from pygame.locals import *
from functions import *
import variables as vars

def repeat_1():
    decision_16 = story("Set in the north wall is a small recess where you may eat\nProvisions without being seen. Do you wish to take Provisions?")
    if decision_16 == "YES":
        vars.provs -= 1
        change_stats(1, 4)
    decision_17 = story("Will you set off either EASTwards or WESTwards?")
    if decision_17 == "WEST":
        story("You walk westwards along the passageway.\nAfter fifty metres or so, the way turns northwards.")
        story("Two or three paces up the passage, you hear a crumbling beneath your feet\nand you try to leap back as the ground gives way. Test your Luck.")
        if not stat_test(2):
            story("You are too slow and you fall over two metres down into a pit - losing 1 Stamina.")
            story("You are in a pit, a little bruised but not too seriously hurt.")
            story("You look round and can see two passageways: a short one to the south\nthat opens into a small chamber, and another heading northwards.")
            story("You're a little worried about the crash your fall has made,\nand even more by the gruntings you hear coming from the chamber to the south.")
            story("Before you can collect your thoughts, a large, ugly head\npokes around the corner and a Troll emerges from its chamber.")
            story("Your ankle is twisted and you cannot move quickly, but\nthe Troll is ready for a fight. You will have to face the brute.")
            if "Invisibility Potion" in vars.equipment:
                vars.equipment.remove(vars.equipment.index("Invisibility Potion"))
                story("You drink the Potion and can see the look of\nastonishment spread across the Troll's face.")
                story("He comes up to you and he gropes the air fruitlessly. He thrashes around,\nclutching for you, but you are easily able to sidestep him.")
                story("Eventually he gives up and returns to his chamber,\njust in time, as you feel yourself reappearing.")
            else:
                fight_tuto()
                story("The creature is man-sized but its long arms\nlook very powerful. Resolve this battle:")
                vars.monster = [8, 8]
            if "Invisibility Potion" not in vars.equipment:
                if fight("Troll"):
                    story("The passage continues for quite some time,\nthen you reach the foot of a staircase cut into the rock.")
                    story("You ascend the stairs which end at a wooden door with rusty hinges.\nListening at the door, you can hear some scratching sounds.")
                    story("You try the handle and the door creaks open. You step into a \nbare room scattered with bones. There's a door on the wall opposite")
                    story("Gnawing at the bones are three Giant Rats\nwhich stop to look as you enter.")
                    story("Each is around a metre long and their\ntatty coats indicate that they are fighters.")
                    story("You will have to take them on if you are going to get\nthrough the room, as they no doubt see you as a tasty meal.")
                    if "Cheese" in vars.equipment:
                        vars.equipment.remove(vars.equipment.index("Cheese"))
                        story("You take the Cheese in your sack and toss it across the room.\nThe Rats scramble for it, scratching each other as they fight.")
                        vars.hero[2] += 2
                        story("Having distracted them, you pass through the room\nand leave by the door in the north wall.")
                    else:
                        story("You draw your sword and wait for the Rats to spring.\nAs the leader prepares to jump, you shout loudly and leap forward at it.")
                        story("Your cry frightens off the other two and they scamper back\na few paces. Fight each of the rats in turn:")
                        vars.monster = [5, 4]
                        if fight("First Rat"):
                            vars.monster = [6, 3]
                            if fight("Second Rat"):
                                vars.monster = [5, 5]
                                if fight("Third Rat"):
                                    story("You may leave through the door in the north wall.")
                    if "Cheese" not in vars.equipment:
                        story("The door opens into a wide passageway and you follow this\nfor some distance before reaching a junction.")
                        decision_18 = story("Here will you either go NORTHwards or turn to the EAST.")
                        if decision_18 == "NORTH":
                            story("The passage widens and you see you are entering a large cavern.\nYou hear noises coming from ahead and proceed cautiously.")
                            story("As you approach, you make out a large figure and are overawed\nas you see this oversized human is at least three metres!")
                            story("Dressed in a leather tunic, the creature is\nabsorbed in a meal he is eating at a table.")
                            story("The cavern is at least a hundred metres across\nand must be the home of this Giant.")
                            story("A large table and two chairs are along one of the walls,\nand it is here that the creature sits.")
                            story("Intent on his meal(a large pig), he is unlikely to notice you.")
                            story("Around the cavern you can see his mattress, a great furry pelt,\nand a huge hammer, which you have no hope of budging.")
                            story("A fire burns in one corner, under a hole in the ceiling.\nThere appears to be no other way through the cavern.")
                            decision_19 = story("Will you TAKE on this brute or RETURN to the junction?")
                            if decision_19 == "TAKE":
                                story("You draw your sword and enter. The Giant stops in the middle\nof a mouthful, raises his head and sniffs the air.")
                                story("He swings round and catches sight of you. Roaring loudly,\nhe flings the pig's carcass at you. Test your Luck.")
                                if not stat_test(2):
                                    story("It his you with quite some force. Then he picks\nup his hammer and prepares to club you with it.")
                                    vars.monster = [8, 9]
                                    if fight("Giant", 3):
                                        change_stats(0, 2)
                                        change_stats(2, 2)
                                        story("The mighty Giant lies dead! You search his cavern and\nfind little, although a belt purse contains 8 Gold.")
                                        story("You are a little concerned about to whom the second chair belongs.")
                                        story("You decide to leave the cavern the way you came.")
                                        decision_18 = "RETURN"
                                    elif vars.escape:
                                        story("You Escape down the passageway, where he will not be able to follow.")
                                        vars.escape = False
                                        decision_18 = "RETURN"
                            if decision_18 == "RETURN":
                                story("You arrive back at the junction and turn eastwards.")
                                decision_18 = "EAST"
                        if decision_18 == "EAST":
                            story("You arrive at another junction. An arrow on the wall points\nnorthwards and you decide to proceed in this direction.")
                            story("The passage runs northwards, and ahead you can har the splashings\nof an underground river. The air becomes cool and fresh.")
                            story("You soon reach a wide opening of a river bank but despair as\nyou look across to see no way through on the other side.")
                            story("To the east the river flows through a cave in the rock.")
                            decision_17 = story("You may either REST, and eat Provisions or will yougo what seems\nthe only way forward, jumping in and SWIMming downstream?")
                            if decision_17 == "REST":
                                vars.provs -= 1
                                story("You squat on the sandy bank. As you prepare your meal you notice\ba movement in the sand a couple of metres to your left.")
                                story("The movement becomes quite turbulent and\nyou spring to your feet, sword at the ready.")
                                story("Suddenly a large tubular head breaks through the surface,\ntwists around in the air and picks up your scent.")
                                story("The smooth, segmented body of a Giant Sandworm\nrears up and sways over in your direction.")
                                story("As it does so, a large orifice, with short spiky teeth, opens in\nwhat must be its head. You must do battle with this creature.")
                                if fight("Giant Sandworm", 3):
                                    change_stats(1, 4)
                                    story("Panting after the struggle, you sit down to collect\nyourself and finish the Provisions you started.")
                                vars.escape = False
                                repeat_4()
        else:
            story("You manage to leap quickly backwards before a pit opens.\nYou had better return to the junction.")
            decision_17 = "EAST"
    if decision_17 == "EAST":
        story("You follow the passage eastwards for several metres,\nthen it turns to the north.")
        decision_17 = story("Shortly you reach another junction where you may either go STRAIGHT\nor turn LEFT, into a passage that soon turns north. Which will you choose?")
        if decision_17 == "STRAIGHT":
            story("The passage ends at a wooden door, trimmed in iron. Various inscriptions\nadorn the door, but none of this makes any sense to you.")
            decision_18 = story("You listen, but hear nothing. Will you either\nOPEN the door or RETURN to the junction.")
            if decision_18 == "OPEN":
                story("The door opens into a small room, comfortably furnished with a table,\nseveral chairs and a large bookcase which covers one wall.")
                story("Seated at the table is an old man with a long grey beard,\nand squatting on the old man's shoulder is a small winged beast.")
                story("This creature is no more tham six centimetres tall.\nIt has two arms and legs; its skin is a dusty grey colour.")
                story("It has tiny sharp white teeth and its wings are folded behind its back.")
                story("The old man says nothing as you walk in through the door,\nbut he beckons you over to sit down at the table.")
                story("He is tossing in his hand two small white objects. Will you:")
                decision_18 = story("SIT down as he tells you?\nLEAVE the room and return to the junction?\nDraw your sword and RUSH forward?")
                if decision_18 == "SIT":
                    story("The old man does not look up, but his devilish little pet eyes you\nsuspiciously and starts chattering in a small squeaky voice.")
                    if vars.gold > 0:
                        decision_18 = story("The old man grunts and asks you whether you are game\nfor a wager. Will you ACCEPT, LEAVE or ATTACK him?")
                        #sus if you put attack
                        if decision_18 == "ACCEPT":
                            while decision_19 != "LEAVE":
                                while decision_19 < 1 or decision_19 > vars.gold:
                                    decision_19 = story("The old asks you your stake. How much will you bet?")
                                    if not decision_19.isdigit():
                                        story("Choose a number.")
                                    story("Bet between 1 and the number of Gold Pieces you have.")
                                story("He tosses the white dice he has been\nplaying with to you and asks you to roll.")
                                vars.dice_num = randint(2, 12)
                                vars.dice_roll2 = randint(2, 12)
                                story("You roll the dice")
                                if vars.dice_num > vars.dice_roll2:
                                    story("The old man rolls " + str(vars.dice_roll2) + " so you win your stake.")
                                    win = True
                                elif vars.dice_num < vars.dice_roll2:
                                    story("The old man rolls " + str(vars.dice_roll2) + " so you lose your stake.")
                                if vars.gold == 0:
                                    story("You have no Gold Pieces left so you must leave\nthrough the door and return to the junction.")
                                    break
                                decision_20 = story("Will you CONTINUE betting or LEAVE\nthrough the door and return to the junction?")
                                if decision_20 == "LEAVE":
                                    if win:
                                        change_stats(0, 2)
                                        change_stats(1, 2)
                                        change_stats(2, 2)
                                        story("2 points are added to your Skill, Stamina and Luck scores.")
                                    decision_18 = "LEAVE"
                                    break
                    else:
                        decision_18 = story("The old man asks if you are game for a wager but you\nhave no Gold so will you either LEAVE or ATTACK him.")
                elif decision_18 == "RUSH":
                    decision_18 = "ATTACK"
                if decision_18 == "ATTACK":
                    story("As you draw your sword, the Winged Gremlin flaps to the air and the man\nrushes to the bookshelf to escape through a secret door.")
                    story("But you must fight his pet.")
                    vars.monster = [5, 7]
                    if fight("Winged Gremlin"):
                        story("You search but try as you may you cannot find the switch for\nthe secret bookshelf door - the old man must have locked it.")
                        vars.gold += 5
                        story("You do find 5 Gold Pieces in a drawer in the table.\nYou decide to return to the junction to the south.")
                        decision_18 = "LEAVE"
                if decision_18 == "LEAVE":
                    story("You arrive back at the junction and this time take the passageway to the east.")
                    story("The passageway runs for several paces eastwards, then turns north.")
                    decision_17 = "LEFT"
            elif decision_18 == "RETURN":
                story("You arrive back at the junction and this time take the passageway to the east.\nIt runs for several paces eastwards, then turns north.")
                decision_17 = "LEFT"
        if decision_17 == "LEFT":
            story("The passageway ends in a door at which you listen but hear nothing.\nTrying the handle, the door opens to reveal a large, square room.")
            story("The room is completely bare, but the floor is covered in a mosaic of tiles.\nTwo shapes stand out; star tiles and hand tiles.")
            story("A door on the opposite wall is the only way through. Will you:")
            decision_17 = story("WALK across the room?\nWalk across the room only stepping on STARS?\nWalk across the room stepping only on HANDS?")
            if decision_17 == "WALK":
                story("Test your Luck three times.")
                change_stats(2, 1, "subtract")
                if not stat_test(2):
                    story("You are lucky.")
                    if not stat_test(2):
                        story("You are lucky.")
                        if not stat_test(2):
                            story("You make it across to the far door and can leave the room.")
                            decision_17 = "STARS"
                else:
                    #make work
                    story("You are unlucky and step on a hand tile.")
                    decision_17 = "HANDS"
            elif decision_17 == "STARS":
                story("You tiptoe precariously across the room to the door in the\nnorth wall. You open the door and proceed through it.")
            if decision_17 == "HANDS":
                story("The moment your foot touches a hand, you feel a vice-like grip\non your ankle and see a ghostly white hand gripping your leg.")
                story("You fight for your balance and manage to regain it.")
                story("But to your horror you see that, from every hand-shaped tile\nin the floor, a similar apparition has appeared.")
                story("The floor is now scattered with ghoulish hands, flexing and\nsnatching in the air. You draw your sword and chop at the hand.")
                vars.monster = [6, 4]
                if fight("Hand"):
                    story("The hand withers and shrinks back into the floor. At the same time,\nthe other hands stop dead and fade away down into the tiles.")
                    vars.hero[2] += 2
                    story("You decide this time to step on the star-shaped tiles, and step\ncarefully across to the door. The door opens. Add 2 Luck.")
                    decision_17 = "STARS"
            if decision_17 == "STARS":
                story("The passageway ahead runs northwards and you\nfollow this until you reach another junction.")
                decision_17 = story("Here will you either continue NORTHwards or you may turn WESTwards")
                if decision_17 == "NORTH":
                    story("The passageway ends in a solid doorway and you are surprised to see\na leather skirt tacked along the bottom of the door")
                    decision_17 = story("You listen but hear nothing. Will you\nENTER the room or RETURN to the junction?")
                    if decision_17 == "ENTER":
                        story("You enter a small room with bare, rocky walls. On the far wall hangs a golden key. There seems to be no way through the room.")
                        decision_18 = story("Do you want to go for the KEY or LEAVE it\nand return to the junction?")
                        if decision_18 == "KEY":
                            story("As you step into the room, the door swings shut behind you\nAs it closes, there is a click and a hiss.")
                            story("From the centre of the ceiling, a jet of gas is filling the room\nwith an acrid vapour. You breathe and cough deeply.")
                            decision_18 = story("Will you RETURN to the door and escape quickly or\nhold your breath and DASH for the key first?")
                            if decision_18 == "RETURN":
                                story("You get to the door, struggle with the lock and open it.\nYou burst out, close the door and take several deep breaths.")
                                decision_17 = "RETURN"
                            elif decision_18 == "DASH":
                                vars.equipment.append("125 key")
                                story("You snatch the key from its hook. It has the number 125 inscribed\non it. But your lungs are bursting. Roll two dice.")
                                if not stat_test(2):
                                    story("You are forced to take a breath of poison gas.")
                                    change_stats(0, 2, "subtract")
                                    change_stats(1, 3, "subtract")
                                    story("Your Skill is reduce by 2 and your Stamina\nis reduced by 3. You dash for the door.")
                                    decision_17 = "RETURN"
                                else:
                                    story("You make it across the room to the door.")
                                    decision_17 = "RETURN"
                            elif decision_18 == "LEAVE":
                                decision_17 = "RETURN"
                    if decision_17 == "RETURN":
                        story("You arrive back at the junction and this time turn right.")
                        decision_17 = "WEST"
                if decision_17 == "WEST":
                    story("Some way along the passage, the corridor bends round to the north\nand you follow it until you reach another junction.")                
                    story("At this junction you see an arrow cut into the rock,\npointing to the north, and you decide to try this direction.")
                    story("The passage runs northwards, and ahead you can har the splashings\nof an underground river. The air becomes cool and fresh.")
                    story("You soon reach a wide opening of a river bank but despair as\nyou look across to see no way through on the other side.")
                    story("To the east the river flows through a cave in the rock.")
                    decision_17 = story("Will you either REST, and eat Provisions or go what seems the only\nway forward, jumping into the river and SWIMming downstream?")
                    if decision_17 == "REST":
                        story("You squat on the sandy bank. As you prepare your meal you notice\ba movement in the sand a couple of metres to your left.")
                        story("The movement becomes quite turbulent and\nyou spring to your feet, sword at the ready.")
                        story("Suddenly a large tubular head breaks through the surface,\ntwists around in the air and picks up your scent.")
                        story("The smooth, segmented body of a Giant Sandworm\nrears up and sways over in your direction.")
                        story("As it does so, a large orifice, with short spiky teeth, opens in\nwhat must be its head. You must do battle with this creature.")
                        if fight("Giant Sandworm"):
                            take_provs()
                            story("Panting after the struggle, you sit down to collect\nyourself and finish the Provisions you started.")
                            story("Eventually you pack your bag and wade into the stream.")
                        elif vars.escape:
                            story("You Escape by diving into the river and swimming downstream,\nbut you have lost the Provisions you started to eat.")
                            vars.escape = False
                        decision_17 = "SWIM"
                    if decision_17 == "SWIM":
                        repeat_4()

def repeat_2():
    story("You enter another small room, bare except for a fountain in the middle.")
    story("Not a particularly grand affair, the fountain is a small carved fish,\nand a short jet of water comes from its mouth.")
    story("A wooden sign hangs from the fish and bears a message. It is\nwritten in Goblin tongue, at which you are not very proficient.")
    story("The first word you cannot understand, but the others read:\n'... not drink'. But you are extremely thirsty.")
    decision_16 = story("Will you DRINK from the fountain? Or PASS\nit by and leave through a door in the north wall?")
    if decision_16 == "DRINK":
        story("The water is refreshing. You feel a glow spreading through your\nbody as if you were drinking at the fountain of life.")
        change_stats(1, 4)
        change_stats(0, 11)
        change_stats(2, 11)
        story("Add 4 Stamina points, and restore your Skill\nand Luck score to their initial levels.")
        decision_17 = story("The fountain of life for you must be death for\nthe evil Goblins. Will you eat Provisions " + provs_tuto() + " here?")
        if decision_17 == "YES":
            change_stats(1, 4)
        story("When you have rested, leave through the north door.")
        decision_16 = "PASS"
    if decision_16 == "PASS":
        story("The door opens into a passage which you follow northwards.\nShortly you reach a bend and follow it round to the east.")
        decision_16 = story("Several metres on, you reach a junction at which\nyou may either go NORTH or continue EASTwards. Which will you choose?")
        if decision_16 == "EAST":
            story("The passage twists and turns and eventually ends in\na solid iron door. You listen but hear nothing.")
            decision_17 = story("Will you try to OPEN the door or you can go BACK to the junction.")
            if decision_17 == "OPEN":
                story("The room is unoccupied and there\nseems to be no other means of exit.")
                story("In the centre of the floor stands a table, and on this\ntable are two helments; one of bronze and one of iron.")
                story("Both are about your size. Will you:")
                decision_17 = story("Try on the BRONZE helmet?\nTry on the IRON helmet?\nRETURN to the junction?")
                if decision_17 == "BRONZE":
                    story("You place the helmet on your head. It fits well.\nSuddenly a searing pain flashes across your forehead.")
                    story("You cannot think straight. This helmet is cursed and,\ntry as you might, you cannot remove it!")
                    change_stats(0, 1, "subtract")
                    story("The pain soon subsides, but you still cannot shift\nthe helmet. You stagger back to the junction.")
                    decision_17 = "BACK"
                elif decision_17 == "IRON":
                    story("You place the helmet on your head. It fits well.")
                    story("A glow fills your body and you seem to possess a power\nand confidence neyond anything you have felt before.")
                    story("This helmet is blessed with magic and will allow you to\nadd 1 point to all future Attack Strengths.")
                    vars.equipment.append("Iron Helmet")
                    decision_16 = "BACK"
                if decision_17 == "RETURN":
                    decision_16 = "BACK"
            elif decision_16 == "BACK":
                story("You arrive back at the junction and this time turn northwards.")
                decision_16 = "NORTH"
        if decision_16 == "NORTH":
            decision_16 = story("Some way up, you reach another junction where you\nmay either go EASTwards or turn WESTwards. Which will you choose?")
            if decision_16 == "EAST":
                story("The passageway ahead widens and you can see ahead a large cavern.")
                story("As you shine your lantern you can see crude stone weapons\non the floor and a smouldering fire in the centre.")
                story("Back you see no way through.")
                story("As you turn to make your way back you stop in your tracks\nto see two Neanderthal Cavemen barring your exit.")
                story("They grunt aggressively at you. You draw your sword and must prepare to fight.")
                vars.monster = [7, 6]
                if fight("First Caveman"):
                    vars.monster = [6, 4]
                    if fight("Second Caveman"):
                        story("You leave the cavern and return to the junction to pregress westwards.")
                        decision_16 = "WEST"
            if decision_16 == "WEST":
                story("The passageway twists sharply northwards and ahead you can hear water flowing.")
                story("You eventually reach the south bank of an underground river.")
                story("As you stand on the pebbled bank you hear a fluttering and\nlook up to see three Giant Bats swooping down on you.")
                decision_16 = story("Will you FIGHT these three as a single creature or ESCAPE?")
                if decision_16 == "FIGHT":
                    vars.monster = [6, 6]
                    if fight("Giant Bats"):
                        story("You sheathe your sword and walk up to the water, wondering if its safe to swim.")
                        story("Although you cannot see any immediate danger, there is\nno way through on the north side of the river.")
                        story("You suddenly notice a gleaming sword lying on the river\nbed several steps in. You wade to retrieve it.")
                        story("it is light in your hand, far less cumbersome than\nyour own weapon, and it has a keen edge.")
                        story("This marvellous weapon will add 1 point to your Skill whilst you use it.")
                        vars.equipment.append("Good Sword")
                        decision_16 = story("A mysterious voice speaking in your mind seems to be\ntelling you to throw your own sword into the river. Will you?")
                        if decision_16 == "YES":
                            story("As your sword splashes into the water,\na bubbly voice says, 'Thank you!'")
                            story("It now seems that the only way onward is to swim\ndownstream to the east. You plunge into the water.")
                            decision_16 = "ESCAPE"
                        elif decision_16 == "NO":
                            story("As you put the two swords into your belt,\nyour new one seems to take on a mind of its own.")
                            change_stats(1, 1, "subtract")
                            story("It cuts your leg and, as you draw\nit out, it turns rubbery in your hand.")
                            vars.equipment.remove(vars.equipment.index("Good Sword"))
                            story("It's useless so you fling it into the river.\nIt seems the only way is for you to swim downriver.")
                            story("You plunge in and start swimming.")
                            decision_16 = "ESCAPE"
                    elif vars.escape:
                        repeat_4()
                        vars.escape = False
                elif decision_16 == "ESCAPE":
                    change_stats(1, 2, "subtract")
            if decision_16 == "ESCAPE":
                repeat_4()

def repeat_3():
    story("The passage ahead ends at a sturdy door. You listen but hear nothing.\nYou try the handle, it turns, and you enter the room.")
    story("As you look around you hear a loud cry from behind you and swing round to see a wild man leaping towards you wielding a large battle axe.")
    story("He is a mad barbarian and you must fight him!")
    vars.monster = [7, 6]
    if fight("Barbarian"):
        story("A room search reveals nothing of any value, although an old box contains\na wooden mallet and five stumps of wood, sharpened at one end.")
        decision_16 = story("Do you wish to take these?")
        if decision_16 == "YES":
            vars.equipment.append("Five Wooden Stumps")
        vars.escape = True
    if vars.escape:
        story("You leave through the door in the north wall.")
        story("The door opens into a short corridor which ends several metres ahead at another door, similar to the one you have just come through.")
        story("You listen and hear nothing. You try the handle and it turns, allowing you into another room of a similar size.")
        story("But this roon is splendidly decorated, with a polished marble floor and rough walls painted white.")
        story("On each of the four walls hangs a painting, and there is another door in the north wall.")
        decision_16 = story("Will you either go STRAIGHT through the room or you may stop to LOOK at the paintings.")
        if decision_16 == "LOOK":
            story("They are portaits of men. Your spine shivers as you read one nameplate\n- it is of Zagor, the Warlock whose treasure you are seeking.")
            story("You look at his portrait and realise you are pitting\nyourself against an awesome adversary.")
            story("You have the feeling that you are being watched and\nnotice the piercing eyes following you as you move.")
            story("You find yourelf drawn towards his portrait and you fear rises.\nDo you have enough courage to try to combat the Warlock.")
            decision_17 = story("Will you either ESCAPE through the north door or\nlook for a WEAPON to use against the Warlock's power?")
            if decision_17 == "ESCAPE":
                change_stats(1, 2, "subtract")
                decision_16 = "STRAIGHT"
            elif decision_16 == "WEAPON":
                if "Jewel" in vars.equipment:
                    story("You try various items of equipment against the gaze of the painting, but none seems to work. Which will you try of the following:")
                    if "Wooden Stake" in vars.equipment:
                        if "Cheese" in vars.equipment:
                            decision_17 = story("SLASH it with a swor?\nHold a JEWEL up at it?\nPLUNGE a wooden stake into it?\nThrow CHEESE at it?")
                        else:
                            decision_17 = story("SLASH the painting with a sword?\nHold a JEWEL up in front of it?\nPLUNGE a wooden stake into it?")
                    else:
                        decision_17 = story("Either SLASH the painting with your sword\nor hold a JEWEl up in front of it?")
                else:
                    story("You try various items against the gaze of the painting, but none work.\nNow you must try slashing it with your sword.")
                    decision_16 = "SLASH"
                if decision_16 == "SLASH":
                    change_stats(1, 1, "subtract")
                    story("The sword flies out of your hand, and you must leap aside as\nit comes down on you. It grazes your cheek as it falls.")
                    change_stats(0, 1, "subtract")
                    story("You decide you'd better leave the room. Pick up your sword\nand lose 1 more Skill in fear of the Warlock's power.")
                    decision_16 = "STRAIGHT"
                elif decision_16 == "JEWEL":
                    story("If you have the jewel from the Eye of the Cyclops,\nyou hold it in front of the Warlock.")
                    story("His intimidating stare turns to an expression of pain.\nHe obviously feels the jewel's power.")
                    story("Suddenly his eyes turn white and he goes limp. Your confidence\ngains as you realise you have won your first real battle.")
                    story("You put the jewel into your pack and leave through the north door.")
                    decision_16 == "STRAIGHT"
                elif decision_16 == "PLUNGE":
                    story("As you attack the portrait with the wooden stake, you feel a wrench of pain in your wrist.")
                    story("You are forced by some unseen power to drop the stake. You decide to run and leave through the north door.")
                    change_stats(0, 1, "subtract")
                    story("You lose 1 more Skill in awe of the Warlock's power.")
                    decision_16 = "STRAIGHT"
                elif decision_16 == "CHEESE":
                    story("The Cheese hits the portrait and bounces off. You hear an\nevil laugh and realise the Warlock is mockicking you.")
                    story("You decide to leave the room by the north door.")
                    decision_16 = "STRAIGHT"
        if decision_16 == "STRAIGHT":
            story("You open the door into a narrow passage and follow it northwards.\nSome metres up, it turns to the east, then to the north.")
            story("However, at this second bend, there is a small alcove\nin the rock. It seems a convenient hiding place.")
            decision_16 = story("Do you wish to eat Provisions?")
            if decision_16 == "YES":
                vars.provs -= 1
                change_stats(1, 4)
            story("When you have rested, continue northwards.")
            story("The passageway ends in another wooden door,\nthis time a small one with a carved bone handle.")
            story("You listen but hear nothing coming from inside.")
            story("You try the handle and the door opens into a pear-shaped room with\na rough stone floor, making walking across it somewhat awkward.")
            story("In one corner is a pile of rubble, mainly stones and dust, but there\nare also two odd-shaped pieces of wood and a length of rope.")
            story("A door in the north wall leads on. Will you:")
            decision_16 = story("Examine the bits of WOOD?\nStudy the length of ROPE?\nLEAVE through the north door?")
            if decision_16 == "WOOD":
                story("Both pieces of wood are Y-shaped and smooth,\nas if washed up from a river.")
                vars.equipment.append("Pieces Of Wood")
                decision_17 = story("If you wish to take the pieces of wood you must\nchoose one item of equipment to leave behind. Which will you choose?")
                while decision_17 not in vars.equipment:
                    decision_17 = story("You don't have that. Which piece of equipment will you choose from your pack.")
                vars.equipment.remove(vars.equipment.index(decision_17.title()))
                decision_16 = story("Will you either LEAVE through the north door or stay and examine the ROPE?")
            if decision_16 == "ROPE":
                story("You pick up the rope. It looks normal. In fact it looks as if\nit might be quite useful. You open your pack to put it in.")
                story("Suddenly, it comes alive in your fingers, snakes up your arm\nand attempts to wrap itself around your neck.")
                story("You struggle to cut the rope with your sword\nbefore its grip tightens. Test your Luck.")
                dice_num = randint(2, 12)
                change_stats(2, 1, "subtract")
                while dice_num > vars.hero[2]:
                    change_stats(1, 1, "subtract")
                    story("You are unlucky so the rope tightens.\nYou must Test your Luck again.")
                    dice_num = randint(2, 12)
                    change_stats(2, 1, "subtract")
                story("You cut the rope and it drops to the ground.\nYou may leave through the north door.")
                decision_16 = "LEAVE"
            if decision_16 == "LEAVE":
                story("The passage ahead leads you northwards. The rocky floor becomes\nsandy until eventually you are walking on a sort of coarse sand.")
                story("The passage widens and you can hear water. You continue until\nyou find yourself in a large cavern through which a river flows.")
                vars.river = True
        vars.escape = False

def repeat_4():
    story("The current is strong and takes you swiftly downstream.")
    story("You are washed out into a large cavern with banks on both sides.\nThe current washes you on to the south bank.")
    vars.river = True

if __name__ != "__main__":
    raise Exception

vars.background = "mountain"
story("Welcome to Firetop Mountain.")
story("You have in your possession a sword and a shield\ntogether with a rucksack containing Provisions for the trip.")
story("You have been preparing for this quest but to see how successful you have been\nyou must use the dice to determine your initial Skill, Stamina and Luck scores.")
story("Roll 1 die to determine your Skill score.")
dice_num = randint(1, 6)
vars.hero[0] = dice_num + 6
vars.init_hero = [vars.hero]
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
vars.monster = [9, 9]

vars.background = "passage"
decision_1 = story("You enter the caverns of Firetop Mountain and within a few metres\nyou arrive at a junction, do you want to go EAST or WEST?")
if decision_1 == "EAST":
    vars.background = "door"
    decision_2 = story("The passageway soon comes to an end at a locked wooden door.\nYou listen at the door but hear nothing. Will you try to charge it down?")
    if decision_2 == "YES":
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
    elif decision_2 == "NO":
        vars.background = "passage"
        story("You turn around and head back to the junction.")
    vars.background = "archtooutside"
    story("You arrive back at the junction. You look left to see the\ncave entrance in the dim distance but walk straight on.")
    decision_1 = "WEST"
    
if decision_1 == "WEST":
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
    decision_3 = story("You listen at the door and can hear a rasping sound which\nmay be some kind of creature snoring. Do you want to open the door?")
    
if decision_3 == "YES":
    vars.background = "darkroom"
    story("The door opens to reveal a small, smelly room. In the centre is a rickety\nwooden table on which stands a lit candle. Underneath is small wooden box.")
    vars.background = "sleepingorc"
    story("Asleep on a straw mattress is a short, stocky creature; the same sort of\ncreature you found at the sentry post. He must be the night watch guard.")
    decision_4 = story("You may either RETURN to the corridor and press on northwards\nor will you creep into the room and try to STEAL the box?")
    if decision_4 == "RETURN":
        vars.background = "passage"
        decision_3 = "NO"
    elif decision_4 == "STEAL":
        story("Test your Luck.")
        if stat_test(2):
            story("He doesn't wake up.")
            vars.background = "box"
            story("You leave the room and open the box in the passage. Inside you find a single Piece of Gold\nand a small mouse, which must've been the creature's pet.")
            vars.gold += 1
            vars.background = "mouse"
            story("You keep the coin and release the mouse which scurries off down the passageway.")
            vars.hero[2] += 2
            story("You gain 2 Luck points.")
            decision_3 = "NO"
        else:
            vars.background = "orc"
            story("The sleeping creature awakens startled.\nHe jumps up and rushes at you unarmed.")
            decision_4 = story("With your sword you should be able to defeat him but his teeth look vicious.\nWill you ESCAPE or FIGHT the Orc who is attacking you?")
            if decision_4 == "ESCAPE":
                change_stats(1, 2, "subtract")
                vars.background = "passage"
                story("You run out of the room and slam the door shut\nbut the Orc has scratched you with its teeth.")
                story("You turn northwards up the passageway passing a similar-looking door further up.")
                decision_3 = "NO"
            elif decision_4 == "FIGHT":
                fight_tuto()
                vars.monster = [6, 4]
                if fight("Orc"):
                    vars.background = "passage"
                    story("You leave and open the box in the passage. Inside you find a single Piece of Gold\nand a small mouse, which must have been the creature's pet.")
                    vars.gold += 1
                    vars.background = "mouse"
                    story("You keep the coin and release the mouse which scurries off down the passageway.")
                    vars.hero[2] += 2
                    story("You gain 2 Luck points.")
                    decision_3 = "NO"
        
if decision_3 == "NO":
    vars.background = "door"
    decision_5 = story("Further up the passage along the west wall you see another door.\nYou listen at it but hear nothing. Do you want to try opening the door?")
  
if decision_5 == "YES":
    vars.background = "room"
    story("The door opens to reveal a small room with dirty walls. In the centre\nof the room is a makeshift wooden table on which is standing a lit candle.")
    decision_6 = story("Under the table is a small box.\nWill you either OPEN the box or LEAVE the room?")
    if decision_6 == "OPEN":
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
            decision_5 = "NO"
    elif decision_6 == "LEAVE":
        decision_5 = "NO"

if decision_5 == "NO":
    vars.background = "door"
    story("Further up the passage on the west wall you see another similar door. You listen\nand grimace to hear the worst singing you have ever heard in your life!")
    decision_7 = story("Do you want to go into the room to investigate this hideous din?")

if decision_7 == "YES":
    vars.background = "room"
    story("The door opens to reveal a small, unkempt room. In the centre\nis a wooden table upon which a candle burns, lighting the room with its flickering flame.")
    story("A small box rests under the table. Seated around the table are\ntwo small creatures with warty skin, dressed in leather armour.")
    story("They are drinking some sort of grog and, by the way they stagger to their feet\non your arrival, you assume they are very drunk.")
    decision_8 = story("Will you either draw your sword and LEAP forward at them\nor slam the door quickly and RUN on up the passage?")
    if decision_8 == "LEAP":
        story("The two drunken Orcs you now face are obviously startled at your entrance and,\nas quickly as they are able, they fumble around for their weapons.")
        story("You must attack each one in turn. Their drunkenness allows you to\nadd 1 to your dice roll when working out your Attack Strength.")
        #make work
        fight_tuto()
        vars.background = "orc"
        vars.monster = [5, 4]
        if fight("First Orc"):
            vars.monster = [5, 5]
            if fight("Second Orc"):
                story("You wipe your bloodied sword on the mattress. The green blood\nleaves a slimy stain on the straw mattress.")
                vars.background = "box"
                story("Stepping over the bodies towards the table, you pick up the box from under the table\nand examine it. It is a small wooden box with crude hinges.")
                decision_8 = story("The name Farrigo Di Maggio is inscribed on a brass namplate on its lid.\nDo you wish to OPEN the box or LEAVE it behind?")
                if decision_8 == "OPEN":
                    vars.background = "book"
                    story("The box contains a small leather-bound book entitled 'The Making and\nCasting of Dragonfire'. You open the pages and begin to read.")
                    story("Fortunately it's written in your language and probably not understood by Orcs\n- or it would certainly not be as loosely guarded as it was.")
                    story("The book is written in tiny writing by Farrigo Di Maggio.\nHe tells the story of his life's work; creation of the Dragonfire spell.")
                    story("You read how, in his last years, Farrigo finally perfected his spell\nto fight Dragons but by then was too old to make use of it.")
                    story("So he completed his book and hid it in the depths of Firetop Mountain\nafraid it might fall into the wrong hands. The last page reads:")
                    story("And so, you who hold this book,\nyou have my life's work in your hands.\nThe power of destruction is yours if you wish it,\nbut do not waste it.")
                    story("Unless you use it for which it was intended,\nyou shall be consumed by evil itself\nand die by the fire from your own hands.")
                    story("Remember, only when the Dragon breathes fire at you\nshould you raise your arms and say:\nEkil Erif, Ekam Erif, Erif Erif, Di Maggio.")
                    story("You say these words slowly and softly. Suddenly the pages seem to glow\nand as this glow disappears, so do the words on the pages of the book.")
                    vars.equipment.append("Dragonfire spell")
                    story("You repeat the spell to yourself to memorise it and leave the room.")
                    decision_7 = "NO"
                elif decision_8 == "LEAVE":
                    decision_7 = "NO"
    elif decision_8 == "RUN":
        decision_7 = "NO"
        
if decision_7 == "NO":
    background = "passage"
    decision_8 = story("You eventually arrive at the end of the passage, at a three-way junction.\nWill you turn either to the WEST or to the EAST?")
    if decision_8 == "WEST":
        vars.background = "door"
        story("The passageway runs straight for several metres and then ends in a wooden door.\nYou listen at the door and hear angry shouting coming from within.")
        decision_8 = story("Will you investigate?")
        if decision_8 == "YES":
            vars.background = "room'jpg"
            story("You open the door to a large room. A large chair behind a solid-looking table\nsuggests to you that someone, or something, of rank uses this room.")
            story("A chest in the centre catches your eye. In the corner stands a\nman-sized creature with a warty face, standing over a small creature of similar race.")
            story("With the whip in his hand, the Orc Chieftain has been beating his servant,\nwho is whimpering beneath him. Will you:")
            decision_9 = story("Attack them BOTH?\nSpring at the CHIEFTAIN in the hope his servant will aid you?\nLEAVE the room and head back for the junction?")
            if decision_9 == "CHIEFTAIN":
                vars.background = "orc"
                story("As you spring at the Chieftain, his servant rises to his feet, picks up a hefty club\nand joins the melee. But to your horror he attacks you!")
                decision_10 = story("Seeing this will you ESCAPE through the door down the corridor or CONTINUE the fight.")
                if decision_10 == "ESCAPE":
                    change_stats(1, 2, "subtract")
                    if vars.hero > 0:
                        story("The Chieftain gets a hit on you as you Escape.")
                        decision_8 = "BACK"
                elif decision_10 == "CONTINUE":
                    decision_9 = "BOTH"
            if decision_9 == "BOTH":
                vars.background = "orc"
                fight_tuto()
                story("The battle commences!")
                vars.monster = [7, 6]
                if fight("Orc Chieftain"):
                    vars.monster = [5, 3]
                    if fight("Servant"):
                        story("The green blood of the dead Orcs smells foul as it seeps from their bodies.\nYou step around the corpses and investigate the chest.")
                        vars.background = "box"
                        story("It is a sturdy affair, made of strong oak and iron, and it is firmly locked.")
                        decision_9 = story("Will you try to SMASH the lock with your sword\nor leave it alone and GO through the open door.")
                        if decision_9 == "SMASH":
                            story("The lock was obviously inadequate; it flies off\nand lands on the floor several metres away.")
                            story("You lift up the heavy lid and your eyes widen as you see the gold sheen\ncoming from within. A fair number of Gold Pieces are inside.")
                            story("In a corner lies a small black bottle with a tight stopper,\ncontaining some kind of liquid. Also in the chest is a silky black glove.")
                            story("But as you are admiring this treasure you hear a soft click and\nwince in pain as a small dart shoots forward into your stomach.")
                            story("Roll a die to determine the effect of the poison on the dart tip.")
                            dice_num = randint(1, 6)
                            change_stats(1, dice_num)
                            if vars.hero[1] > 0:
                                story("You sink to the floor. You pull the dart out and decide to bandage the wound.\nThis gives some relief, but you still feel weak.")
                                story("You decide to take it easy and examine the contents of the chest.")
                                decision_9 = story("Do you wish to eat some Provisions" + provs_tuto() + " here?")
                                if decision_9 == "YES":
                                    take_provs()
                                    story("Your Stamina is restored.")
                                story("There are 25 Gold Pieces and the bottle label shows it to be a\nPotion of Invisibility, good for one dose. The glove is a mystery.")
                                vars.gold += 25
                                vars.equipment.append("Invisibility Potion")
                                vars.equipment.append("Silk Glove")
                                story("You put all of these into your haversack and leave the room.")
                                decision_8 = "NO"
                        elif decision_9 == "GO":
                            decision_8 = "NO"
            elif decision_9 == "LEAVE":
                decision_8 = "NO"
        if decision_8 == "NO":
            vars.background = "passage"
            story("You arrive back at the junction in the passage and walk straight on eastwards.")
            decision_8 = "EAST"
    if decision_8 == "EAST":
        decision_11 = story("You arrive at another junction in the passage.\nWill you either go NORTHwards or continue WESTwards?")

if decision_11 == "WEST":
    vars.background = "door"
    story("The passage ends at a solid wooden door with metal hinges. Listening at the door,\nyou hear strange mutterings and the clatter of what could be pots and pans.")
    decision_12 = story("Whatever is in there, there are several of them.\nDo you want to go through the door?")
    if decision_12 == "YES":
        vars.background = "fiveorcs"
        story("You open the door into a large room which can only only be the dining room\nof the same warty-faced creatures you now recognise.")
        story("Sitting around a large table are five Orcs busily drinking\nand dribbling their bowls of rat-gizzard soup.")
        story("All are involved in a rowdy arguement as to who will get to chew the rat bones\nleft in the large soup cauldron, so they do not see you enter.")
        decision_13 = story("Will you be bold and prepare to ATTACK them or, if you don't relish the prospect\nof taking on five of these creatures, try to ESCAPE?")
        if decision_13 == "ESCAPE":
            story("Test your Luck.")
            if stat_test(2):
               decision_12 == "NO"
            else:
                #explanation
                decision_13 = "ATTACK"
        if decision_13 == "ATTACK":
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
                                decision_13 = story("But under the serving hatch you find a thin leather\ncase half a metre long. Do you want to open it?")
                                if decision_13 == "YES":
                                    story("The case opens easily and inside you find a magnificent bow and one silver arrow.")
                                    story("An inscription on the case says: 'The giver of sleep to those who never can'.")
                                    decision_13 = story("Do you want to eat Provisions" + provs_tuto() + "here?")
                                    if decision_13 == "YES":
                                        take_provs()
                                    change_stats(2, 1)
                                    vars.equipment.append("Bow and arrow")
                                    story("You put the bow, arrow and case in your pack and leave the room.")
                                    decision_12 = "NO"
                                elif decision_13 == "NO":
                                    story("You leave it behind and walk out of the door.")
                                    decision_12 = "NO"
    if decision_12 == "NO":
        vars.background = "passage"
        story("You move swiftly down the passage and arrive back\nat the junction. You turn northwards this time.")
        decision_11 = "NORTH"

if decision_11 == "NORTH":
    vars.background = "door"
    story("You see a well-used door on the right-hand(east) side of the passageway.\nWith your ear to the keyhole, you hear a man screaming for help from inside.")
    decision_11 = story("Will you OPEN the door or WALK on?")
    if decision_11 == "OPEN":
        story("The door is locked so you try to charge it down. Test your Skill.")
        if not stat_test(0):
            story("The door remains locked, you bruise your\nshoulder and you must progress up the passage.")
            decision_11 = "WALK"
        else:
            vars.background = "darkroom"
            story("The locked door bursts open and a nauseating stench hits your nostrils.\nInside, the floor is covered with bones, rotting vegetation and slime.")
            story("A wild-haired old man, clothed in rags, rushes at you screaming.\nHis beard is long and grey, and he is waving an old wooden chair-leg.")
            decision_12 = story("Is he as insane as he appears, or is this some kind of trap?\nWill you either SHOUT to try to calm him down or draw your sword and ATTACK.")
            if decision_12 == "SHOUT":
                story("You shout: 'You are freed, old man!' at the top of your voice.\nInstantly, his rantings cease. He stops and sinks to the floor, weeping loudly.")
                story("As he composes himself, he thanks you many times. You talk in the hope of\ndiscovering secrets of the mountain and he begins to tell his story.")
                story("Many years ago he was an adventurer like you\nin search of the Warlock's treasure.")
                story("He was captured by Orcs and thrown into his\nsolitary cell as a sort of pet for the creatures.")
                story("You ask whether he would like to accompany you into the mountain,\nbut he simply wants to leave and see the world again.")
                story("You ask him for advice but he says he knows little.\nHe advises you to pay your respects to the boatman.")
                story("He tells you that you must pull the right-hand lever on the wall ahead\nto open the iron gate at the end of the passage.")
                story("He has also learned that the keys to the Boat House are guarded by a\nman and his dog. You shake hands, leave the room and go your separate ways.")
                decision_11 = "WALK"
            elif decision_12 == "ATTACK":
                story("You lunge at the old man as he leaps towards you with outstretched arms\n- and run him through the chest with your sword.")
                story("You curse as you realise he was making no attempt to attack; his wild excitement\nmust merely have been relief after being imprisoned for so long.")
                story("You will now get no information out of him on the perils of\nthe adventure ahead. You progress up the passageway.")
                vars.background = "passage"
                decision_11 = "WALK"
    if decision_11 == "WALK":
        vars.background = "door"
        decision_14 = story("Further up the passage you see a door in the east wall. You listen hard\nbut can hear no sound. Do you want to investigate?")

if decision_14 == "YES":
    decision_13 = story("The door is firmly locked. You may try to force it open, will you?")
    if decision_13 == "YES":
        story("You charge at the door, hitting it squarely with your shoulder. Test your Skill.")
        if not stat_test(0):
            change_stats(1, 1, "subtract")
            story("The door shudders but does not budge\nand you wince in pain.")
            vars.background = "passage"
            story("You continue up the corridor.")
            decision_13 = "NO"
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
                decision_15 = story("However, the shield is heavy so you must choose a piece of\nequipment to leave behind. Which will you pick?")
                while decision_15.title() not in vars.equipment:
                    decision_15 = story("You don't have that. Which piece of equipment will you choose from your pack?")
                vars.equipment.remove(decision_15.title())
            story("You now leave the room and continue up the corridor.")
            decision_14 = "NO"
            #why on earth does this not work now *sigh

if decision_14 == "NO":
    vars.background = "door"
    story("On the east wall of the passage you see another door, this time made of solid metal.\nListening at the door you hear tortured screams coming from within.")
    decision_14 = story("Do you wish to try opening the door?")
    if decision_14 == "YES":
        vars.background = "room"
        story("The door is not locked and opens. The room in front of you seems to be a\nsmall torture chamber, with various torture devices around the walls.")
        story("In the centre, two small, hunchbacked creatures are having their fiendish way\nwith a Dwarf, who is tied to a hook in the ceiling by his wrists.")
        story("The two hunchbacks are poking and cutting him viciously with their swords.\nThe Dwarf lets out a final scream and falls silent, eyes closed.")
        story("His captors make disappointed noises and look round angrily as if it were\nyour fault that the Dwarf has collapsed. You must act quickly. Will you:")
        decision_15 = story("CLOSE the door quickly and continue on?\nDraw your sword and FIGHT?\nJAB the Dwarf with your sword and put on an evil laugh?")
        if decision_15 == "CLOSE":
            decision_14 = "NO"
        elif decision_15 == "FIGHT":
            story("These two evil creatures are Goblins.\nThey attack you one at a time.")
            vars.monster = [5, 5]
            if fight("Goblin"):
                if fight("Goblin"):
                    story("You cut down the Dwarf. He is, as you guessed, dead. Going through the\nGoblins' pockets, you find a large piece of sweet-smelling Cheese.")
                    story("You put it in your pack and leave the room northwards.")
                    vars.equipment.append("Cheese")
                    decision_14 = "NO"
        elif decision_15 == "JAB":
            story("The two Goblins look at each other amazed. They chatter to themselves and\nthen indicate for you to wait while they go off and get another Dwarf.")
            story("They disappear out of the room and you cut down the Dwarf who is, as you guessed,\nquite dead. You decide it best to leave and press on northwards.")
            decision_14 = "NO"
    if decision_14 == "NO":
        vars.background = "passage"
        story("You arrive at the passage's end, where it meets another going east-west.\nAn iron portcullis blocks your way and no amount of charging will budge it.")
        decision_16 = story("On the wall are two levers and it seems these have something to do\nwith the portcullis. Do you wish to pull the RIGHT or LEFT lever?")

if decision_16 == "LEFT":
    story("To your horror, you realise that\nthis dummy lever was a trap!")
    story("Although it looked like a handle, it was in fact a wax-coated sword blade and\nit has now cut your hand badly. Did you use your right or left hand.")
    story("Roll one die.")
    dice_num = randint(1, 6)
    if dice_num % 2 == 1:
        change_stats(0, 3, "subtract")
        change_stats(1, 1, "subtract")
        story("Your roll is odd so this was your sword hand and your fighting prowess\nis severely hampered.")
    else:
        change_stats(0, 1, "subtract")
        change_stats(1, 2, "subtract")
        story("Your roll is even so you used your non-sword hand,\nand the injury is not quite so important.")
    story("You now pull the right lever.")
    decision_16 = "RIGHT"

if decision_16 == "RIGHT":
    story("You hear a deep rumbling noise and the ground begins to shudder.\nSlowly and noisily the portcullis rises into the celing.")
    decision_16 = story("You may now walk to the junction.\nWill you turn WEST or EAST?")
    if decision_16 == "WEST":
        decision_16 = story("Shortly you arrive at another junction where you may go either\nstraight ahead WESTwards or turn NORTHwards. Which will you choose?")
        if decision_16 == "NORTH":
            story("The passage runs for some distance northwards and then starts to open into a\nlarge cavern with rough walls. There appears to be no way through.")
            decision_17 = story("Will you RETURN to the junction or ENTER the cavern?")
            if decision_17 == "ENTER":
                story("As you enter the cavern you hear loud footsteps, crunching heavily on the\nrocky floor. You crouch down beside the entrance in a small alcove.")
                story("The steps get louder and you see\na great Ogre enter the cavern!")
                story("He stands over two metres tall and is dressed in ill-fitting garments\nmade from some sort of hide. He carries a large wooden club. Will you:")
                decision_18 = story("ATTACK him as he enters?\nTry to CREEP out without him noticing?\nTry to DISTRACT him by throwing something into a far corner?")
                if decision_18 == "CREEP":
                    story("Test your Luck.")
                    if not stat_test(2):
                        story("You curse as you kick a small stone\nwhich goes skidding across the floor.")
                        story("You draw your sword in case the Ogre has heard it.")
                        decision_17 = "ATTACK"
                    else:
                        story("You creep down the corridor back to the crossroads.")
                        decision_17 = "RETURN"
                elif decision_18 == "DISTRACT":
                    if len(vars.equipment) == 0:
                        if vars.gold > 0:
                            vars.gold -= 1
                            story("You open your pack and reach inside for a Gold Piece.\nYou throw it across the cavern where it lands with a clatter.")
                            story("The Ogre looks towards the noise, and goes over to investigate.\nMeanwhile you creep out, down the passage and back to the junction.")
                            decision_17 == "RETURN"
                        else:
                            story("You open your pack and find nothing to throw.\nYou must now fight the Ogre.")
                            decision_18 = "ATTACK"
                    elif len(vars.equipment) == 1:
                        story("You open your pack and reach inside for the " + str(vars.equipment[0]) + ".\nYou throw it across the cavern where it lands with a clatter.")
                        story("The Ogre looks towards the noise, and goes over to investigate.\nMeanwhile you creep out, down the passage and back to the junction.")
                        vars.equipment.remove[0]
                    else:
                        decision_18 = story("You open your pack and reach inside for something\nsuitable to throw. Which item will you choose to throw?")
                        while decision_18 not in vars.equipment:
                            decision_18 = story("You don't have that. Which piece of equipment will you choose from your pack?")
                        vars.equipment.remove(decision_18.title())
                        story("You throw the " + decision_18 + " across the cavern\nwhere it lands with a clatter.")
                        story("The Ogre looks towards the noise, and goes over to investigate.\nMeanwhile you creep out, down the passage and back to the junction.")
                        decision_17 == "RETURN"
                if decision_18 == "ATTACK":
                    story("You draw your sword, and as you do so\nthe Ogre hears you and prepares to attack.")
                    vars.monster = [8, 10]
                    #escape after 2nd round
                    if fight("Ogre"):
                        vars.equipment.append("9 key")
                        story("The slain creature crashes to the ground. You go through his garments\nand find nothing, but a small pouch hangs around his neck.")
                        story("Inside this pouch is a small bronze key, with the number 9 cast into it.\nNothing else is of value so you head back to the junction.")
                        decision_17 == "RETURN"
            if decision_17 == "RETURN":
                story("You arrive back at the junction and turn westwards.")
                decision_16 = "WEST"
        if decision_16 == "WEST":
            story("The passageway continues westwards and then turns due north. Some way up,\nyou reach a junction where a narrow passage runs off to the west.")
            decision_16 = story("Will you continue NORTHwards or take the WEST way?")
            if decision_16 == "NORTH":
                story("Several metres up the passageway you arrive at a\njunction where you may turn either west or east.")
                repeat_1()
                decision_16 = "NO"
            elif decision_16 == "WEST":
                story("As you walk along the corridor, you see that it's getting narrower.\nAt one point you stoop, and as you do so, a deep, resonating laugh starts up.")
                decision_16 = story("Do you wish to continue?")
                if decision_16 == "YES":
                    story("The narrow passageway eventually becomes too small for you to walk along.\nYou get down on your hands and knees, and crawl.")
                    story("Eventually, there seems to be no way through, so you decide\nto return to the main passage. You head for the junction.")
                    decision_16 = "NO"
                if decision_16 == "NO":
                    story("You arrive back at the junction and turn northwards. Several metres up\nyou arrive at a junction where you may turn either west or east.")
            if decision_16 == "NO":
                repeat_1()
    elif decision_16 == "EAST":
        story("Cautiously you creep along the passageway.\nAfter a short time it turns sharply to the north.")
        story("At the corner there's a bench of solid wood\nand a sign reads 'Rest Ye Here Weary Traveller'.")
        decision_16 = story("Do you want to eat Provisions" + provs_tuto() + " here?")
        if decision_16 == "YES":
            take_provs()
            story("As you sit on the bench and eat, you begin to feel deeply relaxed and the\naches from your body seem to sooth themselves away. This place is enchanted")
            story("You restore 2 additional Stamina as well\nas the normal amount and 1 Skill point.")
            decision_16 = "NO"
        if decision_16 == "NO":
            decision_16 = story("You arrive at another junction in the passageway.\nWould you like to turn WEST or EAST?")
            if decision_16 == "WEST":
                story("You follow the passage westwards, then it turns sharply to the north and,\nsome metres further on, a passage runs off to the west.")
                decision_16 = story("Would you like to go along the WESTwards passage or carry on NORTHwards?")
                if decision_16 == "WEST":
                    story("As you walk, it visibly widens and eventually you find yourself\nstanding at the mouth of a rough cavern, a natural cave in the rock.")
                    story("As you look into the darkness, the cavern appears\nto be about 30 metres deep, with no visible exit.")
                    decision_16 = story("Do you want to go INTO the cavern or go BACK to the junction?")
                    if decision_16 == "INTO":
                        story("You enter the cavern and look around to see dozens of beautifully\ncoloured stalactites and stalagmites bordering the perimeter.")
                        story("Numerous drips can be heard, but the\nwhole place seems like a magic grotto.")
                        story("Near the back of the cavern, you come across a pair of boots,\nwhich seem to have been made quite recently. Will you:")
                        decision_17 = story("CONTINUE investigating the cavern?\nTry on the BOOTS?\nLEAVE the cavern and return to the junction?")
                        if decision_17 == "CONTINUE":
                            story("As you investigate, you hear a scurry of steps behind you and\nswing round to face the grotesque black shape of a Giant Spider.")
                            story("The Spider's body is at least a metre wide and\nyou quickly draw your sword to defend yourself.")
                            if fight("Giant Spider", 2):
                                story("Apart from the boots, which you ignore, there is little of\nvalue in the cavern. You decide to head back the way you came.")
                            if vars.escape == True:
                                story("You Escape from the fight down the passageway.")
                            decision_17 = "BACK"
                            vars.escape = False
                        elif decision_17 == "BOOTS":
                            story("The boots are well-fashioned in a deep red leather.\nThey are much sturdier than your own and fit you well.")
                            story("You try a few steps but are horrified to find that you cannot move,\nand the boots seem to grip your feet with considerable force.")
                            story("As you struggle to free yourself, you hear a crack\nand a smash as a stalactite falls from the roof.")
                            story("You crane round to see a large black shape shifting\ntowards you. As it approaches you turn cold.")
                            story("Several metres away is a Giant Spider advancing on spindly legs,\nmandibles clicking nervously in anticipation of its next meal.")
                            story("You draw your sword to defend yourself as it stalks you.\nYou cannot move and thus must subtract 2 from each dice roll.")
                            #make work
                            if fight("Giant Spider"):
                                story("Almost exhausted after your awkward fight with the Spider,\nyou set to work on hacking the boots off with your sword.")
                                story("Eventually they come free and you may leave the cavern\ndown the passageway and back to the junction.")
                                decision_17 = "BACK"
                        if decision_17 == "LEAVE":
                            decision_17 = "BACK"
                    if decision_17 == "BACK":
                        story("You arrive back at the junction and this time turn northwards.")
                        decision_16 = "NORTH"
                if decision_16 == "NORTH":
                    story("A rough timber doorway is on the wast wall of the passage.\nYou listen at the door and can hear a jolly sort of humming sound.")
                    decision_16 = story("Do you want to KNOCK on the door and\ngo in or will you CONTINUE northwards?")
                    if decision_16 == "KNOCK":
                        story("A voice bids you 'Come in!' and you walk into a room furnished with a\ntable, shelves and the like, all of which have seen better days.")
                        story("Plates, bowls, cups and hundreds of old books line the shelves.")
                        story("In the midst of all this clutter, you see a little old man in a grubby white gown swaying to and fro in a rocking chair.")
                        story("He is still humming happily to himself, his eyes fixed on you, but seeming at peace with the world. He bids you 'Good day.' Do you:")
                        decision_17 = story("START to make conversation with him?\nDraw your sword and CHARGE at him?\nDecide not to waste time and LEAVE?")
                        if decision_17 == "START":
                            story("As you speak the old man rises to his feet.'Oh my, oh my,\na stranger!' he starts. 'Well, do come in, the shop is open.'")
                            story("'What can I get you? What would you like to buy? What takes\nyour fancy? Which way are you headed? North? Well?'")
                            story("You tell the old man your story. He listens intently and replies,\n'In that case you will undoubtedly need one of my Blue Candles.'")
                            story("'That will be 20 Gold Pieces please. Cash if you don't mind.\nYes, I know it's expensive but isn't everything these days?'")
                            if vars.gold > 19:
                                story("'I can guarantee it's still worth the price.\nYou might need it sooner than you think...'")
                                decision_17 = story("Will you decide to buy a candle?")
                                if decision_17 == "YES":
                                    vars.gold -= 20
                                    vars.equipment.append("Blue Candle")
                                story("You are getting a little tired of his constant prattling.\nYou leave the room and go northwards.")
                                decision_16 = "CONTINUE"
                            else:
                                story("You don't have enough Gold Pieces and you are getting a little\ntired of his prattling. You leave the room and go northwards.")
                                decision_16 = "CONTINUE"
                        elif decision_16 == "CHARGE":
                            story("He is a little startled, but simply raises his hand. As he does so,\nyou suddenly collide heavily into...apparently nothing.")
                            change_stats(2, 2, "subtract")
                            story("You sit on the floor in a heap, rubbing your nose. Lose 2 Stamina points.")
                            story("The old man chuckles and says, 'You poor fool. Did you think I was\ndefenceless in such a den of evil as this? Regret your folly.'")
                            story("You rise to your feet and return to the passageway, turning north up the corridor.")
                            decision_16 = "CONTINUE"
                        if decision_16 == "LEAVE":
                            decision_16 = "CONTINUE"
                    if decision_16 == "CONTINUE":
                        story("Northwards the passageway ends at a solid wooden door.\nYou listen at the door but can hear nothing.")
                        story("There appears to be no choice but to open the door and\nenter the room, which you do. It's a large square room.")
                        story("You flash your lantern around and glimpse its emptiness - although\nthere are murals on the wall - before your lantern suddenly dies.")
                        story("You try to re-light it, but it will not catch. In the\nblackness you hear a succession of frightfil noises.")
                        story("Howls, screams, cries and wails are getting louder and louder\nuntil they reach the pitch where you must cover your ears.")
                        if "Blue Candle" not in vars.equipment:
                            story("The ear-piercing sound gets louder and louder. The pain is\nunbearable. You grope in the dark for a wall. Do you head for:")
                            decision_16 = "STAY"
                        else:
                            story("You think back to the words of the old man.\n'You might need it sooner than you think...'")
                            story("You grope in your pack and pull out the candle.\nImmediately it lights iteself of its own accord.")
                            story("The howling stops and the room appears bathed in a blue light\nfrom the candle. On the walls the figures in the mural are moving!")
                            story("They are mouthing silent screams as if trapped in a two-dimensional hell.")
                            decision_16 = story("On the wall opposite is another door.\nWill you LEAVE through it or STAY to investigate?")
                            if decision_16 == "LEAVE":
                                repeat_2()
                            elif decision_16 == "STAY":
                                story("As you watch the living mural, you are unaware of the speed\nyour candle is burning. Suddenly it flickers and goes out!")
                                story("You again begin to hear the piercing screams\nand their pitch grows to an unbearable level.")
                                story("You drop to your knees clutching your ears and crawl towards\nthe wall. Which wall will you crawl towards:")
                        if decision_16 == "STAY":
                            decision_16 = story("The EAST wall?\nThe NORTH wall?\nThe WEST wall?")
                            if decision_16 == "EAST":
                                story("You run along the wall searching for a door but find none.\nYour ears are on fire with the agony!")
                                change_stats(0, 1, "subtract")
                                decision_16 = story("You may either try the WEST wall or the NORTH wall,\nbut you must find a way out soon! Which will you choose?")
                            if decision_16 == "WEST":
                                story("You grope along the wall but can find no way of escape.\nThe noise of causing you to scream in pain!")
                                change_stats(0, 1, "subtract")
                                decision_16 = story("Will you either try the EAST wall or the NORTH wall.")
                            if decision_16 == "NORTH":
                                story("You grope around the length of the wall and find a door.\nQuickly you fumble with the handle. It opens!")
                                repeat_2()
            elif decision_16 == "EAST":
                decision_16 = story("After a few metres you reach another three-way junction.\nWill you go either NORTHwards or EASTwards.")
                if decision_16 == "NORTH":
                    repeat_3()
                elif decision_16 == "EAST":
                    decision_16 = story("The passageway ends in a sturdy wooden door. Do you\nwant to try OPENing it or go back and try another ROUTE?")
                    if decision_16 == "OPEN":
                        story("The door opens and you enter a small room. Your eyes widen as you\nsee that the walls of the room are covered in ornate stonework.")
                        story("Mosaics and marble inlays give this room a\nkind of beauty you have never seen before.")
                        story("In a corner of the room is a large metal statue of a\none-eyed creature. In its single eye is a sparkling jewel.")
                        story("As there appear to be no other ways through the room, you will have\nto go back to the junction - but that large jewel is very tempting.")
                        decision_16 = story("Will you LEAVE it alone and go back to the junction\nor try to take the JEWEL with you?")
                        if decision_16 == "LEAVE":
                            decision_16 = "ROUTE"
                        elif decision_16 == "JEWEL":
                            story("You approach the statue cautiously. A scampering behind you\nmakes you flash around...but it is only a rat.")
                            story("You feel at the jewel but it is solidly in place. You work your\nsword in behind it and as you work, you hear an ominous creaking.")
                            story("To your horror the statue is beginning to move!\nYou jump down and draw your sword.")
                            story("The Iron Cyclops cranes its head round towards you\nand steps down from its pedestal. You must fight!")
                            vars.monster = [10, 10]
                            if fight("Iron Cyclops"):
                                decision_17 = story("You sit back and rest from the exhausting battle.\nDo you want to eat Provisions here?")
                                if decision_17 == "YES":
                                    take_provs()
                                story("You prise the jewel from the still statue.\nIt is heavy in your hand and is worth 50 Gold Pieces.")
                                story("As you explore the room and statue you notice\nthat one of its breastplate sections is loose.")
                                story("When you open this, a small key is inside.\nYou examine this and notice the number 111 on it.")
                                vars.hero[1] += 3
                                vars.equipment.append("Jewel")
                                vars.equipment.append("111 Key")
                                story("With a smile you put the jewel and the key in\nyour pack and set off back to the junction.")
                            elif vars.escape:
                                story("You run through the door back to the junction.")
                                vars.escape = False
                            decision_16 = "ROUTE"
                    if decision_16 == "ROUTE":
                        story("You arrive back at the junction and this time you turn northwards.")
                        repeat_3()
if vars.river:
    story("You are on the south bank of an underground river facing across its\nblack depths. There appear to be four ways of crossing.")
    story("To your left, a rusted bell bears the sign:\n'Ferry Service 2 Gold Pieces - Please Ring.'")
    story("There is a small raft in front of you with a long stick resting beside it:\nyou could punt across the river. A rickety old bridge crosses on the right.")
    story("If you don't trust any of these, you may swim.")
    decision_17 = story("Which will you choose?\nRING the bell\nPUNT the raft across\nrisk the BRIDGE\nSWIM")
    if decision_17 == "RING":
        #3
        pass
    elif decision_17 == "PUNT":
        #386
        pass
    elif decision_17 == "BRIDGE":
        #209
        pass
    elif decision_17 == "SWIM":
        #316
        pass

pygame.quit()
#you can face the Winged Gremlin twice
#add animations when changing stats
#make it so you can go to all 3 walls
#add sound
#add more images
#I've a feeling I'm missing a bit maybe with a vampire
#fix dice
#make escaping do what it says
#line 243, in change_stats
#    if vars.hero[stat] + amount > vars.init_hero[stat]:
#TypeError: '>' not supported between instances of 'int' and 'list'
#error after failing to get into shield room