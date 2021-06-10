import modesolverpy.mode_solver as ms
import modesolverpy.structure as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

w_wg_list = [round(0.2 +0.01*i,2) for i in range(0,81)]
total_list = []

def find_n_eff(wg_width:float)->float:
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
    wg_height = 0.4
    film_thickness = 0.5
    structure = st.RidgeWaveguide(wavelength, x_step, y_step, wg_height,wg_width,sub_height,sub_width,clad_height,n_sub,n_wg,angle,n_clad,film_thickness)
    mode_solver = ms.ModeSolverSemiVectorial(3, semi_vectorial_method='Ex')
    a = mode_solver.solve(structure)
    mode_solver.write_modes_to_file('example_modes_1.dat')
    return a["n_effs"][1].real

for i in w_wg_list:
    l = find_n_eff(i)
