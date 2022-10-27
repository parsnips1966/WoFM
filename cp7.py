from functions import *
import variables as vars
from rp1 import repeat1
from rp2 import repeat2
from rp3 import repeat3
from rp4 import repeat4

def checkpoint7():
    if vars.decision_16 == "LEFT":
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
        vars.decision_16 = "RIGHT"

    if vars.decision_16 == "RIGHT":
        story("You hear a deep rumbling noise and the ground begins to shudder.\nSlowly and noisily the portcullis rises into the celing.")
        vars.decision_16 = story("You may now walk to the junction.\nWill you turn WEST or EAST?")
        if vars.decision_16 == "WEST":
            vars.decision_16 = story("Shortly you arrive at another junction where you may go either\nstraight ahead WESTwards or turn NORTHwards. Which will you choose?")
            if vars.decision_16 == "NORTH":
                story("The passage runs for some distance northwards and then starts to open into a\nlarge cavern with rough walls. There appears to be no way through.")
                vars.decision_17 = story("Will you RETURN to the junction or ENTER the cavern?")
                if vars.decision_17 == "ENTER":
                    story("As you enter the cavern you hear loud footsteps, crunching heavily on the\nrocky floor. You crouch down beside the entrance in a small alcove.")
                    story("The steps get louder and you see\na great Ogre enter the cavern!")
                    story("He stands over two metres tall and is dressed in ill-fitting garments\nmade from some sort of hide. He carries a large wooden club. Will you:")
                    vars.decision_18 = story("ATTACK him as he enters?\nTry to CREEP out without him noticing?\nTry to DISTRACT him by throwing something into a far corner?")
                    if vars.decision_18 == "CREEP":
                        story("Test your Luck.")
                        if not stat_test(2):
                            story("You curse as you kick a small stone\nwhich goes skidding across the floor.")
                            story("You draw your sword in case the Ogre has heard it.")
                            vars.decision_17 = "ATTACK"
                        else:
                            story("You creep down the corridor back to the crossroads.")
                            vars.decision_17 = "RETURN"
                    elif vars.decision_18 == "DISTRACT":
                        if len(vars.equipment) == 0:
                            if vars.gold > 0:
                                vars.gold -= 1
                                story("You open your pack and reach inside for a Gold Piece.\nYou throw it across the cavern where it lands with a clatter.")
                                story("The Ogre looks towards the noise, and goes over to investigate.\nMeanwhile you creep out, down the passage and back to the junction.")
                                vars.decision_17 == "RETURN"
                            else:
                                story("You open your pack and find nothing to throw.\nYou must now fight the Ogre.")
                                vars.decision_18 = "ATTACK"
                        elif len(vars.equipment) == 1:
                            story("You open your pack and reach inside for the " + str(vars.equipment[0]) + ".\nYou throw it across the cavern where it lands with a clatter.")
                            story("The Ogre looks towards the noise, and goes over to investigate.\nMeanwhile you creep out, down the passage and back to the junction.")
                            vars.equipment.remove(vars.equipment[0])
                        else:
                            vars.decision_18 = story("You open your pack and reach inside for something\nsuitable to throw. Which item will you choose to throw?")
                            while vars.decision_18 not in vars.equipment:
                                vars.decision_18 = story("You don't have that. Which piece of equipment will you choose from your pack?")
                            vars.equipment.remove(vars.decision_18.title())
                            story("You throw the " + vars.decision_18 + " across the cavern\nwhere it lands with a clatter.")
                            story("The Ogre looks towards the noise, and goes over to investigate.\nMeanwhile you creep out, down the passage and back to the junction.")
                            vars.decision_17 == "RETURN"
                    if vars.decision_18 == "ATTACK":
                        story("You draw your sword, and as you do so\nthe Ogre hears you and prepares to attack.")
                        vars.monster = [8, 10]
                        if fight("Ogre", 2):
                            vars.equipment.append("9 Key")
                            story("The slain creature crashes to the ground. You go through his garments\nand find nothing, but a small pouch hangs around his neck.")
                            story("Inside this pouch is a small bronze key, with the number 9 cast into it.\nNothing else is of value so you head back to the junction.")
                            vars.decision_17 == "RETURN"
                        #if vars.escape:

                if vars.decision_17 == "RETURN":
                    story("You arrive back at the junction and turn westwards.")
                    vars.decision_16 = "WEST"
            if vars.decision_16 == "WEST":
                story("The passageway continues westwards and then turns due north. Some way up,\nyou reach a junction where a narrow passage runs off to the west.")
                vars.decision_16 = story("Will you continue NORTHwards or take the WEST way?")
                if vars.decision_16 == "NORTH":
                    story("Several metres up the passageway you arrive at a\njunction where you may turn either west or east.")
                    repeat1()
                    vars.decision_16 = "NO"
                elif vars.decision_16 == "WEST":
                    story("As you walk along the corridor, you see that it's getting narrower.\nAt one point you stoop, and as you do so, a deep, resonating laugh starts up.")
                    vars.decision_16 = story("Do you wish to continue?")
                    if vars.decision_16 == "YES":
                        story("The narrow passageway eventually becomes too small for you to walk along.\nYou get down on your hands and knees, and crawl.")
                        story("Eventually, there seems to be no way through, so you decide\nto return to the main passage. You head for the junction.")
                        vars.decision_16 = "NO"
                    if vars.decision_16 == "NO":
                        story("You arrive back at the junction and turn northwards. Several metres up\nyou arrive at a junction where you may turn either west or east.")
                if vars.decision_16 == "NO":
                    repeat1()
        elif vars.decision_16 == "EAST":
            story("Cautiously you creep along the passageway.\nAfter a short time it turns sharply to the north.")
            story("At the corner there's a bench of solid wood\nand a sign reads 'Rest Ye Here Weary Traveller'.")
            vars.decision_16 = story("Do you want to eat Provisions" + provs_tuto() + " here?")
            if vars.decision_16 == "YES":
                take_provs()
                story("As you sit on the bench and eat, you begin to feel deeply relaxed and the\naches from your body seem to sooth themselves away. This place is enchanted")
                change_stats(1, 2)
                change_stats(0, 1)
                story("You restore 2 additional Stamina as well\nas the normal amount and 1 Skill point.")
                vars.decision_16 = "NO"
            if vars.decision_16 == "NO":
                vars.decision_16 = story("You arrive at another junction in the passageway.\nWould you like to turn WEST or EAST?")
                if vars.decision_16 == "WEST":
                    story("You follow the passage westwards, then it turns sharply to the north and,\nsome metres further on, a passage runs off to the west.")
                    vars.decision_16 = story("Would you like to go along the WESTwards passage or carry on NORTHwards?")
                    if vars.decision_16 == "WEST":
                        story("As you walk, it visibly widens and eventually you find yourself\nstanding at the mouth of a rough cavern, a natural cave in the rock.")
                        story("As you look into the darkness, the cavern appears\nto be about 30 metres deep, with no visible exit.")
                        vars.decision_16 = story("Do you want to go INTO the cavern or go BACK to the junction?")
                        if vars.decision_16 == "INTO":
                            story("You enter the cavern and look around to see dozens of beautifully\ncoloured stalactites and stalagmites bordering the perimeter.")
                            story("Numerous drips can be heard, but the\nwhole place seems like a magic grotto.")
                            story("Near the back of the cavern, you come across a pair of boots,\nwhich seem to have been made quite recently. Will you:")
                            vars.decision_17 = story("CONTINUE investigating the cavern?\nTry on the BOOTS?\nLEAVE the cavern and return to the junction?")
                            if vars.decision_17 == "CONTINUE":
                                story("As you investigate, you hear a scurry of steps behind you and\nswing round to face the grotesque black shape of a Giant Spider.")
                                story("The Spider's body is at least a metre wide and\nyou quickly draw your sword to defend yourself.")
                                if fight("Giant Spider", 2):
                                    story("Apart from the boots, which you ignore, there is little of\nvalue in the cavern. You decide to head back the way you came.")
                                elif vars.escape == True:
                                    story("You Escape from the fight down the passageway.")
                                vars.decision_17 = "BACK"
                                vars.escape = False
                            elif vars.decision_17 == "BOOTS":
                                story("The boots are well-fashioned in a deep red leather.\nThey are much sturdier than your own and fit you well.")
                                story("You try a few steps but are horrified to find that you cannot move,\nand the boots seem to grip your feet with considerable force.")
                                story("As you struggle to free yourself, you hear a crack\nand a smash as a stalactite falls from the roof.")
                                story("You crane round to see a large black shape shifting\ntowards you. As it approaches you turn cold.")
                                story("Several metres away is a Giant Spider advancing on spindly legs,\nmandibles clicking nervously in anticipation of its next meal.")
                                story("You draw your sword to defend yourself as it stalks you.\nYou cannot move and thus must subtract 2 from each dice roll.")
                                #make work
                                vars.monster = [6, 6] #actual stats needed
                                if fight("Giant Spider"):
                                    story("Almost exhausted after your awkward fight with the Spider,\nyou set to work on hacking the boots off with your sword.")
                                    story("Eventually they come free and you may leave the cavern\ndown the passageway and back to the junction.")
                                    vars.decision_17 = "BACK"
                            if vars.decision_17 == "LEAVE":
                                vars.decision_17 = "BACK"
                        if vars.decision_17 == "BACK":
                            story("You arrive back at the junction and this time turn northwards.")
                            vars.decision_16 = "NORTH"
                    if vars.decision_16 == "NORTH":
                        story("A rough timber doorway is on the wast wall of the passage.\nYou listen at the door and can hear a jolly sort of humming sound.")
                        vars.decision_16 = story("Do you want to KNOCK on the door and\ngo in or will you CONTINUE northwards?")
                        if vars.decision_16 == "KNOCK":
                            story("A voice bids you 'Come in!' and you walk into a room furnished with a\ntable, shelves and the like, all of which have seen better days.")
                            story("Plates, bowls, cups and hundreds of old books line the shelves.")
                            story("In the midst of all this clutter, you see a little old man\nin a grubby white gown swaying to and fro in a rocking chair.")
                            story("He is still humming happily to himself, his eyes fixed on you,\nbut seeming at peace with the world. He bids you 'Good day.' Do you:")
                            vars.decision_17 = story("START to make conversation with him?\nDraw your sword and CHARGE at him?\nDecide not to waste time and LEAVE?")
                            if vars.decision_17 == "START":
                                story("As you speak the old man rises to his feet.'Oh my, oh my,\na stranger!' he starts. 'Well, do come in, the shop is open.'")
                                story("'What can I get you? What would you like to buy? What takes\nyour fancy? Which way are you headed? North? Well?'")
                                story("You tell the old man your story. He listens intently and replies,\n'In that case you will undoubtedly need one of my Blue Candles.'")
                                story("'That will be 20 Gold Pieces please. Cash if you don't mind.\nYes, I know it's expensive but isn't everything these days?'")
                                if vars.gold > 19:
                                    story("'I can guarantee it's still worth the price.\nYou might need it sooner than you think...'")
                                    vars.decision_17 = story("Will you decide to buy a candle?")
                                    if vars.decision_17 == "YES":
                                        vars.gold -= 20
                                        vars.equipment.append("Blue Candle")
                                    story("You are getting a little tired of his constant prattling.\nYou leave the room and go northwards.")
                                    vars.decision_16 = "CONTINUE"
                                else:
                                    story("You don't have enough Gold Pieces and you are getting a little\ntired of his prattling. You leave the room and go northwards.")
                                    vars.decision_16 = "CONTINUE"
                            elif vars.decision_16 == "CHARGE":
                                story("He is a little startled, but simply raises his hand. As he does so,\nyou suddenly collide heavily into...apparently nothing.")
                                change_stats(2, 2, "subtract")
                                story("You sit on the floor in a heap, rubbing your nose. Lose 2 Stamina points.")
                                story("The old man chuckles and says, 'You poor fool. Did you think I was\ndefenceless in such a den of evil as this? Regret your folly.'")
                                story("You rise to your feet and return to the passageway, turning north up the corridor.")
                                vars.decision_16 = "CONTINUE"
                            if vars.decision_16 == "LEAVE":
                                vars.decision_16 = "CONTINUE"
                        if vars.decision_16 == "CONTINUE":
                            story("Northwards the passageway ends at a solid wooden door.\nYou listen at the door but can hear nothing.")
                            story("There appears to be no choice but to open the door and\nenter the room, which you do. It's a large square room.")
                            story("You flash your lantern around and glimpse its emptiness - although\nthere are murals on the wall - before your lantern suddenly dies.")
                            story("You try to re-light it, but it will not catch. In the\nblackness you hear a succession of frightful noises.")
                            story("Howls, screams, cries and wails are getting louder and louder\nuntil they reach the pitch where you must cover your ears.")
                            if "Blue Candle" not in vars.equipment:
                                story("The ear-piercing sound gets louder and louder. The pain is\nunbearable. You grope in the dark for a wall. Do you head for:")
                                vars.decision_16 = "STAY"
                            else:
                                story("You think back to the words of the old man.\n'You might need it sooner than you think...'")
                                story("You grope in your pack and pull out the candle.\nImmediately it lights iteself of its own accord.")
                                story("The howling stops and the room appears bathed in a blue light\nfrom the candle. On the walls the figures in the mural are moving!")
                                story("They are mouthing silent screams as if trapped in a two-dimensional hell.")
                                vars.decision_16 = story("On the wall opposite is another door.\nWill you LEAVE through it or STAY to investigate?")
                                if vars.decision_16 == "LEAVE":
                                    repeat2()
                                elif vars.decision_16 == "STAY":
                                    story("As you watch the living mural, you are unaware of the speed\nyour candle is burning. Suddenly it flickers and goes out!")
                                    story("You again begin to hear the piercing screams\nand their pitch grows to an unbearable level.")
                                    story("You drop to your knees clutching your ears and crawl towards\nthe wall. Which wall will you crawl towards:")
                            if vars.decision_16 == "STAY":
                                vars.decision_16 = story("The EAST wall?\nThe NORTH wall?\nThe WEST wall?")
                                if vars.decision_16 == "EAST":
                                    story("You run along the wall searching for a door but find none.\nYour ears are on fire with the agony!")
                                    change_stats(0, 1, "subtract")
                                    vars.decision_16 = story("You may either try the WEST wall or the NORTH wall,\nbut you must find a way out soon! Which will you choose?")
                                if vars.decision_16 == "WEST":
                                    story("You grope along the wall but can find no way of escape.\nThe noise of causing you to scream in pain!")
                                    change_stats(0, 1, "subtract")
                                    vars.decision_16 = story("Will you either try the EAST wall or the NORTH wall?")
                                if vars.decision_16 == "NORTH":
                                    story("You grope around the length of the wall and find a door.\nQuickly you fumble with the handle. It opens!")
                                    repeat2()
                elif vars.decision_16 == "EAST":
                    vars.decision_16 = story("After a few metres you reach another three-way junction.\nWill you go either NORTHwards or EASTwards?")
                    if vars.decision_16 == "NORTH":
                        repeat3()
                    elif vars.decision_16 == "EAST":
                        vars.decision_16 = story("The passageway ends in a sturdy wooden door. Do you\nwant to try OPENing it or go back and try another ROUTE?")
                        if vars.decision_16 == "OPEN":
                            story("The door opens and you enter a small room. Your eyes widen as you\nsee that the walls of the room are covered in ornate stonework.")
                            story("Mosaics and marble inlays give this room a\nkind of beauty you have never seen before.")
                            story("In a corner of the room is a large metal statue of a\none-eyed creature. In its single eye is a sparkling jewel.")
                            story("As there appear to be no other ways through the room, you will have\nto go back to the junction - but that large jewel is very tempting.")
                            vars.decision_16 = story("Will you LEAVE it alone and go back to the junction\nor try to take the JEWEL with you?")
                            if vars.decision_16 == "LEAVE":
                                vars.decision_16 = "ROUTE"
                            elif vars.decision_16 == "JEWEL":
                                story("You approach the statue cautiously. A scampering behind you\nmakes you flash around...but it is only a rat.")
                                story("You feel at the jewel but it is solidly in place. You work your\nsword in behind it and as you work, you hear an ominous creaking.")
                                story("To your horror the statue is beginning to move!\nYou jump down and draw your sword.")
                                story("The Iron Cyclops cranes its head round towards you\nand steps down from its pedestal. You must fight!")
                                vars.monster = [10, 10]
                                if fight("Iron Cyclops"):
                                    vars.decision_17 = story("You sit back and rest from the exhausting battle.\nDo you want to eat Provisions here?")
                                    if vars.decision_17 == "YES":
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
                                vars.decision_16 = "ROUTE"
                        if vars.decision_16 == "ROUTE":
                            story("You arrive back at the junction and this time you turn northwards.")
                            repeat3()
    vars.checkpoint = 8