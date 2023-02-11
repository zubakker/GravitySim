class Planet:   # not necessary a planet, just a round body with gravity.

    def __init__( self, mass, rad, vel, pos, color ):
        self.mass = mass
        self.rad = rad
        self.vel = vel
        self.pos = pos
        self.color = color
    
    def attract( self, other ):
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        dist = dx**2 + dy**2 
        if dist == 0:
            return
        dv =  other.mass / dist
        self.vel[0] += dv * dx/dist
        self.vel[1] += dv * dy/dist

    def update( self ):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def get_mass( self ):
        return self.mass
    def get_rad( self ):
        return self.rad
    def get_vel( self ):
        return self.vel
    def get_pos( self ):
        return self.pos
    def get_color( self ):
        return self.color
