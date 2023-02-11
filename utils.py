import pygame

from math import sqrt
from json import loads, dumps


from planet import Planet



def load_bodies( filename ):
    input = open( filename, 'r' )
    d = loads( input.read() )
    body_list = list()

    for body in d[ "body_list" ]:
        mass = body["mass"]
        rad = body["rad"] 
        vel = body["vel"] 
        pos = body["pos"] 
        color = body["color"]
        planet_inst = Planet( mass, rad, vel, pos, color )
        body_list.append( planet_inst )

    return body_list



def save_bodies( filename, body_list ):
    output = open( filename, 'w+' )
    d = { "body_list": list() }
    for body in body_list:
        body_chars = dict()
        body_chars["mass"] = body.get_mass()
        body_chars["rad"] = body.get_rad()
        body_chars["vel"] = body.get_vel()
        body_chars["pos"] = body.get_pos()
        body_chars["color"] = body.get_color()
        d[ "body_list" ].append( body_chars )
    output.write( dumps(d) )


def get_body( camera, body_list, screen_coords ):
    mouse_x, mouse_y = screen_coords
    for body in body_list:
        x, y, r = camera.project( body )
        sx = x - mouse_x
        sy = y - mouse_y
        dist = sqrt( sx*sx + sy*sy )
        if dist < r:
            return body
    return ""


def moving_zooming( event, camera, body_list ):
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
        if event.key == pygame.K_a:
            sleeptime = 0.03
        if event.key == pygame.K_p:
            pause_loop( screen, body_list, camera )
