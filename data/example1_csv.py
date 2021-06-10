import modesolverpy.mode_solver as ms
import modesolverpy.structure as st
import numpy as np
import pandas as pd

total_list = []
w_wg_list = [0.2 + 0.01 * i for i in range(0,3)]
t_soi_list = [0.2 + 0.01*i for i in range(0,3)]
t_slab_list = []

def find_n_eff(wg_width, film_thickness, wg_height:float)->float:
    x_step = 0.02
    y_step = 0.02
    sub_height = 0.5
    sub_width = 2.
    n_sub = 1.4
    n_wg = 3.4
    n_clad = 1.
    wavelength = 1.55
    angle = 90.
    clad_height = 0.5
    structure = st.RidgeWaveguide(wavelength, x_step, y_step, wg_height, wg_width, sub_height, sub_width, clad_height, n_sub, n_wg, angle, n_clad, film_thickness)
    mode_solver = ms.ModeSolverFullyVectorial(2, semi_vectorial_method='Ey')
    a = mode_solver.solve(structure)
    return a['n_effs'][1]

for i in w_wg_list:
    for j in t_soi_list:
        t_slab_list = [0.01*x for x in range(0,3) if (0.01*x <= j/2)]
        for k in t_slab_list:
            l = find_n_eff(i,j,j-k)
            total_list.append([i,j,k,l])

df = pd.DataFrame(total_list, columns=['w_wg_list', 't_soi_list', 't_slab_list', 'n_effs'])
print(df.head(5))
df.to_csv('n_effs.csv')