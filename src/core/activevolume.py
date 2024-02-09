import sys
from src.core.muon import muon
from src.core.voxel import voxel
from src.tools.vector import vector
from src.tools.line import line

import matplotlib.pyplot as plt
import numpy as np

class activevolume:

    def __init__(self, conf):

        self.x = conf.activex
        self.y = conf.activey
        self.z = conf.activez
        self.center = vector(self.x, self.y, self.z)
        self.Lx = conf.activeLx
        self.Ly = conf.activeLy
        self.Lz = conf.activeLz
        self.nx = conf.activenx
        self.ny = conf.activeny
        self.nz = conf.activenz
        self.stepx = self.Lx/self.nx
        self.stepy = self.Ly/self.ny
        self.stepz = self.Lz/self.nz
        originx = self.x - self.Lx / 2.0
        originy = self.y - self.Ly / 2.0
        originz = self.z - self.Lz / 2.0
        self.voxels = []
        if len(conf.l) != self.nx * self.ny * self.nz:
            print('The config file is not consistent')
            sys.exit(0)
        # Creating the voxels
        for ix in range(0, self.nx):
            voxely = []
            for iy in range(0, self.ny):
                voxelz = []
                for iz in range(0, self.nz):
                    myVoxel = voxel(originx + self.stepx / 2.0 + ix * self.stepx, originy + self.stepy / 2.0 + iy * self.stepy, originz + self.stepz / 2.0 + iz * self.stepz, 
                                    self.stepx, self.stepy, self.stepz, False, 0)
                    voxelz.append(myVoxel)
                voxely.append(voxelz)
            self.voxels.append(voxely)
 
        # Filling the information of the voxels
        self.blocks = set()
        for i, j in enumerate(conf.l):
            ix = conf.index[i][0]
            iy = conf.index[i][1]
            iz = conf.index[i][2]
            fixed = conf.fixed[i]
            self.voxels[ix][iy][iz].blockid = conf.blockid[i]
            if not fixed:
                self.blocks.add(conf.blockid[i])
            if not fixed:
                self.voxels[ix][iy][iz].isFixed = False
            else:
                self.voxels[ix][iy][iz].isFixed = True
 
        #Loop over the set
        self.listOfVoxelsPerBlock = []
        self.params = []
        for i, j in enumerate(self.blocks):
            a = []
            for k, s in enumerate(conf.l):
                if conf.fixed[k]:
                    continue
                ix = conf.index[k][0]
                iy = conf.index[k][1]
                iz = conf.index[k][2]
                if j == conf.blockid[k]:
                    a.append([ix, iy, iz])
            self.listOfVoxelsPerBlock.append(a)     
            self.params.append(self.voxels[a[0][0]][a[0][1]][a[0][2]].lrad)
                    

    def isInside(self, p):

        if p.x < self.x - self.Lx / 2.0 and p.x > self.x + self.Lx / 2.0:
            return False
        if p.y < self.y - self.Ly / 2.0 and p.y > self.y + self.Ly / 2.0:
            return False
        if p.z < self.z - self.Lz / 2.0 and p.z > self.z + self.Lz / 2.0:
            return False
        return True
    
    def findVoxel(self, point):
        for ix in range(0, self.nx):
            for iy in range(0, self.ny):
                if self.voxels[ix][iy][self.nz-1].isInside(point):
                    return ix,iy,self.nz-1
        return -1,-1,-1 

    def print(self):

        print('----------ActiveVolume----------')
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
        print('Lx:', self.Lx, 'Ly:', self.Ly, 'Lz:', self.Lz)
        for ix in range(0, self.nx):
            for iy in range(0, self.ny):
                for iz in range(0, self.nz):
                    self.voxels[ix][iy][iz].print(ix, iy, iz)
                    

