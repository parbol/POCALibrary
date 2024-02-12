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
        try:
            return np.arccos(self.measurement1.v.dot(self.measurement2.v))
        except:
            self.measurement1.print()
            self.measurement2.print()
        return 0
    
         
    def POCAPoint(self):

        normalVector = self.measurement1.v.cross(self.measurement2.v)
        normalVector = normalVector / normalVector.norm()
        xpoca1 = self.measurement1.p + self.measurement1.v * (self.measurement2.p - self.measurement1.p).dot(self.measurement2.v.cross(normalVector))
        xpoca2 = self.measurement2.p + self.measurement2.v * (self.measurement2.p - self.measurement1.p).dot(self.measurement1.v.cross(normalVector))
        return (xpoca1 + xpoca2) * 0.5

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
