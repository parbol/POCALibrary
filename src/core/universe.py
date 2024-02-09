from src.core.muon import muon
from src.core.activevolume import activevolume
from src.tools.vector import vector
from src.tools.line import line
import sys

class universe:
    
    # This class handles all the elements of the geometrical universe.
    # The universe is composed by an active volume that contains the voxels
    # and also two detectors. Even if most of the muon trajectory will go
    # through the active volume the universe will handle the magic happening
    # from the detector to the active volume. This is in principle conceived
    # as a pure geometrical extrapolation. 
    def __init__(self, conf, activeVol):

        x = conf.unix
        y = conf.uniy
        z = conf.uniz
        Lx = conf.uniLx
        Ly = conf.uniLy
        Lz = conf.uniLz

        if x - Lx / 2.0 > activeVol.x - activeVol.Lx / 2.0:
            print('The active volume is not contained in the universe')
            sys.exit()
        if y - Ly / 2.0 > activeVol.y - activeVol.Ly / 2.0:
            print('The active volume is not contained in the universe')
            sys.exit()
        if z - Lz / 2.0 > activeVol.z - activeVol.Lz / 2.0:
            print('The active volume is not contained in the universe')
            sys.exit()
  
        if x - Lx / 2.0 > detector1.x - detector1.Lx / 2.0:
            print('The detector1 is not contained in the universe')
            sys.exit()
        if y - Ly / 2.0 > detector1.y - detector1.Ly / 2.0:
            print('The detector1 is not contained in the universe')
            sys.exit()
        if z - Lz / 2.0 > detector1.z - detector1.Lz / 2.0:
            print('The detector1 volume is not contained in the universe')
            sys.exit()

        if x - Lx / 2.0 > detector2.x - detector2.Lx / 2.0:
            print('The detector2 is not contained in the universe')
            sys.exit()
        if y - Ly / 2.0 > detector2.y - detector2.Ly / 2.0:
            print('The detector2 is not contained in the universe')
            sys.exit()
        if z - Lz / 2.0 > detector2.z - detector2.Lz / 2.0:
            print('The detector2 is not contained in the universe')
            sys.exit()
   
        self.center = vector(x, y, z)
        self.x = x
        self.y = y
        self.z = z
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
        self.activeVol = activeVol
        

    def loadData(self, filename):

        f = r.TFile(filename)
        t = f.Get("hits")

        for ev in t:
        
            momentum = ev.p
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
            theta = mu.getDiff(meas1, meas2)
            i,j,k = self.activeVol.findVoxel(mu.getPOCAPoint())
            self.activeVol.voxels[i][j][k].update(theta)

   

    def print(self):
        print('------------------Universe----------------')
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
        print('Lx:', self.Lx, 'Ly:', self.Ly, 'Lz:', self.Lz)
        self.activeVol.print()
       


 

