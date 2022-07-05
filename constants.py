"""Contains all the constants used including colours and all the words which the user is allowed to input."""

import pygame
from pygame import mixer

pygame.mixer.init()

width = 1300
height = 700
screen = pygame.display.set_mode((width, height))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 127, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
INPUTS = ["YES", "NO", "EAST", "WEST", "RETURN", "STEAL", "ESCAPE", "FIGHT", "OPEN", "LEAVE", "LEAP", "RUN", "CHIEFTAIN", "BACK", "BOTH", "CONTINUE", "SMASH", "GO",
    "NORTH", "ATTACK", "WALK", "SHOUT", "CLOSE", "LEFT", "RIGHT", "ENTER", "DISTRACT", "CREEP", "INTO", "BOOTS", "KNOCK", "START", "CHARGE", "STAY", "ROUTE", "JEWEL",
    "RING", "PUNT", "BRIDGE", "SWIM", "TAKE", "REST", "STRAIGHT", "SIT", "ACCEPT", "RUSH", "STARS", "HANDS", "KEY", "DASH", "DRINK", "PASS", "BRONZE", "IRON", "LOOK",
    "WEAPON", "SLASH", "PLUNGE", "CHEESE", "WOOD", "ROPE", "SHIELD", "125 KEY", "99 KEY", "111 KEY", "66 KEY", "9 KEY"
    ]

#sounds
click = mixer.Sound('./sounds/click1.wav')