from functions import *
import variables as vars
from rp1 import repeat1
from rp2 import repeat2
from rp3 import repeat3
from rp4 import repeat4

def checkpoint8():
    if vars.river:
        story("You are on the south bank of an underground river facing across its\nblack depths. There appear to be four ways of crossing.")
        story("To your left, a rusted bell bears the sign:\n'Ferry Service 2 Gold Pieces - Please Ring.'")
        story("There is a small raft in front of you with a long stick resting beside it:\nyou could punt across the river. A rickety old bridge crosses on the right.")
        story("If you don't trust any of these, you may swim.")
        vars.decision_17 = story("Which will you choose:\nRING the bell\nPUNT the raft across\nrisk the BRIDGE\nSWIM?")
        if vars.decision_17 == "RING":
            story("The bell gives a dull clang and after a few moments you see\na withered old man climb into a small rowing boat moored on the north bank")
            story("He rows slowly across to you, moors the boat and limps towards you.\nHe asks you for 3 Gold Pieces.")
            story("When you protest at the price he mutters something about 'inflation'.\nHe begins to get angry at your protestations.")
            if vars.gold > 2:    
                vars.decision_17 = story("Do you PAY him the 3 Gold Pieces or THREATEN him?")
            else:
                story("You don't have 3 Gold Pieces so you decide to threaten him.")
                vars.decision_17 = "THREATEN"
            if vars.decision_17 == "THREATEN":
                story("He doesn't take at all kindly to your threats. As you argue,\nand his anger builds, you notice a transformation taking place.")
                story("He begins to straighten up and grows physically stronger in front of your very eyes.\nHis face and arms grow hairy. You must make a quick decision.")
                if vars.gold > 4:
                    vars.decision_17 = story("Will you OFFER him 5 Gold Pieces to calm him down or PREPARE to attack him.")
                else:
                    story("You do not have 5 Gold Pieces so you prepare to attack him.")
                    vars.decision_17 = "PREPARE"
                    if vars.decision_17 == "PREPARE":
                        #188
                        pass
                    elif vars.decision_17 == "OFFER":
                        vars.gold -= 5
                        #272 same page as pay
                        pass
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
                if dice_num <= vars.hero[2] and dice_num <= vars.hero[1]: #do not deduct a luck point
                    story("You manage to hold on and manoeuvre the raft across to the north bank.")
                    story("You arrive safely but as you step on to the bank,\nthe raft drifts away and makes its own way across the river to the south bank.")
                    #7
                    pass
                else:
                    story("The raft throws you into the water\nand you start to swim back to the south bank")
                    #166 same as swim
                    pass
            elif vars.decision_17 == "SWIM":
                story("You land in the icy water and frantically swim for the south bank.")
                story("To your amazement the raft turns round in mid-stream\nand makes its own way back to the south bank")
                story("You quicken your pace, aware that your splashings may at any time\nattract the attentions of any underwater creatures living in the river. Roll one die.")
                dice_num = randint(1, 6)
                if dice_num < 5:
                    story("You make it safely back to the south bank")
                    #218
                    pass
                elif dice_num > 4:
                    #158
                    pass

        elif vars.decision_17 == "BRIDGE":
            story("The timbers of the bridge are rotting and decayed from years of neglect.\nA single plank snaps under your foot. Roll one die")
            dice_num = randint(1, 6)
            if dice_num == 6:
                story("You splash into the river below.")
                story("The water around you bristles with activity,\nas if an invisible hand is droppping unseen pebbles into the river.")
                story("You gulp - PIRANHAS! - and you begin to feel their sharp teeth biting into your flesh.")
                story("You kick with your limbs and slash with your weapons\nto keep them off until you reach the south bank.")
                vars.monster = [6, 5]
                if fight("Piranhas"):
                    vars.decision_17 = story("You manage to scramble out of the water andlie panting\non the south bank. You may eat provisions here. Will you?")
                    if vars.decision_17 == "YES":
                        take_provs()
                        vars.decision_17 == "NO"
                    if vars.decision_17 == "NO":
                        #218
                        pass
            else:
                story("You regain your footing. In the middle of the river,\nthe bridge swings to and fro as it strains to take your weight.")
                story("The handrail comes away suddenly as you lean on it.\nRoll one die.")
                dice_num = randint(1, 6)
                if dice_num == 6:
                    story("You plunge into the river below.")
                    #158
                    pass
                elif dice_num < 6:
                    story("You regain your balance.")
                    #298
                    pass
            
        elif vars.decision_17 == "SWIM":
            story("The water is icy cold. You start to swim and notice\nthat your splashings are attracting a moving 'turbulence' in the water.")
            story("Will your strength and stamina hold out?\nRoll two dice.")
            dice_num = randint(1, 12)
            if dice_num <= vars.hero[1]:
                story("You believe you can make it and swim furiously for the north bank")
                story("You gain ground on the 'turbulence' in the water but a few metres from the north bank\nyou notice two sinister reptilian eyes on the surface of the water watching you.")
                story("You are swimming straight for them. If you decide you'd rather not\nface the owner of the eyes, you may turn around.")
                story("Alternatively, you may risk the eyes ahead. You may try a detour which will send you nearer the 'turbulence'")
                vars.decision_17 = story("Will you\nTURN around\nRISK the eyes\nor try a DETOUR")
                if vars.decision_17 == "TURN":
                    story("You arrive exhausted and lose 1 stamina point.") #lose 1 stamina
                    #218
                    pass
                elif vars.decision_17 == "RISK":
                    #86
                    pass
                elif vars.decision_17 == "DETOUR":
                    #158
                    pass
                
            else:
                vars.decision_17 = story("You decide not to risk it and return to the south bank.\nYou may eat provisions on the south bank. Will you?")
                if vars.decision_17 == "YES":
                    take_provs()
                    vars.decision_17 == "NO"
                if vars.decision_17 == "NO":
                    #218
                    pass


    vars.checkpoint = 9