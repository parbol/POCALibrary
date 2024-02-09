import numpy as np
from src.tools.vector import vector
from src.tools.plane import plane


class line:

    def __init__(self, p, v):

        self.p = p
        self.v = v
        n = v.norm()
        if n != 0:
            self.v = v/n
 
    def intersectionExists(self, plane):

        if plane.n.dot(self.v) == 0:
            return false 
        else:
            return true

    def intersection(self, plane):

        p = vector(0, 0, 0)
        if not intersectionExists(plane):
            return [float('inf'), p] 
        d = (plane.p-self.p).dot(plane.n) / self.v.dot(plane.n)
        p = self.p + d * self.v
        return [d, p]

    def intersectionZ(self, z):

        p = vector(0, 0, 0)
        if self.v.z() == 0:
            return [float('inf'), p] 
        d = (z - self.p.z())/self.v.z()
        p = self.p + self.v * d
        return d, p

    def intersectionY(self, y):

        p = vector(0, 0, 0)
        if self.v.y() == 0:
            return [float('inf'), p] 
        d = (y - self.p.y())/self.v.y()
        p = self.p + self.v * d
        return [d, p]

    def intersectionX(self, x):

        p = vector(0, 0, 0)
        if self.v.x() == 0:
            return [float('inf'), p] 
        d = (x - self.p.x())/self.v.x()
        p = self.p + self.v * d
        return [d, p]
 
    def orthogonalPlane(self, d):

        p = self.p + self.v * d
        return plane(p, self.v)

    def print(self, lineTag):

        print('Line:', lineTag, ' -> Point: (' + str(self.p.x()) + ', ' + str(self.p.y()) + ', ' + str(self.p.z()) + '), Vector: (' + str(self.v.x()) + ', ' + str(self.v.y()) + ', ' + str(self.v.z()) + ')')




