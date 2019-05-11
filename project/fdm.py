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


Tl = 140
Tr = 440
Tb = 140
Tt = 440

for i in range(0,Nx):
    for j in range(0,Ny):
        if (j == 0):
            T[i,j] = Tb
        elif (j == (Ny - 1)):
            T[i,j] = Tt
        elif (i == 0):
            T[i,j] = Tl
        elif (i == Nx - 1):
            T[i,j] = Tr



T_new = np.copy(T)


h = (hx**2 + hy**2) / (hx**2 * hy**2)
cx = tau * a / hx**2
cy = tau * a / hy**2
dif = 1
iter = 0



fig = plt.figure()
ax = plt.axes()

X, Y = np.meshgrid(np.arange(0.0,B,hx), np.arange(0.0, A, hy))



while abs(dif) > 0.01:

    iter = iter + 1

    # T_new[0, 0] = T[0, 0] + 2 * a * tau * (((T[1, 0] + T[0, 1] - 2 * T[0, 0]) / (hx * hx)) + (Tl + Td) / ( lam * hx))
    # Tnew[i][j] = T[i][j] + 2 * a * tau * (
    #             ((T[i + 1][j] + T[i][j - 1] - 2 * T[i][j]) / (hx * hx)) + (Tl + Tu) / (lam *hx))
    # Tnew[i][j] = T[i][j] + 2 * a * tau * (
    #             ((T[i - 1][j] + T[i][j + 1] - 2 * T[i][j]) / (hx * hx)) + (Tr + Td) / (lam *hx))
    # Tnew[i][j] = T[i][j] + 2 * a * tau * (
    #         ((T[i - 1][j] + T[i][j - 1] - 2 * T[i][j]) / (hx * hx)) + (Tr + Tu) / (lam *hx))


    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            T_new[i, j] = T[i, j] * (1 - 2*tau*a*h) + cx * T[i-1, j] + cx * T[i+1, j] + cy*T[i, j-1] + cy * T[i, j+1]

    dif = np.sum(T_new - T)

    print([iter, dif])
    T = np.copy(T_new)
    #Z = np.sin(T, dtype=float)

surf = ax.contourf(X, Y,np.transpose(T), rstride=1, cstride=1,
        map='viridis', edgecolor='none')
    #ax.set_title('surface');
plt.show()

print(T)


