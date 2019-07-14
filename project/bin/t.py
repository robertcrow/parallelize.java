from matplotlib import pyplot as plt

n = [1, 2, 4]



x1 = [1, 0.26/0.45, 0.182/0.45]
x2 = [1, 1.192/1.782, 0.591/1.782]
x3 = [1, 36.635/60.886, 26.034/60.886]

plt_handle1, = plt.plot(n, x1,label='5120 elementów')
plt_handle2, = plt.plot(n, x2,label='81920 elementów')
plt_handle3, = plt.plot(n, x3,label='512000 elementów')

plt.plot(n,[1, 0.5, 0.25],'--')


                        #, n, std_xmed, n, std_yhat, n, std_ymed)
plt.legend(handles=[plt_handle1, plt_handle2, plt_handle3])