from src.tools.vector import vector

import numpy as np


class plane:

    def __init__(self, p, n):

        self.p = p
        k = n.norm()
        self.n = n
        if k != 0:
            self.n = n/k
    
 
    def getBasis(self):

        vx = vector(1.0, 0, 0)
        vy = vector(0, 1.0, 0)
        v = vector(0, 0, 0)
        if abs(vx.dot(self.n)) > abs(vy.dot(self.n)):
            v = vy
        else:
            v = vx
        vxp = vx - self.n * vx.dot(self.n) 
        vxp = vxp/vxp.norm()
        vyp = vxp ^ self.n
        vyp = vyp/vyp.norm()
     
        return vxp, vyp 
        

    def print(self, planeTag):

        print('Plane:', planeTag, ' -> Point: (' + str(self.p.x()) + ', ' + str(self.p.y()) + ', ' + str(self.p.z()) + '), Normal: (' + str(self.n.x()) + ', ' + str(self.n.y()) + ', ' + str(self.n.z()) + ')') 

