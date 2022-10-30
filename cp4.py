from functions import *
import variables as vars

def checkpoint4():
    if vars.decision_8 == "YES":
        vars.background = "room"
        story("The door opens to reveal a small, unkempt room. In the centre\nis a wooden table upon which a candle burns, lighting the room with its flickering flame.")
        story("A small box rests under the table. Seated around the table are\ntwo small creatures with warty skin, dressed in leather armour.")
        story("They are drinking some sort of grog and, by the way they stagger to their feet\non your arrival, you assume they are very drunk.")
        vars.decision_9 = story("Will you either draw your sword and LEAP forward at them\nor slam the door quickly and RUN on up the passage?")
        if vars.decision_9 == "LEAP":
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
                    vars.decision_10 = story("The name Farrigo Di Maggio is inscribed on a brass namplate on its lid.\nDo you wish to OPEN the box or LEAVE it behind?")
                    if vars.decision_10 == "OPEN":
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
                        vars.equipment.append("Dragonfire Spell")
                        story("You repeat the spell to yourself to memorise it and leave the room.")
                        vars.decision_8 = "NO"
                    elif vars.decision_10 == "LEAVE":
                        vars.decision_8 = "NO"
        elif vars.decision_9 == "RUN":
            vars.decision_8 = "NO"

    if vars.decision_8 == "NO":
        vars.background = "passage"
        vars.decision_9 = story("You eventually arrive at the end of the passage, at a three-way junction.\nWill you turn either to the WEST or to the EAST?")
        if vars.decision_9 == "WEST":
            vars.background = "door"
            story("The passageway runs straight for several metres and then ends in a wooden door.\nYou listen at the door and hear angry shouting coming from within.")
            vars.decision_11 = story("Will you investigate?")
            if vars.decision_11 == "YES":
                vars.background = "room"
                story("You open the door to a large room. A large chair behind a solid-looking table\nsuggests to you that someone, or something, of rank uses this room.")
                story("A chest in the centre catches your eye. In the corner stands a\nman-sized creature with a warty face, standing over a small creature of similar race.")
                story("With the whip in his hand, the Orc Chieftain has been beating his servant,\nwho is whimpering beneath him. Will you:")
                vars.decision_12 = story("Attack them BOTH?\nSpring at the CHIEFTAIN in the hope his servant will aid you?\nLEAVE the room and head back for the junction?")
                if vars.decision_12 == "CHIEFTAIN":
                    vars.background = "orc"
                    story("As you spring at the Chieftain, his servant rises to his feet, picks up a hefty club\nand joins the melee. But to your horror he attacks you!")
                    vars.decision_13 = story("Seeing this will you ESCAPE through the door down the corridor or CONTINUE the fight.")
                    if vars.decision_13 == "ESCAPE":
                        change_stats(1, 2, "subtract")
                        if vars.hero > 0:
                            story("The Chieftain gets a hit on you as you Escape.")
                            vars.decision_9 = "BACK"
                    elif vars.decision_13 == "CONTINUE":
                        vars.decision_10 = "BOTH"
                if vars.decision_12 == "BOTH":
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
                            vars.decision_14 = story("Will you try to SMASH the lock with your sword\nor leave it alone and GO through the open door.")
                            if vars.decision_14 == "SMASH":
                                story("The lock was obviously inadequate; it flies off\nand lands on the floor several metres away.")
                                story("You lift up the heavy lid and your eyes widen as you see the gold sheen\ncoming from within. A fair number of Gold Pieces are inside.")
                                story("In a corner lies a small black bottle with a tight stopper,\ncontaining some kind of liquid. Also in the chest is a silky black glove.")
                                story("But as you are admiring this treasure you hear a soft click and\nwince in pain as a small dart shoots forward into your stomach.")
                                story("Roll a die to determine the effect of the poison on the dart tip.")
                                dice_num = randint(1, 6)
                                change_stats(1, dice_num, "subtract")
                                if vars.hero[1] > 0:
                                    story("You sink to the floor. You pull the dart out and decide to bandage the wound.\nThis gives some relief, but you still feel weak.")
                                    story("You decide to take it easy and examine the contents of the chest.")
                                    vars.decision_15 = story("Do you wish to eat some Provisions" + provs_tuto() + " here?")
                                    if vars.decision_15 == "YES":
                                        take_provs()
                                        story("Your Stamina is restored.")
                                    story("There are 25 Gold Pieces and the bottle label shows it to be a\nPotion of Invisibility, good for one dose. The glove is a mystery.")
                                    vars.gold += 25
                                    vars.equipment.append("Invisibility Potion")
                                    vars.equipment.append("Silk Glove")
                                    story("You put all of these into your haversack and leave the room.")
                                    vars.decision_9 = "NO"
                            elif vars.decision_14 == "GO":
                                vars.decision_9 = "NO"
                elif vars.decision_12 == "LEAVE":
                    vars.decision_9 = "NO"
            if vars.decision_11 == "NO":
                vars.background = "passage"
                story("You arrive back at the junction in the passage and walk straight on eastwards.")
                vars.decision_9 = "EAST"
        if vars.decision_9 == "EAST":
            vars.decision_16 = story("You arrive at another junction in the passage.\nWill you either go NORTHwards or continue EASTwards?")
    vars.checkpoint = 5