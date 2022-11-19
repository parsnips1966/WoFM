from functions import *
import variables as vars

def checkpoint_12():
    story("You are on the south bank of an underground river facing across its\nblack depths. There appear to be four ways of crossing.")
    story("To your left, a rusted bell bears the sign:\n'Ferry Service 2 Gold Pieces - Please Ring.'")
    story("There is a small raft in front of you with a long stick resting beside it:\nyou could punt across the river. A rickety old bridge crosses on the right.")
    story("If you don't trust any of these, you may swim.")
    vars.decision_79 = story("Which will you choose:\nRING the bell\nPUNT the raft across\nrisk the BRIDGE\nSWIM?")
    if vars.decision_79 == "RING":
        story("The bell gives a dull clang and after a few moments you see\na withered old man climb into a small rowing boat moored on the north bank.")
        story("He rows slowly across to you, moors the boat and limps towards you.\nHe asks you for 3 Gold Pieces.")
        story("When you protest at the price he mutters something about 'inflation'.\nHe begins to get angry at your protestations.")
        if vars.gold > 2:    
            vars.decision_80 = story("Do you PAY him the 3 Gold Pieces or THREATEN him?")
        else:
            story("You don't have 3 Gold Pieces so you decide to threaten him.")
            vars.decision_80 = "THREATEN"
        if vars.decision_80 == "THREATEN":
            story("He doesn't take at all kindly to your threats. As you argue,\nand his anger builds, you notice a transformation taking place.")
            story("He begins to straighten up and grows physically stronger in front of your very eyes.\nHis face and arms grow hairy. You must make a quick decision.")
            if vars.gold > 4:
                vars.decision_81 = story("Will you OFFER him 5 Gold Pieces to calm him down or PREPARE to attack him.")
            else:
                story("You do not have 5 Gold Pieces so you prepare to attack him.")
                vars.decision_81 = "PREPARE"
                if vars.decision_81 == "PREPARE":
                    story("He now stands just under two metres tall. He advances towards you.\nHis body is hairy. His teeth are pointed. His eyes flash.")
                    story("His fingernails are sharp claws.\nHis nose has become a rat-like snout. He is a WERERAT!")
                    vars.monster = [6, 5]
                    if fight("Wererat"):
                        story("The Wererat slumps to the ground. You search his body\nand find 2 Gold Pieces, his fare from the last crossing.")
                        vars.gold += 2
                        story("You curse him for trying to overcharge you.\nYou take the 2 Gold Pieces and row yourself across the river.")
                        story("As you moor the boat on the north bank\nyou look back at the body. It has vanished!")
                        change_stats(2, 2, "add")
                        vars.checkpoint = 13
                    if vars.escape:
                        story("You decide to escape and run over the rickety bridge.")
                        vars.decision_79 == "BRIDGE"
                        vars.escape
                elif vars.decision_81 == "OFFER":
                    vars.gold -= 5
                    vars.decision_80 = "PAY"
        if vars.decision_80 == "PAY":
            vars.gold -= 3
            story("He calms down, takes the gold and rows you across to the north bank.\nAfter mooring the boat he ambles off down a passageway.")
            vars.checkpoint = 13
    elif vars.decision_79 == "PUNT":
        story("You climb on the raft and start to punt your way across the river.\nThe going is not easy.")
        story("In the middle of the river the raft seems to take on\na will of its own and bobs up and down dangerously.")
        story("You realise it is attempting to capsize itself\nand throw you into the river!")
        vars.decision_82 = story("Will you either test your strength and luck to HOLD on\nor jump into the water and attempt to SWIM to the south bank?")
        if vars.decision_82 == "HOLD":
            story("Roll two dice.")
            vars.dice_num = randint(1, 12)
            if vars.dice_num <= vars.hero[2] and vars.dice_num <= vars.hero[1]:
                story("You manage to hold on and manoeuvre the raft across to the north bank.")
                story("You arrive safely but as you step on to the bank,\nthe raft drifts away and makes its own way across the river to the south bank.")
                vars.checkpoint = 13
            else:
                story("You lose your grip and the raft throws you in.")
                vars.decision_82 = "SWIM"
        if vars.decision_82 == "SWIM":
            story("You land in the icy water and frantically swim for the south bank.")
            story("To your amazement the raft turns round in mid-stream\nand makes its own way back to the south bank")
            story("You quicken your pace, aware that your splashings may at any time\nattract the attentions of any underwater creatures living in the river. Roll one die.")
            vars.dice_num = randint(1, 6)
            if vars.dice_num < 5:
                story("You make it safely back to the south bank")
                #218
                pass
            elif vars.dice_num > 4:
                vars.decision_17 = "PIRANHAS"
    elif vars.decision_79 == "BRIDGE":
        story("The timbers of the bridge are rotting and decayed from years of neglect.\nA single plank snaps under your foot. Roll one die.")
        vars.dice_num = randint(1, 6)
        if vars.dice_num == 6:
            story("You splash into the river below.")
            story("The water around you bristles with activity,\nas if an invisible hand is droppping unseen pebbles into the river.")
            story("You gulp - PIRANHAS! - and you begin to feel their sharp teeth biting into your flesh.")
            story("You kick with your limbs and slash with your weapons\nto keep them off until you reach the south bank.")
            vars.monster = [6, 5]
            if fight("Piranhas"):
                vars.decision_83 = story("You manage to scramble out of the water andlie panting\non the south bank. You may eat provisions here. Will you?")
                if vars.decision_83 == "YES":
                    take_provs()
                    vars.decision_83 == "NO"
                if vars.decision_83 == "NO":
                    #218
                    pass
        else:
            story("You regain your footing. In the middle of the river,\nthe bridge swings to and fro as it strains to take your weight.")
            story("The handrail comes away suddenly as you lean on it.\nRoll one die.")
            vars.dice_num = randint(1, 6)
            if vars.dice_num == 6:
                story("You plunge into the river below.")
                story("You gulp - PIRANHAS! - and you begin to feel their sharp teeth biting into your flesh")
                story("You kick with your limbs and slash with your weapons\nto keep them off until you reach the south bank.")
                vars.monster = [6, 5]
                if fight("Piranhas"):
                    vars.decision_86 = story("You manage to scramble out of the water andlie panting\non the south bank. You may eat provisions here. Will you?")
                    if vars.decision_86 == "YES":
                        take_provs()
                        vars.decision_86 = "NO"
                    if vars.decision_86 == "NO":
                        #218 back to start of cp8
                        pass
            elif vars.dice_num < 6:
                story("You regain your balance.")
                story("The bridge is slippery from the splashings of the water.\nAt one point you slip on a tuft of wet moss covering the timbers. Roll one die.")
                vars.dice_num = randint(1, 6)
                if vars.dice_num == 6:
                    story("You slip from the bridge into the water below and start swimming for the nearest bank.")
                    vars.decision_17 = "RISK"
                elif vars.dice_num < 6:
                    story("You manage to hold on and you reach the north bank.")
                    vars.checkpoint = 13
    elif vars.decision_79 == "SWIM":
        story("The water is icy cold. You start to swim and notice\nthat your splashings are attracting a moving 'turbulence' in the water.")
        story("Will your strength and stamina hold out?\nRoll two dice.")
        vars.dice_num = randint(1, 12)
        if vars.dice_num <= vars.hero[1]:
            story("You believe you can make it and swim furiously for the north bank.")
            story("You gain ground on the 'turbulence' in the water but a few metres from the north bank\nyou notice two sinister reptilian eyes on the surface of the water watching you.")
            story("You are swimming straight for them. If you decide you'd rather not\nface the owner of the eyes, you may turn around.")
            story("Alternatively, you may risk the eyes ahead.\nYou may also try a detour which will send you nearer the 'turbulence'.")
            vars.decision_84 = story("Will you\nTURN around\nRISK the eyes\nor try a DETOUR?")
            if vars.decision_84 == "TURN":
                change_stats(1, 1, "subtract")
                story("You arrive exhausted and lose 1 stamina point.")
                #218
                pass
            elif vars.decision_84 == "RISK":
                story("A huge jaw opens in front of you. By the size of it,\nthe Crocodile you are swimming towards must be at least three metres long.")
                story("The beast slaps its tail in the water and glides towards you.\nYou must fight two attack rounds.")
                vars.monster = [7, 6]
                #Only fight two attack rounds.
                story("Your combined thrashings attract a 'turbulence' in the water\nthat you had noticed before and this now makes its way towards your part of the river.")
                story("Out of the corner of your eye\nyou notice this and must decide what to do.")
                story("If you belive that the Crocodile is on its last legs\nand you wish to continue the battle, then do so.")
                story("Otherwise you can keep the beast occupied in the faint hope\nthat this mysterious visitor will help you in some way.")
                vars.decision_87 = story("Will you CONTINUE the battle or KEEP the beast occupied?")
                if vars.decision_87 == "CONTINUE":
                    #continue the battle
                    if fight("Crocodile"):
                        #259
                        pass
                elif vars.decision_87 == "KEEP":
                    #have 1 more attack round
                    story("As the 'turbulence' surrounds you,\nyou can feel the jostlings of many small fish.")
                    story("They start ripping your flesh with vicious bites and\nyou realize that you are surrounded by deadly PIRANHAS!")
                    #if you have wounded the crocodile:
                    #    story("You are lucky and most of the fish\nattack the bleeding reptile.")
                    #    vars.decision_89 = "FIGHT"
                    #elif you haven't wounded the crocodile:
                    #    story("You have not wounded the crocodile, so the fish may go for either you or it. Roll one die.")
                    #    vars.dice_num = randint(1, 6)
                    #    if vars.dice_num < 3:
                    #        story("The majority of the Piranhas go for you.")
                    #        vars.monster = [5, 5]
                    #        if fight("Piranhas"):
                    #            vars.decision_90 = "WIN"
                    #    elif vars.dice_num > 2 or vars.decision_89 == "FIGHT":
                    #        vars.monster = [5, 1]
                    #        if fight("Piranhas") or vars.decision_90 == "WIN":
                    #            vars.decision_91 = story("You swim to shore. Do you want to eat provisions?")
                    #            change_stats(2, 1, "add")
                    #            if vars.decision_91 == "YES":
                    #                take_provs()
                    #                vars.decision_91 = "NO"
                    #            if vars.decision_91 == "NO":
                    #                vars.checkpoint = 13
            elif vars.decision_84 == "DETOUR" or vars.decision_17 == "PIRANHAS":
                story("You plunge into the river below. The water around you bristles with activity,\nas if an invisible hand is dropping unseen pebbles into the river.")
                story("You gulp - PIRANHAS! - and you begin to feel their sharp teeth biting into your flesh.")
                story("You kick with your limbs and slash with your weapons\nto keep them off until you reach the south bank.")
                vars.monster = [6, 5]
                if fight("Piranhas"):
                    vars.decision_88 = story("You manage to scramble out of the water andlie panting\non the south bank. You may eat provisions here. Will you?")
                    if vars.decision_88 == "YES":
                        take_provs()
                        vars.decision_88 = "NO"
                    if vars.decision_88 == "NO":
                        #218 back to start of cp8
                        pass
        else:
            vars.decision_85 = story("You decide not to risk it and return to the south bank.\nYou may eat provisions on the south bank. Will you?")
            if vars.decision_85 == "YES":
                take_provs()
                vars.decision_85 == "NO"
            if vars.decision_85 == "NO":
                #218
                pass
