from functions import *
import variables as vars

def checkpoint_8():
    vars.decision_48 = story("Set in the north wall is a small recess where you may eat\nProvisions without being seen. Do you wish to take Provisions?")
    if vars.decision_16 == "YES":
        vars.provs -= 1
        change_stats(1, 4)
    vars.decision_49 = story("Will you set off either EASTwards or WESTwards?")
    if vars.decision_49 == "WEST":
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
                vars.equipment.remove("Invisibility Potion")
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
                        vars.equipment.remove("Cheese")
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
                        vars.decision_50 = story("Here will you either go NORTHwards or turn to the EAST.")
                        if vars.decision_50 == "NORTH":
                            story("The passage widens and you see you are entering a large cavern.\nYou hear noises coming from ahead and proceed cautiously.")
                            story("As you approach, you make out a large figure and are overawed\nas you see this oversized human is at least three metres!")
                            story("Dressed in a leather tunic, the creature is\nabsorbed in a meal he is eating at a table.")
                            story("The cavern is at least a hundred metres across\nand must be the home of this Giant.")
                            story("A large table and two chairs are along one of the walls,\nand it is here that the creature sits.")
                            story("Intent on his meal(a large pig), he is unlikely to notice you.")
                            story("Around the cavern you can see his mattress, a great furry pelt,\nand a huge hammer, which you have no hope of budging.")
                            story("A fire burns in one corner, under a hole in the ceiling.\nThere appears to be no other way through the cavern.")
                            vars.decision_51 = story("Will you TAKE on this brute or RETURN to the junction?")
                            if vars.decision_51 == "TAKE":
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
                                        vars.decision_51 = "RETURN"
                                    elif vars.escape:
                                        story("You Escape down the passageway, where he will not be able to follow.")
                                        vars.escape = False
                                        vars.decision_51 = "RETURN"
                            if vars.decision_51 == "RETURN":
                                story("You arrive back at the junction and turn eastwards.")
                                vars.decision_18 = "EAST"
                        if vars.decision_50 == "EAST":
                            story("You arrive at another junction. An arrow on the wall points\nnorthwards and you decide to proceed in this direction.")
                            story("The passage runs northwards, and ahead you can har the splashings\nof an underground river. The air becomes cool and fresh.")
                            story("You soon reach a wide opening of a river bank but despair as\nyou look across to see no way through on the other side.")
                            story("To the east the river flows through a cave in the rock.")
                            vars.decision_52 = story("You may either REST, and eat Provisions or will yougo what seems\nthe only way forward, jumping in and SWIMming downstream?")
                            if vars.decision_52 == "REST":
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
                                vars.checkpoint = 11
        else:
            story("You manage to leap quickly backwards before a pit opens.\nYou had better return to the junction.")
            vars.decision_49 = "EAST"
    if vars.decision_49 == "EAST":
        story("You follow the passage eastwards for several metres,\nthen it turns to the north.")
        vars.decision_53 = story("Shortly you reach another junction where you may either go STRAIGHT\nor turn LEFT, into a passage that soon turns north. Which will you choose?")
        if vars.decision_53 == "STRAIGHT":
            story("The passage ends at a wooden door, trimmed in iron. Various inscriptions\nadorn the door, but none of this makes any sense to you.")
            vars.decision_54 = story("You listen, but hear nothing. Will you either\nOPEN the door or RETURN to the junction.")
            if vars.decision_54 == "OPEN":
                story("The door opens into a small room, comfortably furnished with a table,\nseveral chairs and a large bookcase which covers one wall.")
                story("Seated at the table is an old man with a long grey beard,\nand squatting on the old man's shoulder is a small winged beast.")
                story("This creature is no more tham six centimetres tall.\nIt has two arms and legs; its skin is a dusty grey colour.")
                story("It has tiny sharp white teeth and its wings are folded behind its back.")
                story("The old man says nothing as you walk in through the door,\nbut he beckons you over to sit down at the table.")
                story("He is tossing in his hand two small white objects. Will you:")
                vars.decision_55 = story("SIT down as he tells you?\nLEAVE the room and return to the junction?\nDraw your sword and RUSH forward?")
                if vars.decision_55 == "SIT":
                    story("The old man does not look up, but his devilish little pet eyes you\nsuspiciously and starts chattering in a small squeaky voice.")
                    if vars.gold > 0:
                        vars.decision_56 = story("The old man grunts and asks you whether you are game\nfor a wager. Will you ACCEPT, LEAVE or ATTACK him?")
                        #sus if you put attack
                        if vars.decision_56 == "ACCEPT":
                            while vars.decision_57 != "LEAVE":
                                vars.decision_57 = story("The old asks you your stake. How many gold pieces will you bet?", any_input=True)
                                while not vars.decision_57.isdigit():
                                    story("Choose a number.")
                                    vars.decision_57 = story("The old asks you your stake. How many gold pieces will you bet?", any_input=True)
                                while int(vars.decision_57) < 1 or int(vars.decision_57) > vars.gold:
                                    story("Bet between 1 and the number of Gold Pieces you have.")
                                    vars.decision_57 = story("The old asks you your stake. How many gold pieces will you bet?", any_input=True)
                                story("He tosses the white dice he has been\nplaying with to you and asks you to roll.")
                                vars.dice_roll = randint(2, 12)
                                vars.dice_roll2 = randint(2, 12)
                                story("You roll the dice")
                                if vars.dice_roll > vars.dice_roll2:
                                    story("The old man rolls " + str(vars.dice_roll2) + " so you win your stake.")
                                    vars.gold += int(vars.decision_19)
                                    vars.win = True
                                elif vars.dice_roll < vars.dice_roll2:
                                    story("The old man rolls " + str(vars.dice_roll2) + " so you lose your stake.")
                                    vars.gold -= int(vars.decision_19)
                                if vars.gold == 0:
                                    vars.decision_56 = "LEAVE"
                                    story("You have no Gold Pieces left so you must leave\nthrough the door and return to the junction.")
                                    break
                                vars.decision_20 = story("Will you CONTINUE betting or LEAVE\nthrough the door and return to the junction?")
                                if vars.decision_20 == "LEAVE":
                                    if vars.win:
                                        change_stats(0, 2)
                                        change_stats(1, 2)
                                        change_stats(2, 2)
                                        story("2 points are added to your Skill, Stamina and Luck scores.")
                                    vars.decision_56 = "LEAVE"
                                    break
                    else:
                        vars.decision_56 = story("The old man asks if you are game for a wager but you\nhave no Gold so will you either LEAVE or ATTACK him.")
                elif vars.decision_56 == "RUSH":
                    vars.decision_56 = "ATTACK"
                if vars.decision_56 == "ATTACK":
                    story("As you draw your sword, the Winged Gremlin flaps to the air and the man\nrushes to the bookshelf to escape through a secret door.")
                    story("But you must fight his pet.")
                    vars.monster = [5, 7]
                    if fight("Winged Gremlin"):
                        story("You search but try as you may you cannot find the switch for\nthe secret bookshelf door - the old man must have locked it.")
                        vars.gold += 5
                        story("You do find 5 Gold Pieces in a drawer in the table.\nYou decide to return to the junction to the south.")
                        vars.decision_56 = "LEAVE"
                if vars.decision_56 == "LEAVE":
                    story("You arrive back at the junction and this time take the passageway to the east.")
                    story("The passageway runs for several paces eastwards, then turns north.")
                    vars.decision_53 = "LEFT"
            elif vars.decision_54 == "RETURN":
                story("You arrive back at the junction and this time take the passageway to the east.\nIt runs for several paces eastwards, then turns north.")
                vars.decision_53 = "LEFT"
        if vars.decision_53 == "LEFT":
            story("The passageway ends in a door at which you listen but hear nothing.\nTrying the handle, the door opens to reveal a large, square room.")
            story("The room is completely bare, but the floor is covered in a mosaic of tiles.\nTwo shapes stand out; star tiles and hand tiles.")
            story("A door on the opposite wall is the only way through. Will you:")
            vars.decision_58 = story("WALK across the room?\nWalk across the room only stepping on STARS?\nWalk across the room stepping only on HANDS?")
            if vars.decision_58 == "WALK":
                story("Test your Luck three times.")
                change_stats(2, 1, "subtract")
                if not stat_test(2):
                    story("You are lucky.")
                    if not stat_test(2):
                        story("You are lucky.")
                        if not stat_test(2):
                            story("You make it across to the far door and can leave the room.")
                            vars.decision_58 = "STARS"
                        else:
                            story("You are unlucky and step on a hand tile.")
                            vars.decision_58 = "HANDS"
                    else:
                        story("You are unlucky and step on a hand tile.")
                        vars.decision_58 = "HANDS"
                else:
<<<<<<< Updated upstream
                    story("You are unlucky and step on a hand tile.")
                    vars.decision_58 = "HANDS"
            elif vars.decision_58 == "STARS":
                story("You tiptoe precariously across the room to the door in the\nnorth wall. You open the door and proceed through it.")
            if vars.decision_58 == "HANDS":
                story("The moment your foot touches a hand, you feel a vice-like grip\non your ankle and see a ghostly white hand gripping your leg.")
                story("You fight for your balance and manage to regain it.")
                story("But to your horror you see that, from every hand-shaped tile\nin the floor, a similar apparition has appeared.")
                story("The floor is now scattered with ghoulish hands, flexing and\nsnatching in the air. You draw your sword and chop at the hand.")
                vars.monster = [6, 4]
                if fight("Hand"):
                    story("The hand withers and shrinks back into the floor. At the same time,\nthe other hands stop dead and fade away down into the tiles.")
                    vars.hero[2] += 2
                    story("You decide this time to step on the star-shaped tiles, and step\ncarefully across to the door. The door opens. Add 2 Luck.")
                    vars.decision_58 = "STARS"
            if vars.decision_58 == "STARS":
                story("The passageway ahead runs northwards and you\nfollow this until you reach another junction.")
                vars.decision_59 = story("Here will you either continue NORTHwards or you may turn WESTwards?")
                if vars.decision_59 == "NORTH":
                    story("The passageway ends in a solid doorway and you are surprised to see\na leather skirt tacked along the bottom of the door")
                    vars.decision_60 = story("You listen but hear nothing. Will you\nENTER the room or RETURN to the junction?")
                    if vars.decision_60 == "ENTER":
                        story("You enter a small room with bare, rocky walls. On the far wall\nhangs a golden key. There seems to be no way through the room.")
                        vars.decision_61 = story("Do you want to go for the KEY or LEAVE it\nand return to the junction?")
                        if vars.decision_61 == "KEY":
                            story("As you step into the room, the door swings shut behind you\nAs it closes, there is a click and a hiss.")
                            story("From the centre of the ceiling, a jet of gas is filling the room\nwith an acrid vapour. You breathe and cough deeply.")
                            vars.decision_62 = story("Will you RETURN to the door and escape quickly or\nhold your breath and DASH for the key first?")
                            if vars.decision_62 == "RETURN":
                                story("You get to the door, struggle with the lock and open it.\nYou burst out, close the door and take several deep breaths.")
                                vars.decision_60 = "RETURN"
                            elif vars.decision_62 == "DASH":
                                vars.equipment.append("125 key")
                                story("You snatch the key from its hook. It has the number 125 inscribed\non it. But your lungs are bursting. Roll two dice.")
                                if not stat_test(2):
                                    story("You are forced to take a breath of poison gas.")
                                    change_stats(0, 2, "subtract")
                                    change_stats(1, 3, "subtract")
                                    story("Your Skill is reduce by 2 and your Stamina\nis reduced by 3. You dash for the door.")
                                    vars.decision_60 = "RETURN"
                                else:
                                    story("You make it across the room to the door.")
                                    vars.decision_60 = "RETURN"
                            elif vars.decision_62 == "LEAVE":
                                vars.decision_60 = "RETURN"
                    if vars.decision_60 == "RETURN":
                        story("You arrive back at the junction and this time turn right.")
                        vars.decision_59 = "WEST"
                if vars.decision_59 == "WEST":
                    story("Some way along the passage, the corridor bends round to the north\nand you follow it until you reach another junction.")                
                    story("At this junction you see an arrow cut into the rock,\npointing to the north, and you decide to try this direction.")
                    story("The passage runs northwards, and ahead you can hear the splashings\nof an underground river. The air becomes cool and fresh.")
                    story("You soon reach a wide opening of a river bank but despair as\nyou look across to see no way through on the other side.")
                    story("To the east the river flows through a cave in the rock.")
                    vars.decision_63 = story("Will you either REST, and eat Provisions or go what seems the only\nway forward, jumping into the river and SWIMming downstream?")
                    if vars.decision_63 == "REST":
                        story("You squat on the sandy bank. As you prepare your meal you notice\na movement in the sand a couple of metres to your left.")
                        story("The movement becomes quite turbulent and\nyou spring to your feet, sword at the ready.")
                        story("Suddenly a large tubular head breaks through the surface,\ntwists around in the air and picks up your scent.")
                        story("The smooth, segmented body of a Giant Sandworm\nrears up and sways over in your direction.")
                        story("As it does so, a large orifice, with short spiky teeth, opens in\nwhat must be its head. You must do battle with this creature.")
                        vars.monster = [7, 7]
                        #escape after 3
                        if fight("Giant Sandworm"):
                            take_provs()
                            story("Panting after the struggle, you sit down to collect\nyourself and finish the Provisions you started.")
                            story("Eventually you pack your bag and wade into the stream.")
                        elif vars.escape:
                            story("You Escape by diving into the river and swimming downstream,\nbut you have lost the Provisions you started to eat.")
                            vars.escape = False
                        vars.decision_63 = "SWIM"
                    if vars.decision_63 == "SWIM":
                        vars.checkpoint = 11
=======
                    story("You do not have 5 Gold Pieces so you prepare to attack him.")
                    vars.decision_17 = "PREPARE"
                    if vars.decision_17 == "PREPARE":
                        story("He now stands just under two metres tall. He advances towards you.\nHis body is hairy. His teeth are pointed. His eyes flash.")
                        story("His fingernails are sharp claws.\nHis nose has become a rat-like snout. He is a WERERAT!")
                        vars.monster = [6, 5]
                        if fight("Wererat"):
                            story("The Wererat slumps to the ground. You search his body\nand find 2 Gold Pieces, his fare from the last crossing.")
                            story("You curse him for trying to overcharge you.\nYou take the 2 Gold Pieces and row yourself across the river.")
                            story("As you moor the boat on the north bank\nyou look back at the body. It has vanished!")
                            vars.gold += 2
                            change_stats(2, 2, "add")
                            #7
                            pass
                        if vars.escape:
                            story("You decide to escape and run over the rickety bridge.")
                            vars.decision_17 == "BRIDGE"
                            vars.escape
                    elif vars.decision_17 == "OFFER":
                        vars.gold -= 2
                        vars.decision_17 = "PAY"
            elif vars.decision_17 == "PAY":
                vars.gold -= 3
                story("He calms down, takes the gold and rows you across to the north bank.\nAfter mooring the boat he ambles off down a passageway.")
                #7
                pass

        elif vars.decision_17 == "PUNT":
            story("You climb on the raft and start to punt your way across the river.\nThe going is not easy.")
            story("In the middle of the river the raft seems to take on\na will of its own and bobs up and down dangerously.")
            story("You realise it is attempting to capsize itself\nand throw you into the river!")
            vars.decision_17 = story("You may either test your strength and luck to HOLD on and keep punting to the north side\nor jump into the water and attempt to SWIM to the south bank.")
            if vars.decision_17 == "HOLD":
                story("Roll two dice.")
                dice_num = randint(1, 12)
                if dice_num <= vars.hero[2] and dice_num <= vars.hero[1]:
                    story("You manage to hold on and manoeuvre the raft across to the north bank.")
                    story("You arrive safely but as you step on to the bank,\nthe raft drifts away and makes its own way across the river to the south bank.")
                    #7
                    pass
                else:
                    story("The raft throws you into the water\nand you start to swim back to the south bank")
                    vars.decision_17 = "SWIM"
            elif vars.decision_17 == "SWIM":
                story("You land in the icy water and frantically swim for the south bank.")
                story("To your amazement the raft turns round in mid-stream\nand makes its own way back to the south bank")
                story("You quicken your pace, aware that your splashings may at any time\nattract the attentions of any underwater creatures living in the river. Roll one die.")
                dice_num = randint(1, 6)
                if dice_num < 5:
                    story("You make it safely back to the south bank")
                    #218 back to start of cp8
                    pass
                elif dice_num > 4:
                    vars.decsion_17 = "PIRANHAS"
        elif vars.decision_17 == "BRIDGE":
            story("The timbers of the bridge are rotting and decayed from years of neglect.\nA single plank snaps under your foot. Roll one die")
            dice_num = randint(1, 6)
            if dice_num == 6:
                vars.decision_17 == "PIRANHAS"
            else:
                story("You regain your footing. In the middle of the river,\nthe bridge swings to and fro as it strains to take your weight.")
                story("The handrail comes away suddenly as you lean on it.\nRoll one die.")
                dice_num = randint(1, 6)
                if dice_num == 6:
                    vars.decision_17 = "PIRANHAS"
                    if vars.decision_17 == "PIRANHAS":
                        story("You plunge into the river below. The water around you bristles with activity,\nas if an invisible hand is dropping unseen pebbles into the river.")
                        story("You gulp - PIRANHAS! - and you begin to feel their sharp teeth biting into your flesh")
                        story("You kick with your limbs and slash with your weapons\nto keep them off until you reach the south bank.")
                        vars.monster = [6, 5]
                        if fight("Piranhas"):
                            vars.decision_17 = story("You manage to scramble out of the water andlie panting\non the south bank. You may eat provisions here. Will you?")
                            if vars.decision_17 == "YES":
                                take_provs()
                                vars.decision_17 = "NO"
                            if vars.decision_17 == "NO":
                                #218 back to start of cp8
                                pass
                elif dice_num < 6:
                    story("You regain your balance.")
                    story("The bridge is slippery from the splashings\nof the water. At one point you slip on a tuft of wet moss covering the timbers. Roll one die")
                    dice_num = randint(1, 6)
                    if dice_num == 6:
                        story("You slip from the bridge into the water below and start swimming for the nearest bank.")
                        vars.decision_17 = "RISK"
                    elif dice_num < 6:
                        story("You manage to hold on and you reach the north bank.")
                        #7
                        pass
            
        elif vars.decision_17 == "SWIM":
            story("The water is icy cold. You start to swim and notice\nthat your splashings are attracting a moving 'turbulence' in the water.")
            story("Will your strength and stamina hold out?\nRoll two dice.")
            dice_num = randint(1, 12)
            if dice_num <= vars.hero[1]:
                story("You believe you can make it and swim furiously for the north bank.")
                story("You gain ground on the 'turbulence' in the water but a few metres from the north bank\nyou notice two sinister reptilian eyes on the surface of the water watching you.")
                story("You are swimming straight for them. If you decide you'd rather not\nface the owner of the eyes, you may turn around.")
                story("Alternatively, you may risk the eyes ahead. You may try a detour which will send you nearer the 'turbulence'")
                vars.decision_17 = story("Will you\nTURN around\nRISK the eyes\nor try a DETOUR")
                if vars.decision_17 == "TURN":
                    story("You arrive exhausted and lose 1 stamina point.")
                    change_stats(1, 1, "subtract")
                    #218 back to start of cp8
                    pass
                elif vars.decision_17 == "RISK":
                    story("A huge jaw opens in front of you. By the size of it,\nthe CROCODILE you are swimming towards must be at least three metres long.")
                    story("The beast slaps its tail in the water and glides towards you. You must fight two attack rounds.")
                    vars.monster = [7, 6]
                    #Only fight two attack rounds.
                    story("Your combined thrashings attract a 'turbulence' in the water\nthat you had noticed before and this now makes its way towards your part of the river.")
                    story("Out of the corner of your eye\nyou notice this and must decide what to do.")
                    story("If you belive that the CROCODILE is on its last legs\nand you wish to continue the battle, then do so.")
                    story("Otherwise you can keep the beast occupied in the faint hope\nthat this mysterious visitor will help you in some way.")
                    vars.decision_17 = story("Will you CONTINUE the battle or KEEP the beast occupied?")
                    if vars.decision_17 == "CONTINUE":
                        #continue the battle
                        if fight("Crocodile"):
                            #259
                            pass
                    elif vars.decision_17 == "KEEP":
                        #have 1 more attack round
                        story("As the 'turbulence' surrounds you,\nyou can feel the jostlings of many small fish.")
                        story("They start ripping your flesh with vicious bites and you realize that you are surrounded by deadly PIRANHAS!")
                        if :#you have wounded the crocodile
                            story("You are lucky and most of the fish\nattack the bleeding reptile.")
                            vars.decision_17 = "FIGHT"
                        elif :#you haven't wounded the crocodile
                            story("You have not wounded the crocodile, so the fish may go for either you or it. Roll one die.")
                            dice_num = randint(1, 6)
                            if dice_num < 3:
                                story("The majority of the Piranhas go for you.")
                                vars.monster = [5, 5]
                                if fight("Piranhas"):
                                    vars.decision_17 = "WIN"
                            elif dice_num > 2 or vars.decision_17 == "FIGHT":
                                vars.monster = [5, 1]
                                if fight("Piranhas") or vars.decision_17 == "WIN":
                                    vars.decision_17 = story("You swim to shore. Do you want to eat provisions?")
                                    change_stats(2, 1, "add")
                                    if vars.decision_17 == "YES":
                                        take_provs()
                                        vars.decision_17 = "NO"
                                    if vars.decision_17 == "NO":
                                        #7   
                                        pass                                 
                elif vars.decision_17 == "DETOUR" or vars.decision_17 == "PIRANHAS":
                        story("You plunge into the river below. The water around you bristles with activity,\nas if an invisible hand is dropping unseen pebbles into the river.")
                        story("You gulp - PIRANHAS! - and you begin to feel their sharp teeth biting into your flesh")
                        story("You kick with your limbs and slash with your weapons\nto keep them off until you reach the south bank.")
                        vars.monster = [6, 5]
                        if fight("Piranhas"):
                            vars.decision_17 = story("You manage to scramble out of the water andlie panting\non the south bank. You may eat provisions here. Will you?")
                            if vars.decision_17 == "YES":
                                take_provs()
                                vars.decision_17 = "NO"
                            if vars.decision_17 == "NO":
                                #218 back to start of cp8
                                pass
            else:
                vars.decision_17 = story("You decide not to risk it and return to the south bank.\nYou may eat provisions on the south bank. Will you?")
                if vars.decision_17 == "YES":
                    take_provs()
                    vars.decision_17 == "NO"
                if vars.decision_17 == "NO":
                    #218 back to start of cp8
                    pass
>>>>>>> Stashed changes
