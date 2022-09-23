def repeat2():
    story("You enter another small room, bare except for a fountain in the middle.")
    story("Not a particularly grand affair, the fountain is a small carved fish,\nand a short jet of water comes from its mouth.")
    story("A wooden sign hangs from the fish and bears a message. It is\nwritten in Goblin tongue, at which you are not very proficient.")
    story("The first word you cannot understand, but the others read:\n'... not drink'. But you are extremely thirsty.")
    vars.decision_16 = story("Will you DRINK from the fountain? Or PASS\nit by and leave through a door in the north wall?")
    if vars.decision_16 == "DRINK":
        story("The water is refreshing. You feel a glow spreading through your\nbody as if you were drinking at the fountain of life.")
        change_stats(1, 4)
        change_stats(0, 11)
        change_stats(2, 11)
        story("Add 4 Stamina points, and restore your Skill\nand Luck score to their initial levels.")
        vars.decision_17 = story("The fountain of life for you must be death for\nthe evil Goblins. Will you eat Provisions " + provs_tuto() + " here?")
        if vars.decision_17 == "YES":
            change_stats(1, 4)
        story("When you have rested, leave through the north door.")
        vars.decision_16 = "PASS"
    if vars.decision_16 == "PASS":
        story("The door opens into a passage which you follow northwards.\nShortly you reach a bend and follow it round to the east.")
        vars.decision_16 = story("Several metres on, you reach a junction at which\nyou may either go NORTH or continue EASTwards. Which will you choose?")
        if vars.decision_16 == "EAST":
            story("The passage twists and turns and eventually ends in\na solid iron door. You listen but hear nothing.")
            vars.decision_17 = story("Will you try to OPEN the door or you can go BACK to the junction.")
            if vars.decision_17 == "OPEN":
                story("The room is unoccupied and there\nseems to be no other means of exit.")
                story("In the centre of the floor stands a table, and on this\ntable are two helmets; one of bronze and one of iron.")
                story("Both are about your size. Will you:")
                vars.decision_17 = story("Try on the BRONZE helmet?\nTry on the IRON helmet?\nRETURN to the junction?")
                if vars.decision_17 == "BRONZE":
                    story("You place the helmet on your head. It fits well.\nSuddenly a searing pain flashes across your forehead.")
                    story("You cannot think straight. This helmet is cursed and,\ntry as you might, you cannot remove it!")
                    change_stats(0, 1, "subtract")
                    story("The pain soon subsides, but you still cannot shift\nthe helmet. You stagger back to the junction.")
                    vars.decision_17 = "BACK"
                elif vars.decision_17 == "IRON":
                    story("You place the helmet on your head. It fits well.")
                    story("A glow fills your body and you seem to possess a power\nand confidence beyond anything you have felt before.")
                    story("This helmet is blessed with magic and will allow you to\nadd 1 point to all future Attack Strengths.")
                    #make work
                    vars.equipment.append("Iron Helmet")
                    vars.decision_16 = "BACK"
                if vars.decision_17 == "RETURN":
                    vars.decision_16 = "BACK"
            if vars.decision_16 == "BACK":
                story("You arrive back at the junction and this time turn northwards.")
                vars.decision_16 = "NORTH"
        if vars.decision_16 == "NORTH":
            vars.decision_16 = story("Some way up, you reach another junction where you\nmay either go EASTwards or turn WESTwards. Which will you choose?")
            if vars.decision_16 == "EAST":
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
                        vars.decision_16 = "WEST"
            if vars.decision_16 == "WEST":
                story("The passageway twists sharply northwards and ahead you can hear water flowing.")
                story("You eventually reach the south bank of an underground river.")
                story("As you stand on the pebbled bank you hear a fluttering and\nlook up to see three Giant Bats swooping down on you.")
                vars.decision_16 = story("Will you FIGHT these three as a single creature or ESCAPE?")
                if vars.decision_16 == "FIGHT":
                    vars.monster = [6, 6]
                    if fight("Giant Bats"):
                        story("You sheathe your sword and walk up to the water, wondering if its safe to swim.")
                        story("Although you cannot see any immediate danger, there is\nno way through on the north side of the river.")
                        story("You suddenly notice a gleaming sword lying on the river\nbed several steps in. You wade to retrieve it.")
                        story("it is light in your hand, far less cumbersome than\nyour own weapon, and it has a keen edge.")
                        story("This marvellous weapon will add 1 point to your Skill whilst you use it.")
                        vars.equipment.append("Good Sword")
                        vars.decision_16 = story("A mysterious voice speaking in your mind seems to be\ntelling you to throw your own sword into the river. Will you?")
                        if vars.decision_16 == "YES":
                            story("As your sword splashes into the water,\na bubbly voice says, 'Thank you!'")
                            story("It now seems that the only way onward is to swim\ndownstream to the east. You plunge into the water.")
                            vars.decision_16 = "ESCAPE"
                        elif vars.decision_16 == "NO":
                            story("As you put the two swords into your belt,\nyour new one seems to take on a mind of its own.")
                            change_stats(1, 1, "subtract")
                            story("It cuts your leg and, as you draw\nit out, it turns rubbery in your hand.")
                            vars.equipment.remove("Good Sword")
                            story("It's useless so you fling it into the river.\nIt seems the only way is for you to swim downriver.")
                            story("You plunge in and start swimming.")
                            vars.decision_16 = "ESCAPE"
                    elif vars.escape:
                        repeat_4()
                        vars.escape = False
                elif vars.decision_16 == "ESCAPE":
                    change_stats(1, 2, "subtract")
            if vars.decision_16 == "ESCAPE":
                repeat_4()