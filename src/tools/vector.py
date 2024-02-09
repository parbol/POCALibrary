import numpy as np



class vector:

    def __init__(self, x, y, z):

        self.v = np.array([x, y, z])

    def norm(self):

       return np.sqrt(self.v[0] * self.v[0] + self.v[1] * self.v[1] + self.v[2] * self.v[2])  

    def x(self):

        return self.v[0]

    def y(self):

        return self.v[1]

    def z(self):

        return self.v[2]

    def thetax(self):
        return np.arctan2(self.v[0], self.v[2])

    def thetay(self): 
        return np.arctan2(self.v[1], self.v[2])

    def dphi(self, other):

        return np.acos(self.dot(other) / (self.norm() * other.norm()))

    def setFromAngle(self, thetax, thetay):

        self.v[0] = np.tan(thetax)
        self.v[1] = np.tan(thetay)
        self.v[2] = 1.0
        self.v = 1.0/self.norm() * self.v
     

    def __add__(self, other):
  
       x = vector(0, 0, 0)
       x.v = self.v + other.v 
       return x

    def __sub__(self, other):

       x = vector(0, 0, 0)
       x.v = self.v - other.v 
       return x

    def __mul__(self, k):

       x = vector(self.v[0]*k, self.v[1]*k, self.v[2]*k)
       return x

    def __truediv__(self, k):

       x = vector(self.v[0]/k, self.v[1]/k, self.v[2]/k)
       return x

    def dot(self, v2):

       return self.v[0] * v2.v[0] + self.v[1] * v2.v[1] + self.v[2] * v2.v[2]
    
    def __xor__(self, v2):

       x = vector(self.v[1] * v2.v[2] - self.v[2] * v2.v[1], self.v[2] * v2.v[0] - self.v[0] * v2.v[2], self.v[0] * v2.v[1] - self.v[1] * v2.v[0]) 
       return x

    def cross(self, v1):

        x = vector(self.v[1] * v1[2] - self.v[2] * v1[1], self.v[2] * v1[0] - self.v[0] * v1[2], self.v[0] * v1[1] - self.v[1] * v1[0])

    def print(self, vectortag):

        print('Vector:', vectortag, '-> (' + str(self.x()) + ', ' + str(self.y()) + ', ' + str(self.z()) + ')')




