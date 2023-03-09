

import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
BLACK = (0,0,0)
GREEN = (0,255,0)
LILAC = (216,145,239)
LILAC_A =(145,44,238) 

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 18)
    text = font.render(f"POINTS = {points}", True, LILAC_A)
    text_rect = text.get_rect()
    text_rect.center = (1000, 38)
    return text, text_rect

def get_deaths_dinosaur(deaths):
    font = pygame.font.Font(FONT_STYLE, 18)
    text = font.render(f"DEATHS ={deaths}", True, LILAC_A)
    text_rect = text.get_rect()
    text_rect.center = (1000, 58)
    return text, text_rect

def get_centered_message(message):
    font = pygame.font.Font(FONT_STYLE, 50)
    text = font.render(message, True, GREEN)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH //2, SCREEN_HEIGHT //2)
    return text, text_rect

def get_centered_message_down(message_donwn):
    font = pygame.font.Font(FONT_STYLE, 25)
    text = font.render(message_donwn, True, LILAC)
    text_rect = text.get_rect()
    text_rect.center = (120,580)
    return text, text_rect

def get_centered_message_title(message_title):
    font = pygame.font.Font(FONT_STYLE, 45)
    text = font.render(message_title, True, LILAC)
    text_rect = text.get_rect()
    text_rect.center = (550,250)
    return text, text_rect

def get_deaths_dinosaur_message(deaths_message):
    font = pygame.font.Font(FONT_STYLE, 18)
    text = font.render(deaths_message, True, LILAC)
    text_rect = text.get_rect()
    text_rect.center = (550,340 )
    return text, text_rect