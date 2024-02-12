from src.core.muon import muon
from src.core.activevolume import activevolume
from src.tools.vector import vector
from src.tools.line import line
import ROOT as r
import sys

class universe:
    
    # This class handles all the elements of the geometrical universe.
    # The universe is composed by an active volume that contains the voxels
    # and also two detectors. Even if most of the muon trajectory will go
    # through the active volume the universe will handle the magic happening
    # from the detector to the active volume. This is in principle conceived
    # as a pure geometrical extrapolation. 
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
            i,j,k = self.activeVol.findVoxel(mu.POCAPoint())
            if i == -1 and j == -1 and k == -1:
                continue
            self.activeVol.voxels[i][j][k].update(theta)

   

    def print(self):
        print('------------------Universe----------------')
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
        print('Lx:', self.Lx, 'Ly:', self.Ly, 'Lz:', self.Lz)
        self.activeVol.print()
       


 

