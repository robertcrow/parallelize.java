import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import multiprocessing
from mpi4py import MPI 

class Domain:
    def __init__(self, A, B, hx, hy):
        self.A = A
        self.B = B
        self.hx = hx
        self.hy = hy
        


class Case:
    def __init__(self, domain, T0):
        self.Nx = int(domain.B / domain.hx)
        self.Ny = int(domain.A / domain.hy)
        self.T = np.full((self.Nx, self.Ny), T0)
        self.T_new = np.copy(self.T)


    def SetConstants(self, domain, tmax, rho, cp, lam):
        self.tmax = tmax
        self.rho = rho
        self.cp = cp
        self.lam = lam
        self.a = self.lam / (self.rho * self.cp)
        self.tau = 1 / (self.a * 12 * (1 / domain.hx ** 2 + 1 / domain.hy ** 2))        
        self.Nt = round(self.tmax / self.tau)
        self.cx = self.tau * self.a / domain.hx ** 2
        self.cy = self.tau * self.a / domain.hy ** 2
        self.c1 = 2 * self.a * self.tau / (self.lam * domain.hx)
        self.c2 = 2 * self.tau / (self.cp * self.rho * domain.hx)

    def SetBC(self, bc):
        self.T[0, 0] = (bc.Tb + bc.Tl) / 2
        self.T[0, self.Ny - 1] = (bc.Tt + bc.Tl) / 2
        self.T[self.Nx - 1, 0] = (bc.Tb + bc.Tr) / 2
        self.T[self.Nx - 1, self.Ny - 1] = (bc.Tt + bc.Tr) / 2

        for i in range(1, self.Nx - 1):
            self.T[i, 0] = bc.Tb
            self.T[i, self.Ny-1] = bc.Tt

        for j in range(1, self.Ny - 1):
            self.T[0, j] = bc.Tl
            self.T[self.Nx-1, j] = bc.Tr



    def ApplyBC(self, bc):
        self.T_new[0, 0] = self.T[0][0] * (1 - 4 * self.cx) \
            + 2 * self.cx * self.T[1, 0] \
            + 2 * self.cx * self.T[0, 1] \
            + (bc.Tl + bc.Tb) * self.c1

        self.T_new[0, self.Ny - 1] = self.T[0][self.Ny-1] * (1 - 4 * self.cx) \
            + 2 * self.cx * self.T[1, self.Ny-1] \
            + 2 * self.cx * self.T[0, self.Ny-2] \
            + (bc.Tl + bc.Tt) * self.c1

        self.T_new[self.Nx - 1, 0] = self.T[self.Nx-1][0] * (1 - 4 * self.cx) \
            + 2 * self.cx * self.T[self.Nx - 2, 0] \
            + 2 * self.cx * self.T[self.Nx - 1, 1] \
            + (bc.Tr + bc.Tb) * self.c1

        self.T_new[self.Nx - 1, self.Ny - 1] = self.T[self.Nx - 1][self.Ny - 1] * (1 - 4 * self.cx) \
            + 2 * self.cx * self.T[self.Nx - 2, self.Ny - 1] \
            + 2 * self.cx * self.T[self.Nx - 1, self.Ny - 2] \
            + (bc.Tr + bc.Tt) * self.c1

        for i in range(1, self.Ny-1):
            self.T_new[0, i] = self.T[0][i] * (1 - 2 * self.a * self.tau - 2 * self.cx) \
                + self.a * self.tau * self.T[0, i - 1] \
                + self.a * self.tau * self.T[0, i + 1] \
                + 2 * self.cx * self.T[1, i] \
                + self.c2 * bc.Tl

            self.T_new[self.Nx - 1, i] = self.T[self.Nx - 1, i] * (1 - 2 * self.a * self.tau - 2 * self.cx) \
                + self.a * self.tau * self.T[self.Nx - 1, i + 1] \
                + self.a * self.tau * self.T[self.Nx - 1, i - 1] \
                + self.c2 * bc.Tr \
                + 2 * self.cx * self.T[self.Nx - 2, i]

        for j in range(1, self.Nx-1):
            self.T_new[j, 0] = self.T[j][0] * (1 - 2 * self.a * self.tau - 2 * self.cx) \
                + self.a * self.tau * self.T[j - 1, 0] \
                + self.a * self.tau * self.T[j + 1, 0] \
                + 2 * self.cx * self.T[j, 1] \
                + self.c2 * bc.Tb

            self.T_new[j, self.Ny - 1] = self.T[j][self.Ny - 1] * (1 - 2 * self.a * self.tau - 2 * self.cx) \
                + self.a * self.tau * self.T[j - 1, self.Ny - 1] \
                + self.a * self.tau * self.T[j + 1, self.Ny - 1] \
                + 2 * self.cx * self.T[j, self.Ny - 2] \
                + self.c2 * bc.Tt



    def Compute(self, rank):

        for i in range(1, self.Nx-1):
            for j in range(1, self.Ny-1):
                self.T_new[i, j] = self.T[i, j] * (1 - 2 * self.cx - 2 * self.cy) \
                    + self.cx * self.T[i - 1, j] \
                    + self.cx * self.T[i + 1, j] \
                    + self.cy * self.T[i, j - 1] \
                    + self.cy * self.T[i, j + 1]

    def UpdateSolution(self):
        self.T = self.T_new
    

class BC:
    def __init__(self, Tl, Tr, Tb, Tt):
        self.Tl = Tl
        self.Tr = Tr
        self.Tb = Tb
        self.Tt = Tt

   


def fdm():

    domain = Domain(0.32, 1.6, 0.001, 0.001)
    case = Case(domain, 20)
    case.SetConstants(domain, 1000, 7800, 500, 46)
    bc = BC(1200, 1200, 1200, 1200)
    case.SetBC(bc)
    maxiter = 10

    for iter in range(maxiter):
        case.ApplyBC(bc)
        case.Compute(n_proc)
        case.UpdateSolution()


    return case.T


start = time.time()
T = fdm()
end = time.time()
print(end - start)

A = 0.32
B = 1.6
hx = 0.001
hy = 0.001
fig, ax = plt.subplots()
X, Y = np.meshgrid(np.arange(0.0, B, hx), np.arange(0.0, A, hy))
surf = ax.contourf(X, Y, np.transpose(T), rstride=1, cstride=1,
                   map='jet', edgecolor='none', aspect='equal')
ax.axis('equal')
cbar = fig.colorbar(surf)
plt.show()