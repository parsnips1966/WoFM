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
            story("He rows slowly across to you, moors the boat and\nlimps towards you. He asks you for 3 Gold Pieces.")
            story("When you protest at the price he mutters something about 'inflation'.\nHe begins to get angry at your protestations.")
            if vars.gold > 2:    
                vars.decision_17 = story("Do you PAY him the 3 Gold Pieces or THREATEN him?")
            else:
                story("You don't have 3 Gold Pieces so you decide to threaten him.")
                vars.decision_17 = "THREATEN"
            if vars.decision_17 == "THREATEN":
                #127
                pass
            elif vars.decision_17 == "PAY":
                #272
                pass
        elif vars.decision_17 == "PUNT":
            #386
            pass
        elif vars.decision_17 == "BRIDGE":
            #209
            pass
        elif vars.decision_17 == "SWIM":
            #316
            pass

    vars.checkpoint = 9