import pygame

from time import sleep

from utils import get_body 

from CONSTANTS import SCREENSIZE, MENUSIZE

def moving_zooming( event, camera, body_list, screen ):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: # left button
            pos = pygame.mouse.get_pos()
            body = get_body( camera, body_list, pos )
            if body:
                camera.center_on( body )
        if event.button == 3: # right button
            pos = pygame.mouse.get_pos()
            body = get_body( camera, body_list, pos )
            if body:
                camera.rotate_around( body )
        if event.button == 4: # scroll up
            camera.zoom_in( 1.03 )
        if event.button == 5: # scroll down 
            camera.zoom_out( 1.03 )
    if event.type == pygame.KEYDOWN:
        '...'


def main_loop( screen, body_list, camera ):
    sleeptime = 0.1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_loop( screen, body_list, camera )
                if event.key == pygame.K_a:
                    sleeptime = 0.03
            moving_zooming( event, camera, body_list, screen )
        for body in body_list:
            for sbody in body_list:
                body.attract( sbody )
        for body in body_list:
            body.update()
        pygame.draw.rect( screen, (36, 0, 0), (0,0, SCREENSIZE, SCREENSIZE) )
        camera.update()
        camera.render( body_list, screen )
        pygame.display.update()
        sleep( sleeptime )


def pause_loop( screen, body_list, camera ):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return
            moving_zooming( event, camera, body_list, screen )
        pygame.draw.rect( screen, (36, 0, 0), (0,0, SCREENSIZE, SCREENSIZE) )
        camera.update()
        camera.render( body_list, screen )
        pygame.display.update()
        sleep( 0.01 )

def add_loop():
    "..."

