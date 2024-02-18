import sys
from src.core.muon import muon
from src.core.voxel import voxel
from src.tools.vector import vector
from src.tools.line import line

import matplotlib.pyplot as plt
import numpy as np

class activevolume:

    def __init__(self, x0, y0, z0, Lx, Ly, Lz, nx, ny, nz):

        self.x = x0
        self.y = y0
        self.z = z0
        self.center = vector(self.x, self.y, self.z)
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.stepx = self.Lx/self.nx
        self.stepy = self.Ly/self.ny
        self.stepz = self.Lz/self.nz
        self.framex = [self.x - self.Lx/2.0, self.x + self.Lx/2.0, self.stepx]
        self.framey = [self.y - self.Ly/2.0, self.y + self.Ly/2.0, self.stepy]
        self.framez = [self.z - self.Lz/2.0, self.z + self.Lz/2.0, self.stepz]
        originx = self.x - self.Lx / 2.0
        originy = self.y - self.Ly / 2.0
        originz = self.z - self.Lz / 2.0
        self.voxels = []
        # Creating the voxels
        for ix in range(0, self.nx):
            voxely = []
            for iy in range(0, self.ny):
                voxelz = []
                for iz in range(0, self.nz):
                    myVoxel = voxel(originx + self.stepx / 2.0 + ix * self.stepx, originy + self.stepy / 2.0 + iy * self.stepy, originz + self.stepz / 2.0 + iz * self.stepz, 
                                    self.stepx, self.stepy, self.stepz)
                    voxelz.append(myVoxel)
                voxely.append(voxelz)
            self.voxels.append(voxely)
 
       
    def isInside(self, p):

        if p.x() <= self.x - self.Lx / 2.0 or p.x() >= self.x + self.Lx / 2.0:
            return False
        if p.y() <= self.y - self.Ly / 2.0 or p.y() >= self.y + self.Ly / 2.0:
            return False
        if p.z() <= self.z - self.Lz / 2.0 or p.z() >= self.z + self.Lz / 2.0:
            return False
        return True
    
    def findVoxel(self, point):
 
        if not self.isInside(point):
            return -1,-1,-1
        x = point.x() + self.Lx/2.0
        y = point.y() + self.Ly/2.0
        z = point.z() + self.Lz/2.0
        
        i = int(x/self.stepx)
        j = int(y/self.stepy)
        k = int(z/self.stepz)

        return i,j,k

    def print(self):

        print('----------ActiveVolume----------')
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
        print('Lx:', self.Lx, 'Ly:', self.Ly, 'Lz:', self.Lz)
        for ix in range(0, self.nx):
            for iy in range(0, self.ny):
                for iz in range(0, self.nz):
                    self.voxels[ix][iy][iz].print(ix, iy, iz)
                    

