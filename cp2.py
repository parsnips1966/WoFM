from functions import *
import variables as vars

def checkpoint_2():
    if vars.decision_4 == "YES":
        vars.background = "darkroom"
        story("The door opens to reveal a small, smelly room. In the centre is a rickety\nwooden table on which stands a lit candle. Underneath is small wooden box.")
        vars.background = "sleepingorc"
        story("Asleep on a straw mattress is a short, stocky creature; the same sort of\ncreature you found at the sentry post. He must be the night watch guard.")
        vars.decision_5 = story("You may either RETURN to the corridor and press on northwards\nor will you creep into the room and try to STEAL the box?")
        if vars.decision_5 == "RETURN":
            vars.background = "passage"
            vars.decision_4 = "NO"
        elif vars.decision_5 == "STEAL":
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
                vars.decision_4 = "NO"
            else:
                vars.background = "orc"
                story("The sleeping creature awakens startled.\nHe jumps up and rushes at you unarmed.")
                vars.decision_5 = story("With your sword you should be able to defeat him but his teeth look vicious.\nWill you ESCAPE or FIGHT the Orc who is attacking you?")
                if vars.decision_5 == "ESCAPE":
                    change_stats(1, 2, "subtract")
                    vars.background = "passage"
                    story("You run out of the room and slam the door shut\nbut the Orc has scratched you with its teeth.")
                    story("You turn northwards up the passageway passing a similar-looking door further up.")
                    vars.decision_4 = "NO"
                elif vars.decision_4 == "FIGHT":
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
                        vars.decision_4 = "NO"
    if vars.decision_4 == "NO":
        vars.background = "door"
        vars.decision_6 = story("Further up the passage along the west wall you see another door.\nYou listen at it but hear nothing. Do you want to try opening the door?")
    vars.checkpoint = 3