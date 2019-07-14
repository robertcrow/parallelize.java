import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


rho = 700
cp = 500
lam = 46
a = lam / (rho * cp)

A = 0.32
B = 1.6
t = 1000

T0 = 20
hx = 0.01
hy = 0.01
tau = 1 / (a * 12 * (1 / hx**2 + 1 / hy**2))

Nx = int(B / hx)
Ny = int(A / hy)
Nt = round(t / tau)



T = np.full((Nx,Ny),T0)
T_new = np.copy(T)

Tl = 500
Tr = 293
Tb = 293
Tt = 500

h = (hx**2 + hy**2) / (hx**2 * hy**2)
cx = tau * a / hx**2
cy = tau * a / hy**2
dif = 1000
# iter = 0



fig = plt.figure()
ax = plt.axes()

X, Y = np.meshgrid(np.arange(0.0,B,hx), np.arange(0.0, A, hy))



for iter in range(0,200) :

    # iter = iter + 1

    # for i in range(0, Nx):
    #     for j in range(0, Ny):




    for i in range(0, Nx):
        for j in range(0, Ny):

            if (i == 0):
                T[i, j] = 2 * Tl - T[i+1, j]

            elif (i == Nx - 1):
                T[i, j] = 2 * Tr - T[i-1, j]

            elif (j == 0):
                # T_new[i, j] = 2 * Tb - T[i, j+1]
                T_new[i,j] = T[i,j+1]
            elif (j == Ny - 1):
                T_new[i, j] = 2 * Tt - T[i, j - 1]

            elif (i == 0 and j == 0):
                T_new[i, j] = T[i][j] + 2 * a * tau * (
                        ((T[i + 1, j] + T[i, j + 1] - 2 * T[i, j]) / (hx * hx)) + (Tl + Tb) / (lam * hx))

            elif (i == 0 and j == Ny - 1):
                T_new[i, j] = T[i, j] + 2 * a * tau * (
                        ((T[i + 1][j] + T[i][j - 1] - 2 * T[i][j]) / (hx * hx)) + (Tl + Tt) / (lam * hx))

            elif (i == Nx - 1 and j == 0):
                T_new[i, j] = T[i, j] + 2 * a * tau * (
                        ((T[i - 1, j] + T[i, j + 1] - 2 * T[i, j]) / (hx * hx)) + (Tr + Tb) / (lam * hx))

            elif (i == Nx - 1 and j == Ny - 1):
                T_new[i, j] = T[i, j] + 2 * a * tau * (
                        ((T[i - 1, j] + T[i, j - 1] - 2 * T[i, j]) / (hx * hx)) + (Tr + Tt) / (lam * hx))
            else:
                T_new[i, j] = T[i, j] * (1 - 2 * tau * a * h) + cx * T[i - 1, j] + cx * T[i + 1, j] + cy * T[
                i, j - 1] + cy * T[i, j + 1]


    dif = np.sum(T_new - T)

    print([iter, dif])
    T = np.copy(T_new)
    #Z = np.sin(T, dtype=float)

surf = ax.contourf(X, Y,np.transpose(T), rstride=1, cstride=1,
        map='jet', edgecolor='none', aspect='equal')

plt.show()

print(T)

# if (i == 0 and j == 0):
#     T_new[i, j] = T[i][j] + 2 * a * tau * (
#             ((T[i + 1, j] + T[i, j + 1] - 2 * T[i, j]) / (hx * hx)) + (Tl + Tb) / (lam * hx))
#
# elif (i == 0 and j == Ny - 1):
#     T_new[i, j] = T[i, j] + 2 * a * tau * (
#             ((T[i + 1][j] + T[i][j - 1] - 2 * T[i][j]) / (hx * hx)) + (Tl + Tt) / (lam * hx))
#
# elif (i == Nx - 1 and j == 0):
#     T_new[i, j] = T[i, j] + 2 * a * tau * (
#             ((T[i - 1, j] + T[i, j + 1] - 2 * T[i, j]) / (hx * hx)) + (Tr + Tb) / (lam * hx))
#
# elif (i == Nx - 1 and j == Ny - 1):
#     T_new[i, j] = T[i, j] + 2 * a * tau * (
#             ((T[i - 1, j] + T[i, j - 1] - 2 * T[i, j]) / (hx * hx)) + (Tr + Tt) / (lam * hx))
#
# elif (i == 0):
#     T_new[i, j] = T[i, j] + a * tau * (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1]) + (
#             Tl + (lam * (T[i + 1, j] - T[i, j]) / hx)) * (2 * tau / (cp * rho * hx))
# elif (i == Nx - 1):
#     T_new[i, j] = T[i, j] + a * tau * (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1]) + (
#             Tr + (lam * (T[i - 1, j] - T[i, j]) / hx)) * (2 * tau / (cp * rho * hx))
#
# elif (j == 0):
#     T_new[i, j] = T[i, j] + a * tau * (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]) + (
#             Tb + (lam * (T[i, j + 1] - T[i, j]) / hx)) * (2 * tau / (cp * rho * hx))
# elif (j == Ny - 1):
#     T_new[i, j] = T[i, j] + a * tau * (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]) + (
#             Tt + (lam * (T[i, j - 1] - T[i, j]) / hx)) * (2 * tau / (cp * rho * hx))
