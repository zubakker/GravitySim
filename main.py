import pygame

from planet import Planet
from camera import Camera

from utils import load_bodies, get_body
from loops import main_loop
from CONSTANTS import SCREENSIZE, MENUSIZE



screen = pygame.display.set_mode( (SCREENSIZE, SCREENSIZE) )
MODE = "SIMULATION"
body_list = load_bodies( "resources/test1.json" )

camera = Camera(screen)

main_loop( screen, body_list, camera )
