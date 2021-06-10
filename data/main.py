import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('n_eff3.csv')

xdata = df['w_wg_list']
ydata1 = df['n_eff2']
ydata2 = df['n_eff3']
ydata3 = df['n_eff4']

plt.figure()
plt.plot(xdata, ydata1)
plt.plot(xdata, ydata2)
plt.plot(xdata, ydata3)
plt.ylabel('n_eff')
plt.xlabel('wg_width')
plt.legend(['mode1', 'mode2','mode3'])
plt.title('wg_width & n_eff')
plt.show()