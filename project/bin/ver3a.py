import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numba import jit

@jit(nopython=True)
def fdm():
    rho = 7800
    cp = 500
    lam = 46
    a = lam / (rho * cp)

    A = 0.32
    B = 1.6
    t = 1000

    T0 = 20
    hx = 0.001
    hy = 0.001
    tau = 1 / (a * 12 * (1 / hx**2 + 1 / hy**2))
    maxiter = 10

    Nx = int(B / hx)
    Ny = int(A / hy)
    Nt = round(t / tau)

    T = np.full((Nx,Ny),T0)
    T_new = np.copy(T)


    Tl = 1200
    Tr = 1200
    Tb = 1200
    Tt = 1200

    for i in range(0, Nx):
        for j in range(0, Ny):

            if (i == 0 and j == 0):
                T[i, j] = (Tb + Tl)/2

            elif (i == 0 and j == Ny - 1):
                T[i, j] = (Tt + Tl) / 2

            elif (i == Nx - 1 and j == 0):
                T[i, j] = (Tb + Tr)/2

            elif (i == Nx - 1 and j == Ny - 1):
                T[i, j] = (Tt + Tr)/2

            elif (i == 0):
                T[i,j] = Tl

            elif (i == Nx - 1):
                T[i,j] = Tr

            elif (j == 0):
                T[i, j] = Tb

            elif (j == Ny - 1):
                T[i, j] = Tt


    h = (hx**2 + hy**2) / (hx**2 * hy**2)
    cx = tau * a / hx**2
    cy = tau * a / hy**2


    for iter in range(maxiter) :
        for i in range(0, Nx):
            for j in range(0, Ny):

                if (i == 0 and j == 0):
                    T_new[i, j] = T[i][j] + 2 * a * tau * (
                            ((T[i + 1, j] + T[i, j + 1] - 2 * T[i, j]) / (hx * hx)) + (Tl + Tb) / (lam * hx))

                elif (i == 0 and j == Ny-1):
                    T_new[i, j] = T[i, j] + 2 * a * tau * (
                            ((T[i + 1][j] + T[i][j - 1] - 2 * T[i][j]) / (hx * hx)) + (Tl + Tt) / (lam * hx))

                elif (i == Nx-1 and j == 0):
                    T_new[i, j] = T[i, j] + 2 * a * tau * (
                            ((T[i - 1, j] + T[i, j + 1] - 2 * T[i, j]) / (hx * hx)) + (Tr + Tb) / (lam * hx))

                elif (i == Nx-1 and j == Ny-1):
                    T_new[i, j] = T[i, j] + 2 * a * tau * (
                            ((T[i - 1, j] + T[i, j - 1] - 2 * T[i, j]) / (hx * hx)) + (Tr + Tt) / (lam * hx))

                elif (i == 0):
                    T_new[i, j] = T[i,j] + a * tau * (T[i,j+1] - 2*T[i,j] + T[i,j-1] + (Tl + lam * (T[i+1,j] - T[i,j])/hx) * 2 * tau / (cp * rho *hx))

                elif (i == Nx - 1):
                    T_new[i, j] = T[i, j] + a * tau * (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1] + (Tr + lam * (T[i - 1, j] - T[i, j]) / hx) * 2 * tau / (cp * rho * hx))

                elif (j == 0):
                    T_new[i, j] = T[i, j] + a * tau * (T[i+1, j] - 2 * T[i, j] + T[i-1, j] + (
                                Tb + lam * (T[i, j+1] - T[i, j]) / hy) * 2 * tau / (cp * rho * hy))
                elif (j == Ny - 1):
                    T_new[i, j] = T[i, j] + a * tau * (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j] + (
                            Tt + lam * (T[i, j - 1] - T[i, j]) / hy) * 2 * tau / (cp * rho * hy))

                else:
                    T_new[i,j] = T[i, j] +  a * tau * (
                            ((T[i - 1, j] + T[i+1, j] - 2 * T[i, j]) / (hx * hx)) + (T[i, j-1] + T[i, j+1] - 2 * T[i, j]) / (hy * hy))

        T = np.copy(T_new)

    return T



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