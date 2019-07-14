import numpy as np

class LHS:

    #Initializer
    def __init__(self, n, m):
        self.A = np.zeros((10,10))
        print(self.A)


class Properties:

    def __init__(self, rho, cp, tcon):
        self.rho = rho
        self.cp = cp
        self.tcon = tcon


#class UnsteadyFDM:

 #   def __init__(self, dt, tau, To):