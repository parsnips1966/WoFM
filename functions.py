"""Contains all the functions which control sections of the game including setting up the screen and tutorials."""

from time import sleep
from random import randint
import pygame
from pygame.locals import *
import variables as vars
import constants as consts

def fight_tuto() -> None:
    """Explains how fighting works the first time the player enters a battle."""
    if vars.fight_tuto_done == False:
        story("When fighting monsters, 2 dice will be rolled for the monster\nand added to its Skill score to determine its Attack Strength.")
        story("You will do the same and whoever has\nthe higher Attack Strength will land a blow.")
        story("If the values are equal then\nyou have avoided each others' Attacks.")
        story("If a blow is landed it will take away 2 Stamina and\nthis is repeated until you or the monster are dead.")
        story("At some points you may be given the option of running away from a battle.\nIf you do the monster gets a hit on you as you flee.")
        vars.fight_tuto_done = True

def provs_tuto() -> None:
    """Explains what Provisions do the first time a player encounters them."""
    if vars.provs_tuto_done == False:
        return " which restore 4 Stamina points"
    vars.provs_tuto_done = True

def take_provs() -> None:
    """Changes stamina and removes a Provision"""
    if vars.provs > 0:
        vars.change_provs(-1)
        change_stats(1, 4)
    else:
        story("You have no Provisions left.")

def story(txt: str, timer: int=0) -> str:
    """Initialises the display and all the items on it.
    Allows the player to click to move on and to type if the game asks a question.
    :param txt: The main text which appears in the centre of the screen.
    """
    output = ""
    cursor_flash = 0
    txt = txt.split("\n")
    while True:
        cursor_flash += 1
        equip_str = ""
        surf = pygame.image.load("./images/" + vars.background + ".jpg").convert()
        consts.screen.blit(surf, surf.get_rect())
        for i in range(len(txt)):
            text = txt[i]
            blit_text(text, -1, consts.height // 2 + (i * 30), 40, outline = True, centerx = True)
        blit_text("Player", 10, 10, underline = True, colour = consts.GREEN, outline = True)
        blit_text("Skill: " + str(vars.hero[0]), 10, 35, colour = consts.GREEN, outline = True)
        blit_text("Stamina: " + str(vars.hero[1]), 10, 60, colour = consts.GREEN, outline = True)
        blit_text("Luck: " + str(vars.hero[2]), 10, 85, colour = consts.GREEN, outline = True)
        for item in vars.equipment:
            equip_str += item + ", "
        equip_str = equip_str[0:-2]
        blit_text("Gold: " + str(vars.gold), 10, 615, outline = True)
        blit_text("Provisions: " + str(vars.provs), 10, 640, outline = True)
        blit_text("Equipment: " + str(equip_str), 10, 665, outline = True)
        if vars.fighting:
            if len(vars.monster_name) < 6:
                blit_text(vars.monster_name, 1250, 10, underline = True, colour = consts.RED, outline = True)
            elif len(vars.monster_name) < 10:
                blit_text(vars.monster_name, 1200, 10, underline = True, colour = consts.RED, outline = True)
            else:
                blit_text(vars.monster_name, 1130, 10, underline = True, colour = consts.RED, outline = True)
            blit_text("Skill: " + str(vars.monster[0]), 1220, 35, colour = consts.RED, outline = True)
            blit_text("Stamina: " + str(vars.monster[1]), 1174, 60, colour = consts.RED, outline = True)
        if vars.dice_num != 0:
            if vars.dice_num < 7:
                draw_dice(vars.dice_num)
            else:
                if vars.dice_num - 6 < 1:
                    num = randint(1, 6)
                num = randint(6, vars.dice_num)
                draw_dice(num, 575)
                draw_dice(vars.dice_num - num, 725)
            vars.dice_num = 0
        pygame.display.flip()
        if txt[-1][-1] != "?":
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        return
        pygame.draw.rect(consts.screen, consts.BLACK, Rect(449, 509, 402, 62), 4)
        pygame.draw.rect(consts.screen, consts.WHITE, Rect(450, 510, 400, 60), 2)
        blit_text(output, 645 - 12 * len(output), 528, 40, colour = consts.BLUE, outline = True)
        pygame.display.flip()
        if cursor_flash % 2 == 1:
            pygame.draw.rect(consts.screen, consts.BLACK, Rect(651 + 7 * len(output), 519, 5, 42))
            pygame.draw.rect(consts.screen, consts.WHITE, Rect(652 + 7 * len(output), 520, 3, 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.display.flip()
                    if output in consts.INPUTS:
                        return output
                    else:
                        story("Please enter either one of the words in capitals, YES or NO.")
                        output = ""
                elif event.key == pygame.K_BACKSPACE:
                    if len(output) > 0:
                        output = output[: -1]
                if event.key in range(97, 123) or event.key in range(48, 58) or event.key == pygame.K_SPACE:
                    output += chr(event.key).upper()
            pygame.display.flip()
        if timer > 0:
            sleep(timer)
            return
            

def blit_text(txt: str, x: int, y: int, size: int=30, underline: bool=False, colour: tuple=(255, 255, 255), outline: bool=False, centerx: bool=False) -> None:
    """Blits text to the screen.
    :param txt: The text to blit to the screen.
    :param x: The point on the x axis where the left side of the text goes.
    :param y: The point on the y axis where the top of the text goes.
    :param size: The size of the text.
    :param underline: Dictates whether the text is underlined or not.
    :param colour: The colour of the text.
    :param outline: Dictates whether the text is outlined or not.
    """
    font = pygame.font.SysFont(None, size)
    font.set_underline(underline)
    main_text = font.render(txt, True, colour)
    if centerx:
        x = consts.width // 2 - main_text.get_width() // 2
    if outline:
        outline_text = font.render(txt, True, consts.BLACK)
        consts.screen.blit(outline_text, (x, y + 1))
        consts.screen.blit(outline_text, (x, y - 1))
        consts.screen.blit(outline_text, (x - 1, y))
        consts.screen.blit(outline_text, (x + 1, y))
        consts.screen.blit(outline_text, (x + 1, y + 1))
        consts.screen.blit(outline_text, (x + 1, y - 1))
        consts.screen.blit(outline_text, (x - 1, y + 1))
        consts.screen.blit(outline_text, (x - 1, y - 1))
    consts.screen.blit(main_text, (x, y))

def draw_dice(die_num: int, x: int=650, y: int=10) -> None:
    """
    Draws a die on the screen with the correct number of spots.
    :param die_num: The number of spots on the dice.
    :param x: The point on the x axis where the left side of the die is placed.
    :param y: The point on the y axis where the top of the die is placed.
    """
    pygame.draw.rect(consts.screen, consts.WHITE, Rect(x - 50, 150, 100, 100))
    if die_num == 1:
        pygame.draw.circle(consts.screen, consts.BLACK, (x, 200), y)
    elif die_num == 2:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)
    elif die_num == 3:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x, 200), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)
    elif die_num == 4:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 225), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)
    elif die_num == 5:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x, 200), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 225), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)
    elif die_num == 6:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 200), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 200), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 225), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)

def fight(name: str, escape_round: int=99) -> bool:
    """Controls fights between the player and a monster.
    :param name: The name of the player's opponent.
    :param escape_round: The round number from which the user has the choice to escape.
    """
    vars.fighting = True
    vars.monster_name = name
    round = 1
    while True:
        if vars.hero[1] > 0:
            if vars.monster[1] > 0:
                if round >= escape_round:
                    if story("Do you want to ESCAPE to run away or press enter to continue?") == "ESCAPE":
                        story("You escaped.")
                        change_stats(1, 2, "subtract")
                        vars.fighting = False
                        return False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return False
                hero_attack = randint(2, 12) + vars.hero[0]
                story("Your Attack Strength is " + str(hero_attack) + ".", 1)
                monster_attack = randint(2, 12) + vars.monster[0]
                story("The " + name + "'s Attack Strength is " + str(monster_attack) + ".", 1)
                if hero_attack > monster_attack:
                    if vars.monster[1] - 2 < 0:
                        vars.monster[1] = 0
                    else:
                        vars.monster[1] -= 2
                    story("You land a blow.", 1)
                elif hero_attack < monster_attack:
                    change_stats(1, -2)
                    story("The " + name + " lands a blow.", 1)
                round += 1
            else:
                story("The " + name + " is dead.")
                vars.fighting = False
                return True
        else:
            story("You are dead.", 999)
            return False

def change_stats(stat: int, amount: int, operation: str="add") -> None:
    """Changes one of the player's stats by an amount.
    :param stat: The stat which will be changed.
    :param amount: How much the stat will be changed by.
    """
    if operation == "subtract":
        if vars.hero[stat] - amount < 0:
            vars.hero[stat] = 0
            return story("You are dead.")
        vars.hero[stat] -= amount
        return
    if vars.hero[stat] + amount > vars.init_hero[stat]:
        vars.hero[stat] = vars.init_hero[stat]
        return
    vars.hero[stat] += amount

def stat_test(stat: int) -> bool:
    """Generates a random number between 2 and 12 and compares it to one of the player's stats."""
    if stat == 2:
        change_stats(2, 1, "subtract")
    vars.dice_num = randint(2, 12)
    if vars.dice_num <= vars.hero[stat]:
        return True
    return False

if __name__ == "__main__":
    raise Exception

pygame.init()