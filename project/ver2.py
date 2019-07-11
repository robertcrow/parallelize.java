import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

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
    tau = 1 / (a * 12 * (1 / hx ** 2 + 1 / hy ** 2))
    maxiter = 10

    Nx = int(B / hx)
    Ny = int(A / hy)
    Nt = round(t / tau)

    T = np.full((Nx, Ny), T0)
    T_new = np.copy(T)

    Tl = 1200
    Tr = 1200
    Tb = 1200
    Tt = 1200

    # boundary nodes

    T[0, 0] = (Tb + Tl) / 2
    T[0, Ny - 1] = (Tt + Tl) / 2
    T[Nx - 1, 0] = (Tb + Tr) / 2
    T[Nx - 1, Ny - 1] = (Tt + Tr) / 2

    for i in range(1, Nx - 1):
        T[i, 0] = Tb
        T[i, Ny-1] = Tt

    for j in range(1, Ny - 1):
        T[0, j] = Tl
        T[Nx-1, j] = Tr

    h = (hx ** 2 + hy ** 2) / (hx ** 2 * hy ** 2)
    cx = tau * a / hx ** 2
    cy = tau * a / hy ** 2
    lhx = lam * hx
    lhy = lam * hy
    dif = 1000
    c1 = 2 * a * tau / (lam * hx)
    c2 = 2 * tau / (cp * rho * hx)

    for iter in range(maxiter):

        T_new[0, 0] = T[0][0] * (1 - 4 * cx) + 2 * cx * T[1, 0] + 2 * cx * T[0, 1] + (Tl + Tb) * c1
        T_new[0, Ny - 1] = T[0][Ny-1] * (1 - 4 * cx) + 2 * cx * T[1, Ny-1] + 2 * cx * T[0, Ny-2] + (Tl + Tt) * c1
        T_new[Nx - 1, 0] = T[Nx-1][0] * (1 - 4 * cx) + 2 * cx * T[Nx - 2, 0] + 2 * cx * T[Nx - 1, 1] + (Tr + Tb) * c1
        T_new[Nx - 1, Ny - 1] = T[Nx - 1][Ny - 1] * (1 - 4 * cx) + 2 * cx * T[Nx - 2, Ny - 1] + \
                                2 * cx * T[Nx - 1, Ny - 2] + (Tr + Tt) * c1

        # left and right boundaries
        for i in range(1, Ny-1):
            T_new[0, i] = T[0][i] * (1 - 2 * a * tau - 2 * cx) + a * tau * T[0, i - 1] + a * tau * T[
                0, i + 1] + 2 * cx * T[1, i] + c2 * Tl

            T_new[Nx - 1, i] = T[Nx - 1, i] * (1 - 2 * a * tau - 2 * cx) + a * tau * T[Nx - 1, i + 1] + \
                               a * tau * T[Nx - 1, i - 1] + \
                               c2 * Tr + 2 * cx * T[Nx - 2, i]

        # top and bottom boundaries
        for j in range(1, Nx-1):
            T_new[j, 0] = T[j][0] * (1 - 2 * a * tau - 2 * cx) + a * tau * T[j - 1, 0] + a * tau * T[
                j + 1, 0] + 2 * cx * T[j, 1] + c2 * Tb

            T_new[j, Ny - 1] = T[j][Ny - 1] * (1 - 2 * a * tau - 2 * cx) + a * tau * T[j - 1, Ny - 1] + a * tau * T[
                j + 1, Ny - 1] + 2 * cx * T[j, Ny - 2] + c2 * Tt

        # interior
        for i in range(1, Nx-1):
            for j in range(1, Ny-1):
                T_new[i, j] = T[i, j] * (1 - 2 * cx - 2 * cy) + cx * T[i - 1, j] + cx * T[i + 1, j] + cy * T[
                    i, j - 1] + cy * T[i, j + 1]

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