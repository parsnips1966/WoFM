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
        vars.decision_17 = story("Which will you choose?\nRING the bell\nPUNT the raft across\nrisk the BRIDGE\nSWIM")
        if vars.decision_17 == "RING":
            #3
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