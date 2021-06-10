import modesolverpy.mode_solver as ms
import modesolverpy.structure as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.getcwd()

w_wg_list = [round(0.2 +0.01*i,2) for i in range(0,81)]
total_list = []

def find_n_eff2(wg_width:float)->float:
    x_step = 0.02
    y_step = 0.02
    sub_height = 0.5
    sub_width = 2.
    n_sub = 1.4
    n_wg = 3.4
    n_clad = 1.
    wavelength = 0.78
    angle = 90.
    clad_height = 0.5
    wg_height = 0.4
    film_thickness = 0.5
    structure = st.RidgeWaveguide(wavelength, x_step, y_step, wg_height,wg_width,sub_height,sub_width,clad_height,n_sub,n_wg,angle,n_clad,film_thickness)
    mode_solver = ms.ModeSolverSemiVectorial(2, semi_vectorial_method='Ex') 
    a = mode_solver.solve(structure)
    return a["n_effs"][1].real

def find_n_eff3(wg_width:float)->float:
    x_step = 0.02
    y_step = 0.02
    sub_height = 0.5
    sub_width = 2.
    n_sub = 1.4
    n_wg = 3.4
    n_clad = 1.
    wavelength = 0.78
    angle = 90.
    clad_height = 0.5
    wg_height = 0.4
    film_thickness = 0.5
    structure = st.RidgeWaveguide(wavelength, x_step, y_step, wg_height,wg_width,sub_height,sub_width,clad_height,n_sub,n_wg,angle,n_clad,film_thickness)
    mode_solver = ms.ModeSolverSemiVectorial(3, semi_vectorial_method='Ex') 
    a = mode_solver.solve(structure)
    return a["n_effs"][2].real

def find_n_eff4(wg_width:float)->float:
    x_step = 0.02
    y_step = 0.02
    sub_height = 0.5
    sub_width = 2.
    n_sub = 1.4
    n_wg = 3.4
    n_clad = 1.
    wavelength = 0.78
    angle = 90.
    clad_height = 0.5
    wg_height = 0.4
    film_thickness = 0.5
    structure = st.RidgeWaveguide(wavelength, x_step, y_step, wg_height,wg_width,sub_height,sub_width,clad_height,n_sub,n_wg,angle,n_clad,film_thickness)
    mode_solver = ms.ModeSolverSemiVectorial(4, semi_vectorial_method='Ex') 
    a = mode_solver.solve(structure)
    return a["n_effs"][3].real

   
for i in w_wg_list:
    t1 = find_n_eff2(i)
    t2 = find_n_eff3(i)
    t3 = find_n_eff4(i)
    total_list.append([i,t1, t2, t3])

df = pd.DataFrame(total_list, columns=['w_wg_list','n_eff2','n_eff3','n_eff4'])
df.to_csv('n_eff3.csv')
