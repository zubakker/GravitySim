import pygame

from math import sqrt, atan2, sin, cos, pi

from planet import Planet, Ship

from utils import calc_mass_center

from CONSTANTS import SCREENSIZE, MENUSIZE


class Camera:

    def __init__( self,
                  screen,
                  center_pos = [0, 0],
                  zoom = 1.0,
                  rot = 0 ):
        self.center_pos = center_pos
        self.zoom = zoom
        self.rot = rot
        self.screen = screen
        self.center_body = ''
        self.rotate_around_body = ''
        self.start_ang = 0
        self.center_mass = True
        self.active_body = ''

    def center_on( self, body ):
        self.uncenter()
        self.center_body = body
    def center_on_mass( self ):
        self.uncenter()
        self.center_mass = True
    def uncenter( self ):
        self.center_body = ''
        self.rotate_around_body = ''
        self.center_mass = False
    def activate_body( self, body):
        self.activate_body = body
    def get_active_body( self ):
        return self.activate_body

    def rotate_around( self, body ):
        self.rotate_around_body = body
        sx, sy = self.rotate_around_body.get_pos()
        x,y = self.center_pos
        self.start_ang = atan2( sx-x, sy-y )

    def move( self, rel_pos ):
        self.uncenter()
        self.center_pos[0] += rel_pos[0]* self.zoom
        self.center_pos[1] += rel_pos[1]* self.zoom
    def move_to( self, pos ):
        self.uncenter()
        self.center_pos = pos



    def zoom_in( self, amount ):
        self.zoom /= amount
    def zoom_out( self, amount ):
        self.zoom *= amount

    def update( self, body_list ):
        if self.center_body:
            self.center_pos = self.center_body.get_pos()
        if self.rotate_around_body:
            sx, sy = self.rotate_around_body.get_pos()
            x,y = self.center_pos
            self.rot = atan2( sx-x, sy-y ) - self.start_ang
        if self.center_mass:
            pos = calc_mass_center( body_list ) 
            self.center_pos = pos
        

    def render( self, body_list, screen ):
        for body in body_list:
            sr = body.rad / self.zoom
            sx = (body.pos[0] - self.center_pos[0]) / self.zoom
            sy = (body.pos[1] - self.center_pos[1]) / self.zoom
            dist = sqrt(sx**2 + sy**2)
            ang = atan2(sy, sx) + self.rot
            x = cos(ang)*dist
            y = sin(ang)*dist

            if x - sr > 1 or \
                    x + sr < -1 or \
                    y - sr > 1 or \
                    y + sr < -1:
                continue

            if type(body) == Ship:
                ax = (sx+ sr * cos( body.rot ) + 0.5)*SCREENSIZE
                ay = (sy+ sr * sin( body.rot ) + 0.5)*SCREENSIZE
                bx = (sx+ sr * cos( body.rot + 2*pi/3 ) + 0.5)*SCREENSIZE
                by = (sy+ sr * sin( body.rot + 2*pi/3 ) + 0.5)*SCREENSIZE
                cx = (sx+ sr * cos( body.rot - 2*pi/3 ) + 0.5)*SCREENSIZE
                cy = (sy+ sr * sin( body.rot - 2*pi/3 ) + 0.5)*SCREENSIZE
                pygame.draw.polygon( screen, body.color, 
                        ((ax, ay), (bx, by), (cx, cy)) )
            else:
                pygame.draw.circle( screen, body.color, 
                        ((x+0.5)*SCREENSIZE, (y+0.5)*SCREENSIZE), sr*SCREENSIZE )

    def project( self, body ): 
        sr = body.rad / self.zoom
        sx = (body.pos[0] - self.center_pos[0]) / self.zoom
        sy = (body.pos[1] - self.center_pos[1]) / self.zoom
        dist = sqrt(sx**2 + sy**2)
        ang = atan2(sy, sx) + self.rot
        x = cos(ang)*dist
        y = sin(ang)*dist

        if x - sr > 1 or \
                x + sr < -1 or \
                y - sr > 1 or \
                y + sr < -1:
            return 0, 0, -1 

        return (x+0.5)*SCREENSIZE, (y+0.5)*SCREENSIZE, sr*SCREENSIZE



