from src.tools.line import line
from src.tools.vector import vector
from src.tools.plane import plane
from src.core.muon import muon

import numpy as np

class voxel:

    def __init__(self, x, y, z, Lx, Ly, Lz):

        self.p = vector(x, y, z)
        self.pmin = vector(x - Lx / 2.0, y - Ly / 2.0, z - Lz / 2.0) 
        self.pmax = vector(x + Lx / 2.0, y + Ly / 2.0, z + Lz / 2.0) 
        self.nmuons = 0.0
        self.theta = 0.0
        self.theta2 = 0.0 
        
    def print(self, nx, ny, nz):

        print('------Voxel ', nx, ny, nz, '------')
        print('Position:', self.p.x(), self.p.y(), self.p.z())
        print('Size Lx:', (self.pmax.x()-self.pmin.x()), 'Size Ly:', (self.pmax.y()-self.pmin.y()), 'Size Lz:', (self.pmax.z()-self.pmin.z()))
                

    def update(self, theta):

        self.nmuons += 1
        self.theta += theta
        self.theta2 += theta*theta
        
    def getMean(self):

        return self.theta/self.nmuons
    
    def getRMS(self):

        return np.sqrt(self.theta2/self.nmuons)

    def isInside(self, p):

        # If p is inside the voxel returns true,
        # false otherwise.
        if p.x() <= self.pmin.x() or p.x() > self.pmax.x():
            return False 
        if p.y() <= self.pmin.y() or p.y() > self.pmax.y():
            return False 
        if p.z() <= self.pmin.z() or p.z() > self.pmax.z():
            return False 
        return True

   


   
