from src.core.muon import muon
from src.core.activevolume import activevolume
from src.tools.vector import vector
from src.tools.line import line

import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

import ROOT as r
import sys

class universe:
    
    # This class handles all the elements of the geometrical universe.
    # The universe is composed by an active volume that contains the voxels. 
    def __init__(self, x0, y0, z0, Lx, Ly, Lz, activeVol):

        self.x = x0
        self.y = y0
        self.z = z0
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz

        if self.x - self.Lx / 2.0 > activeVol.x - activeVol.Lx / 2.0:
            print('The active volume is not contained in the universe')
            sys.exit()
        if self.y - self.Ly / 2.0 > activeVol.y - activeVol.Ly / 2.0:
            print('The active volume is not contained in the universe')
            sys.exit()
        if self.z - self.Lz / 2.0 > activeVol.z - activeVol.Lz / 2.0:
            print('The active volume is not contained in the universe')
            sys.exit()
   
        self.center = vector(self.x, self.y, self.z)
        self.activeVol = activeVol
        

    def loadData(self, filename):

        f = r.TFile(filename)
        t = f.Get("globalReco")

        for ev in t:
        
            momentum = ev.e1
            p1 = vector(ev.x1, ev.y1, ev.z1)
            v1 = vector(ev.vx1, ev.vy1, ev.vz1)
            p2 = vector(ev.x2, ev.y2, ev.z2)
            v2 = vector(ev.vx2, ev.vy2, ev.vz2)
            meas1 = line(p1, v1)
            meas2 = line(p2, v2)
            # Create the muon
            mu = muon()
            mu.setMeasurement1(meas1)
            mu.setMeasurement2(meas2)
            mu.setMomentum(momentum)
            theta = mu.getDeltaTheta()        
            
            valid, point = mu.POCAPoint()
            if not valid:
                continue
            i,j,k = self.activeVol.findVoxel(point)
            
            if i == -1 and j == -1 and k == -1:
                continue
            self.activeVol.voxels[i][j][k].update(theta)


    def toNumpy(self):
        # Create a 3D numpy array with the deviations 
        mat = []
        for i in range(self.activeVol.nx):
            ly = []
            for j in range(self.activeVol.ny):
                lz = []
                for k in range(self.activeVol.nz):
                    a = 0                    
                    if self.activeVol.voxels[i][j][k].nmuons != 0:
                        a = self.activeVol.voxels[i][j][k].getRMS()
                    lz.append(a)
                ly.append(lz)
            mat.append(ly)
        
        return np.asarray(mat)


    def toNumpyXYProject(self, threshold):
        
        # Project the numpy array in the XY plane
        mat = []
        for i in range(self.activeVol.nx):
            maty = []
            for j in range(self.activeVol.ny):
                nmuonsz = 0
                ntheta2z = 0 
                for k in range(self.activeVol.nz):            
                    if self.activeVol.voxels[i][j][k].nmuons != 0:
                        nmuonsz += self.activeVol.voxels[i][j][k].nmuons
                        ntheta2z += self.activeVol.voxels[i][j][k].theta2
                if nmuonsz > threshold:
                    maty.append(np.sqrt(ntheta2z/nmuonsz))
                else:
                    maty.append(0.0)
            mat.append(maty)
        return np.transpose(np.asarray(mat))


    def toNumpyXY(self, k, threshold):
        
        # Get slice k in the XY plane
        mat = []
        for i in range(self.activeVol.nx):
            maty = []
            for j in range(self.activeVol.ny):
                if self.activeVol.voxels[i][j][k].nmuons > threshold:
                    maty.append(self.activeVol.voxels[i][j][k].getRMS())
                else:
                    maty.append(0.0) 
            mat.append(maty)
        return np.transpose(np.asarray(mat))


    def toNumpyXZProject(self, threshold):
        
        #Project the numpy array in the XZ plane
        mat = []
        for i in range(self.activeVol.nx):
            matz = []
            for k in range(self.activeVol.nz):
                nmuonsz = 0
                ntheta2z = 0
                for j in range(self.activeVol.ny):            
                    if self.activeVol.voxels[i][j][k].nmuons != 0:
                        nmuonsz += self.activeVol.voxels[i][j][k].nmuons
                        ntheta2z += self.activeVol.voxels[i][j][k].theta2
                if nmuonsz > threshold:
                    matz.append(np.sqrt(ntheta2z/nmuonsz))
                else:
                    matz.append(0.0)
            mat.append(matz)
        
        return np.transpose(np.asarray(mat))

    
    def toNumpyXZ(self, j, threshold):
        
        #Get the j slice in the XZ plane
        mat = []
        for i in range(self.activeVol.nx):
            matz = []
            for k in range(self.activeVol.nz):
                if self.activeVol.voxels[i][j][k].nmuons > threshold:
                    matz.append(self.activeVol.voxels[i][j][k].getRMS())
                else:
                    matz.append(0.0) 
            mat.append(matz)
        
        return np.transpose(np.asarray(mat))


    def toNumpyYZProject(self, threshold):
        
        #Project the numpy array in the YZ plane
        mat = []
        for j in range(self.activeVol.ny):
            matz = []
            for k in range(self.activeVol.nz):
                nmuonsz = 0
                ntheta2z = 0
                for i in range(self.activeVol.nx):            
                    if self.activeVol.voxels[i][j][k].nmuons != 0:
                        nmuonsz += self.activeVol.voxels[i][j][k].nmuons
                        ntheta2z += self.activeVol.voxels[i][j][k].theta2
                if nmuonsz > threshold:
                    matz.append(np.sqrt(ntheta2z/nmuonsz))
                else:
                    matz.append(0.0)
            mat.append(matz)

        return np.transpose(np.asarray(mat))

    
    def toNumpyYZ(self, i, threshold):
        
        #Get the i slice in the YZ plane
        mat = []
        for j in range(self.activeVol.ny):
            matz = []
            for k in range(self.activeVol.nz):
                if self.activeVol.voxels[i][j][k].nmuons > threshold:
                    matz.append(self.activeVol.voxels[i][j][k].getRMS())
                else:
                    matz.append(0.0) 
            mat.append(matz)
        
        return np.transpose(np.asarray(mat))


    def makePlot2D(self, name, framex, framey, mat, vmin_=1.0e-2, vmax_=1.0e-1):

        Y = np.arange(self.activeVol.y - self.activeVol.Ly/2.0, self.activeVol.y + self.activeVol.Ly/2.0, self.activeVol.stepy)
        Z = np.arange(self.activeVol.z - self.activeVol.Lz/2.0, self.activeVol.z + self.activeVol.Lz/2.0, self.activeVol.stepz)
        X = np.arange(framex[0], framex[1], framex[2])
        Y = np.arange(framey[0], framey[1], framey[2])
        x, y = np.meshgrid(X, Y)
        fig, ax = plt.subplots()
        c = ax.pcolormesh(x, y, mat, cmap=cm.plasma, norm=mpl.colors.LogNorm(vmin=vmin_, vmax=vmax_), shading='gouraud', rasterized=True)
        fig.colorbar(c, ax=ax)
        plt.savefig(name)
        plt.close(fig)


    def makePlot3D(self, name):

        mat = self.toNumpy()   
        
        #Color normalization
        norm = mpl.colors.Normalize(vmin=0.0, vmax=0.1)
        cmap = cm.inferno
        m = cm.ScalarMappable(norm=norm, cmap=cmap)

        # Create axis
        axes = [self.activeVol.nx, self.activeVol.ny, self.activeVol.nz]

        # Create Data
        data = np.ones(axes, dtype=np.bool_)

        # Control Transparency
        alpha = 0.8

        # Control colour
        colors = np.empty(axes + [4], dtype=np.float32)
        edgecolors = np.empty(axes + [4], dtype=np.float32)
        for i, col in enumerate(colors):
            for j, col2 in enumerate(col):
                for k, col3 in enumerate(col2):
                    rgbcol = m.to_rgba(mat[i][j][k])
                    colors[i][j][k] = [rgbcol[0], rgbcol[1], rgbcol[2], alpha]
                    edgecolors[i][j][k] = [rgbcol[0], rgbcol[1], rgbcol[2], 0]

        # Plot figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Voxels is used to customizations of the
        # sizes, positions and colors.
        ax.voxels(data, facecolors=colors, edgecolors=edgecolors)
        fig.savefig(name)
        plt.close(fig)


    def makeAllSlices(self, name, plane, threshold, vmin, vmax):

        if plane == 'XY':
            framex = self.activeVol.framex
            framey = self.activeVol.framey
            for i in range(self.activeVol.nz):
                namei = name + '_' + str(i) + '.png'
                mat = self.toNumpyXY(i, threshold)
                self.makePlot2D(namei, framex, framey, mat, vmin, vmax)
        elif plane == 'YZ':
            framey = self.activeVol.framey
            framez = self.activeVol.framez
            for i in range(self.activeVol.nx):
                namei = name + '_' + str(i) + '.png'
                mat = self.toNumpyYZ(i, threshold)
                self.makePlot2D(namei, framey, framez, mat, vmin, vmax)
        elif plane == 'XZ':
            framex = self.activeVol.framex
            framez = self.activeVol.framez
            for i in range(self.activeVol.ny):
                namei = name + '_' + str(i) + '.png'
                mat = self.toNumpyXZ(i, threshold)
                self.makePlot2D(namei, framex, framez, mat, vmin, vmax)
        else:
            print('Incorrect projection')
            sys.exit()


    def print(self):
        print('------------------Universe----------------')
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
        print('Lx:', self.Lx, 'Ly:', self.Ly, 'Lz:', self.Lz)
        self.activeVol.print()
       


 

