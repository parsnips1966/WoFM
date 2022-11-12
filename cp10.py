from functions import *
import variables as vars

def checkpoint_10():
    story("The passage ahead ends at a sturdy door. You listen but hear nothing.\nYou try the handle, it turns, and you enter the room.")
    story("As you look around you hear a loud cry from behind you and swing round\nto see a wild man leaping towards you wielding a large battle axe.")
    story("He is a mad barbarian and you must fight him!")
    vars.monster = [7, 6]
    if fight("Barbarian"):
        story("A room search reveals nothing of any value, although an old box contains\na wooden mallet and five stumps of wood, sharpened at one end.")
        vars.decision_72 = story("Do you wish to take these?")
        if vars.decision_72 == "YES":
            vars.equipment.append("Five Wooden Stumps")
        vars.escape = True
    if vars.escape:
        story("You leave through the door in the north wall.")
        story("The door opens into a short corridor which ends several metres ahead\nat another door, similar to the one you have just come through.")
        story("You listen and hear nothing. You try the handle and it turns,\nallowing you into another room of a similar size.")
        story("But this roon is splendidly decorated, with a\npolished marble floor and rough walls painted white.")
        story("On each of the four walls hangs a painting,\nand there is another door in the north wall.")
        vars.decision_73 = story("Will you either go STRAIGHT through the room\nor you may stop to LOOK at the paintings?")
        if vars.decision_73 == "LOOK":
            story("They are portaits of men. Your spine shivers as you read one nameplate\n- it is of Zagor, the Warlock whose treasure you are seeking.")
            story("You look at his portrait and realise you are\npitting yourself against an awesome adversary.")
            story("You have the feeling that you are being watched and\nnotice the piercing eyes following you as you move.")
            story("You find yourelf drawn towards his portrait and you fear rises.\nDo you have enough courage to try to combat the Warlock.")
            vars.decision_74 = story("Will you either ESCAPE through the north door or\nlook for a WEAPON to use against the Warlock's power?")
            if vars.decision_74 == "ESCAPE":
                change_stats(1, 2, "subtract")
                vars.decision_73 = "STRAIGHT"
            elif vars.decision_74 == "WEAPON":
                if "Jewel" in vars.equipment:
                    story("You try various items of equipment against the gaze of the painting,\nbut none seems to work. Which will you try of the following:")
                    if "Wooden Stake" in vars.equipment:
                        if "Cheese" in vars.equipment:
                            vars.decision_75 = story("SLASH it with a swor?\nHold a JEWEL up at it?\nPLUNGE a wooden stake into it?\nThrow CHEESE at it?")
                        else:
                            vars.decision_75 = story("SLASH the painting with a sword?\nHold a JEWEL up in front of it?\nPLUNGE a wooden stake into it?")
                    else:
                        vars.decision_75 = story("Either SLASH the painting with your sword\nor hold a JEWEl up in front of it?")
                else:
                    story("You try various items against the gaze of the painting, but none work.\nNow you must try slashing it with your sword.")
                    vars.decision_75 = "SLASH"
                if vars.decision_75 == "SLASH":
                    change_stats(1, 1, "subtract")
                    story("The sword flies out of your hand, and you must leap aside as\nit comes down on you. It grazes your cheek as it falls.")
                    change_stats(0, 1, "subtract")
                    story("You decide you'd better leave the room. Pick up your sword\nand lose 1 more Skill in fear of the Warlock's power.")
                    vars.decision_73 = "STRAIGHT"
                elif vars.decision_75 == "JEWEL":
                    story("You have the jewel from the Eye of the Cyclops\nand you hold it in front of the Warlock.")
                    story("His intimidating stare turns to an expression of pain.\nHe obviously feels the jewel's power.")
                    story("Suddenly his eyes turn white and he goes limp. Your confidence\ngains as you realise you have won your first real battle.")
                    story("You put the jewel into your pack and leave through the north door.")
                    vars.decision_73 == "STRAIGHT"
                elif vars.decision_75 == "PLUNGE":
                    story("As you attack the portrait with the wooden stake,\nyou feel a wrench of pain in your wrist.")
                    story("You are forced by some unseen power to drop the stake.\nYou decide to run and leave through the north door.")
                    change_stats(0, 1, "subtract")
                    story("You lose 1 more Skill in awe of the Warlock's power.")
                    vars.decision_73 = "STRAIGHT"
                elif vars.decision_75 == "CHEESE":
                    story("The Cheese hits the portrait and bounces off. You hear an\nevil laugh and realise the Warlock is mockicking you.")
                    story("You decide to leave the room by the north door.")
                    vars.decision_73 = "STRAIGHT"
        if vars.decision_73 == "STRAIGHT":
            story("You open the door into a narrow passage and follow it northwards.\nSome metres up, it turns to the east, then to the north.")
            story("However, at this second bend, there is a small alcove\nin the rock. It seems a convenient hiding place.")
            vars.decision_76 = story("Do you wish to eat Provisions?")
            if vars.decision_76 == "YES":
                vars.provs -= 1
                change_stats(1, 4)
            story("When you have rested, continue northwards.")
            story("The passageway ends in another wooden door,\nthis time a small one with a carved bone handle.")
            story("You listen but hear nothing coming from inside.")
            story("You try the handle and the door opens into a pear-shaped room with\na rough stone floor, making walking across it somewhat awkward.")
            story("In one corner is a pile of rubble, mainly stones and dust, but there\nare also two odd-shaped pieces of wood and a length of rope.")
            story("A door in the north wall leads on. Will you:")
            vars.decision_77 = story("Examine the bits of WOOD?\nStudy the length of ROPE?\nLEAVE through the north door?")
            if vars.decision_77 == "WOOD":
                story("Both pieces of wood are Y-shaped and smooth,\nas if washed up from a river.")
                vars.equipment.append("Pieces Of Wood")
                vars.decision_78 = story("If you wish to take the pieces of wood you must\nchoose one item of equipment to leave behind. Which will you choose?")
                while vars.decision_78 not in vars.equipment:
                    vars.decision_78 = story("You don't have that. Which piece of equipment will you choose from your pack.")
                vars.equipment.remove(vars.decision_17.title())
                vars.decision_77 = story("Will you either LEAVE through the north door or stay and examine the ROPE?")
            if vars.decision_77 == "ROPE":
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
                vars.decision_77 = "LEAVE"
            if vars.decision_77 == "LEAVE":
                story("The passage ahead leads you northwards. The rocky floor becomes\nsandy until eventually you are walking on a sort of coarse sand.")
                story("The passage widens and you can hear water. You continue until\nyou find yourself in a large cavern through which a river flows.")
                vars.checkpoint = 12
        vars.escape = False