def repeat1():
    vars.decision_16 = story("Set in the north wall is a small recess where you may eat\nProvisions without being seen. Do you wish to take Provisions?")
    if vars.decision_16 == "YES":
        vars.provs -= 1
        change_stats(1, 4)
    vars.decision_17 = story("Will you set off either EASTwards or WESTwards?")
    if vars.decision_17 == "WEST":
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
                        vars.decision_18 = story("Here will you either go NORTHwards or turn to the EAST.")
                        if vars.decision_18 == "NORTH":
                            story("The passage widens and you see you are entering a large cavern.\nYou hear noises coming from ahead and proceed cautiously.")
                            story("As you approach, you make out a large figure and are overawed\nas you see this oversized human is at least three metres!")
                            story("Dressed in a leather tunic, the creature is\nabsorbed in a meal he is eating at a table.")
                            story("The cavern is at least a hundred metres across\nand must be the home of this Giant.")
                            story("A large table and two chairs are along one of the walls,\nand it is here that the creature sits.")
                            story("Intent on his meal(a large pig), he is unlikely to notice you.")
                            story("Around the cavern you can see his mattress, a great furry pelt,\nand a huge hammer, which you have no hope of budging.")
                            story("A fire burns in one corner, under a hole in the ceiling.\nThere appears to be no other way through the cavern.")
                            vars.decision_19 = story("Will you TAKE on this brute or RETURN to the junction?")
                            if vars.decision_19 == "TAKE":
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
                                        vars.decision_18 = "RETURN"
                                    elif vars.escape:
                                        story("You Escape down the passageway, where he will not be able to follow.")
                                        vars.escape = False
                                        vars.decision_18 = "RETURN"
                            if vars.decision_18 == "RETURN":
                                story("You arrive back at the junction and turn eastwards.")
                                vars.decision_18 = "EAST"
                        if vars.decision_18 == "EAST":
                            story("You arrive at another junction. An arrow on the wall points\nnorthwards and you decide to proceed in this direction.")
                            story("The passage runs northwards, and ahead you can har the splashings\nof an underground river. The air becomes cool and fresh.")
                            story("You soon reach a wide opening of a river bank but despair as\nyou look across to see no way through on the other side.")
                            story("To the east the river flows through a cave in the rock.")
                            vars.decision_17 = story("You may either REST, and eat Provisions or will yougo what seems\nthe only way forward, jumping in and SWIMming downstream?")
                            if vars.decision_17 == "REST":
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
            vars.decision_17 = "EAST"
    if vars.decision_17 == "EAST":
        story("You follow the passage eastwards for several metres,\nthen it turns to the north.")
        vars.decision_17 = story("Shortly you reach another junction where you may either go STRAIGHT\nor turn LEFT, into a passage that soon turns north. Which will you choose?")
        if vars.decision_17 == "STRAIGHT":
            story("The passage ends at a wooden door, trimmed in iron. Various inscriptions\nadorn the door, but none of this makes any sense to you.")
            vars.decision_18 = story("You listen, but hear nothing. Will you either\nOPEN the door or RETURN to the junction.")
            if vars.decision_18 == "OPEN":
                story("The door opens into a small room, comfortably furnished with a table,\nseveral chairs and a large bookcase which covers one wall.")
                story("Seated at the table is an old man with a long grey beard,\nand squatting on the old man's shoulder is a small winged beast.")
                story("This creature is no more tham six centimetres tall.\nIt has two arms and legs; its skin is a dusty grey colour.")
                story("It has tiny sharp white teeth and its wings are folded behind its back.")
                story("The old man says nothing as you walk in through the door,\nbut he beckons you over to sit down at the table.")
                story("He is tossing in his hand two small white objects. Will you:")
                vars.decision_18 = story("SIT down as he tells you?\nLEAVE the room and return to the junction?\nDraw your sword and RUSH forward?")
                if vars.decision_18 == "SIT":
                    story("The old man does not look up, but his devilish little pet eyes you\nsuspiciously and starts chattering in a small squeaky voice.")
                    if vars.gold > 0:
                        vars.decision_18 = story("The old man grunts and asks you whether you are game\nfor a wager. Will you ACCEPT, LEAVE or ATTACK him?")
                        #sus if you put attack
                        if vars.decision_18 == "ACCEPT":
                            while vars.decision_19 != "LEAVE":
                                while vars.decision_19 < 1 or vars.decision_19 > vars.gold:
                                    vars.decision_19 = story("The old asks you your stake. How much will you bet?")
                                    if not vars.decision_19.isdigit():
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
                                vars.decision_20 = story("Will you CONTINUE betting or LEAVE\nthrough the door and return to the junction?")
                                if vars.decision_20 == "LEAVE":
                                    if win:
                                        change_stats(0, 2)
                                        change_stats(1, 2)
                                        change_stats(2, 2)
                                        story("2 points are added to your Skill, Stamina and Luck scores.")
                                    vars.decision_18 = "LEAVE"
                                    break
                    else:
                        vars.decision_18 = story("The old man asks if you are game for a wager but you\nhave no Gold so will you either LEAVE or ATTACK him.")
                elif vars.decision_18 == "RUSH":
                    vars.decision_18 = "ATTACK"
                if vars.decision_18 == "ATTACK":
                    story("As you draw your sword, the Winged Gremlin flaps to the air and the man\nrushes to the bookshelf to escape through a secret door.")
                    story("But you must fight his pet.")
                    vars.monster = [5, 7]
                    if fight("Winged Gremlin"):
                        story("You search but try as you may you cannot find the switch for\nthe secret bookshelf door - the old man must have locked it.")
                        vars.gold += 5
                        story("You do find 5 Gold Pieces in a drawer in the table.\nYou decide to return to the junction to the south.")
                        vars.decision_18 = "LEAVE"
                if vars.decision_18 == "LEAVE":
                    story("You arrive back at the junction and this time take the passageway to the east.")
                    story("The passageway runs for several paces eastwards, then turns north.")
                    vars.decision_17 = "LEFT"
            elif vars.decision_18 == "RETURN":
                story("You arrive back at the junction and this time take the passageway to the east.\nIt runs for several paces eastwards, then turns north.")
                vars.decision_17 = "LEFT"
        if vars.decision_17 == "LEFT":
            story("The passageway ends in a door at which you listen but hear nothing.\nTrying the handle, the door opens to reveal a large, square room.")
            story("The room is completely bare, but the floor is covered in a mosaic of tiles.\nTwo shapes stand out; star tiles and hand tiles.")
            story("A door on the opposite wall is the only way through. Will you:")
            vars.decision_17 = story("WALK across the room?\nWalk across the room only stepping on STARS?\nWalk across the room stepping only on HANDS?")
            if vars.decision_17 == "WALK":
                story("Test your Luck three times.")
                change_stats(2, 1, "subtract")
                if not stat_test(2):
                    story("You are lucky.")
                    if not stat_test(2):
                        story("You are lucky.")
                        if not stat_test(2):
                            story("You make it across to the far door and can leave the room.")
                            vars.decision_17 = "STARS"
                else:
                    story("You are unlucky and step on a hand tile.")
                    vars.decision_17 = "HANDS"
            elif vars.decision_17 == "STARS":
                story("You tiptoe precariously across the room to the door in the\nnorth wall. You open the door and proceed through it.")
            if vars.decision_17 == "HANDS":
                story("The moment your foot touches a hand, you feel a vice-like grip\non your ankle and see a ghostly white hand gripping your leg.")
                story("You fight for your balance and manage to regain it.")
                story("But to your horror you see that, from every hand-shaped tile\nin the floor, a similar apparition has appeared.")
                story("The floor is now scattered with ghoulish hands, flexing and\nsnatching in the air. You draw your sword and chop at the hand.")
                vars.monster = [6, 4]
                if fight("Hand"):
                    story("The hand withers and shrinks back into the floor. At the same time,\nthe other hands stop dead and fade away down into the tiles.")
                    vars.hero[2] += 2
                    story("You decide this time to step on the star-shaped tiles, and step\ncarefully across to the door. The door opens. Add 2 Luck.")
                    vars.decision_17 = "STARS"
            if vars.decision_17 == "STARS":
                story("The passageway ahead runs northwards and you\nfollow this until you reach another junction.")
                vars.decision_17 = story("Here will you either continue NORTHwards or you may turn WESTwards")
                if vars.decision_17 == "NORTH":
                    story("The passageway ends in a solid doorway and you are surprised to see\na leather skirt tacked along the bottom of the door")
                    vars.decision_17 = story("You listen but hear nothing. Will you\nENTER the room or RETURN to the junction?")
                    if vars.decision_17 == "ENTER":
                        story("You enter a small room with bare, rocky walls. On the far wall hangs a golden key. There seems to be no way through the room.")
                        vars.decision_18 = story("Do you want to go for the KEY or LEAVE it\nand return to the junction?")
                        if vars.decision_18 == "KEY":
                            story("As you step into the room, the door swings shut behind you\nAs it closes, there is a click and a hiss.")
                            story("From the centre of the ceiling, a jet of gas is filling the room\nwith an acrid vapour. You breathe and cough deeply.")
                            vars.decision_18 = story("Will you RETURN to the door and escape quickly or\nhold your breath and DASH for the key first?")
                            if vars.decision_18 == "RETURN":
                                story("You get to the door, struggle with the lock and open it.\nYou burst out, close the door and take several deep breaths.")
                                vars.decision_17 = "RETURN"
                            elif vars.decision_18 == "DASH":
                                vars.equipment.append("125 key")
                                story("You snatch the key from its hook. It has the number 125 inscribed\non it. But your lungs are bursting. Roll two dice.")
                                if not stat_test(2):
                                    story("You are forced to take a breath of poison gas.")
                                    change_stats(0, 2, "subtract")
                                    change_stats(1, 3, "subtract")
                                    story("Your Skill is reduce by 2 and your Stamina\nis reduced by 3. You dash for the door.")
                                    vars.decision_17 = "RETURN"
                                else:
                                    story("You make it across the room to the door.")
                                    vars.decision_17 = "RETURN"
                            elif vars.decision_18 == "LEAVE":
                                vars.decision_17 = "RETURN"
                    if vars.decision_17 == "RETURN":
                        story("You arrive back at the junction and this time turn right.")
                        vars.decision_17 = "WEST"
                if vars.decision_17 == "WEST":
                    story("Some way along the passage, the corridor bends round to the north\nand you follow it until you reach another junction.")                
                    story("At this junction you see an arrow cut into the rock,\npointing to the north, and you decide to try this direction.")
                    story("The passage runs northwards, and ahead you can har the splashings\nof an underground river. The air becomes cool and fresh.")
                    story("You soon reach a wide opening of a river bank but despair as\nyou look across to see no way through on the other side.")
                    story("To the east the river flows through a cave in the rock.")
                    vars.decision_17 = story("Will you either REST, and eat Provisions or go what seems the only\nway forward, jumping into the river and SWIMming downstream?")
                    if vars.decision_17 == "REST":
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
                        vars.decision_17 = "SWIM"
                    if vars.decision_17 == "SWIM":
                        repeat_4()