from src.tools.line import line
from src.tools.vector import vector
from src.tools.plane import plane

import numpy as np


class muon:

    def __init__(self):

        v = vector(0,0,0)
        l = line(v, v)
        self.measurement1 = l
        self.measurement2 = l
        self.momentum = 3.0
        self.mass = 0.105

    def getDeltaTheta(self):
        
        costheta = self.measurement1.v.dot(self.measurement2.v)
        if costheta > 1.0:
            costheta = 1.0
        elif costheta < -1.0:
            costheta = -1.0
        return np.arccos(costheta)
          
         
    def POCAPoint(self):

        ps = self.measurement1.p
        pt = self.measurement2.p
        vs = self.measurement1.v
        vt = self.measurement2.v
    
        cross_st = vs.cross(vt)
        cross_stnorm = cross_st.norm()
        vts = vt.dot(vs)
        if cross_stnorm < 1.0e-7 or vts < 1.0e-7:
            return False, ps
        cross_sst = vs.cross(cross_st)
        DeltaR = ps-pt   
        xpoca2 = pt - vt * DeltaR.dot(cross_sst)/cross_stnorm**2
        xpoca1 = ps + vs * (xpoca2 - ps).dot(vs)/vts
            
        return True, (xpoca1 + xpoca2) * 0.5

    def setMomentum(self, p):
        self.momentum = p
        self.beta = p/np.sqrt(p**2 + self.mass**2)
        self.betamomentum = self.beta * self.momentum

    def setMeasurement1(self, meas1):
        self.measurement1 = meas1
    
    def setMeasurement2(self, meas2):
        self.measurement2 = meas2

    def print(self, tag):

        print('[Muon ' + tag + ']')
        self.measurement1.print('Up measurement')
        self.measurement2.print('Down measurement')
