import pygame

from time import sleep

from planet import Planet, Ship

from utils import get_body, calc_mass_center

from CONSTANTS import SCREENSIZE, MENUSIZE

def moving_zooming( event, camera, body_list, screen ):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: # left button
            pos = pygame.mouse.get_pos()
            body = get_body( camera, body_list, pos )
            if type(body) == Ship:
                camera.activate_body( body )
            elif body:
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
        if event.key == pygame.K_LEFT:
            camera.move( (-0.1, 0) )
        if event.key == pygame.K_RIGHT:
            camera.move( (0.1, 0) )
        if event.key == pygame.K_UP:
            camera.move( (0, -0.1) )
        if event.key == pygame.K_DOWN:
            camera.move( (0, 0.1) )
        if event.key == pygame.K_m:
            camera.center_on_mass()

def render_planets( screen, camera, body_list ):
    pygame.draw.rect( screen, (72, 0, 0), (0,0, SCREENSIZE, SCREENSIZE) )
    camera.update( body_list )
    camera.render( body_list, screen )
    pygame.display.update()


def main_loop( screen, body_list, camera ):
    sleeptime = 0.03
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_loop( screen, body_list, camera )
                if event.key == pygame.K_u:
                    sleeptime = 0.03
            moving_zooming( event, camera, body_list, screen )
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            ship = camera.get_active_body()
            ship.change_speed( 0.001 )
        if keys[pygame.K_s]:
            ship = camera.get_active_body()
            ship.change_speed( -0.001 )
        if keys[pygame.K_a]:
            ship = camera.get_active_body()
            ship.rotate( 0.1 )
        if keys[pygame.K_d]:
            ship = camera.get_active_body()
            ship.rotate( -0.1 )
        for body in body_list:
            for sbody in body_list:
                body.attract( sbody )
        for body in body_list:
            body.update()
        render_planets( screen, camera, body_list )
        sleep( sleeptime )


def pause_loop( screen, body_list, camera ):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return
            moving_zooming( event, camera, body_list, screen )
        render_planets( screen, camera, body_list )
        sleep( 0.01 )

def add_loop():
    "..."

