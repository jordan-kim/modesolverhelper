<h2> modesolverhelper <h2>

### Project members
+ Seoungmin Park
+ Sanghoon Kim
+ Kangseok Kim

### Requirements
 Getting Stared
   + Entered the Terminal, write down 'pip install -r requirements.txt' and download it. \
```pip install -r requirements.txt```
 
## Introduction
> + Background of Si photonics
>   + The problem is that electronics reduces energy efficiency when processing and processing data in a data center. 
>   + Data center capacity is increasing every year due to other Internet activities.
>   + An alternative to Si Electronics is the introduction of Si Photonics. 
>
> + Waveguide and Mode
>   + Waveguide traps light in the Waveguide structure and transmits it to a specific location. 
>   + Waveguide consists of Core and Cladding.Due to the geometric morphology of Waveguide and the refractive index of the components, there is a specific Efield profile in the Waveguide section, which is called Mode.
>  + If the structure of the Waveguide does not change in the direction of light travel, the light will proceed with the probability image in the form of an E-field profile in a particular mode. Waveguide's design parameters have different mode characteristics, so the process of optimizing Waveguide to achieve the desired mode is a must in Waveguide design.

***
## Theory
> +
#### modesolverpy
> + photonic mode solver with a nice interface and output 
> + simple structure drawing.
> + automated data saving and plotting via Gnuplotm
> + some limited (at this stage) data processing (finding MFD of fundamental mode), and
> + easily extensible library
>     
> The documentation for this project can be found here.

***
#### Example : Semi-parallel mode solving of a neff
> The following example finds the first two modes of a waveguide with the following, arbitrary, parameters:
> + thin-film thickness: 500nm
> + waveguide height: 250nm,
> + waveguide width: parameter,
> + refractive index of waveguide: 3.4,
> + refractive index of substrate: 1.4,
> + refractive index of cladding: 1, and
> + wavelength: 1310nm.
>     
##### Python script
```
import modesolverpy.mode_solver as ms
import modesolverpy.structure as st
import numpy as np
import pandas as pd

total_list = [] # element : [w_wg,t_soi,t_slab,n_eff]
w_wg_list = np.linspace(0,2,20) # 0.2 ~ 1


def find_n_eff(wg_width:float)->float:
    x_step = 0.02
    y_step = 0.02
    sub_height = 0.5
    sub_width = 2.
    n_sub = 1.4
    n_wg = 3.4
    n_clad = 1.
    wavelength = 1.31
    angle = 90.
    clad_height = 0.5
    film_thickness = 0.5
    wg_height = 0.25
    structure = st.RidgeWaveguide(wavelength, x_step, y_step, wg_height,
                                  wg_width,sub_height,sub_width,clad_height,
                                  n_sub,n_wg,angle,n_clad,film_thickness)
    mode_solver = ms.ModeSolverSemiVectorial(5, semi_vectorial_method='Ex')
    a = mode_solver.solve(structure)
    return a["n_effs"][0].real # 구해야 하는 것 [mode : 0에서의 n_eff]


for i in w_wg_list:
    a = find_n_eff(i)
    total_list.append([i,a])

df = pd.DataFrame(total_list,columns = ['w_wg_list','n_effs'])
print(df.head(5))
df.to_csv('n_effs_01csv')

 ```
##### How to use
##### mode
##### Structure
 example
<img src = "https://user-images.githubusercontent.com/80964488/121545451-8356f380-ca45-11eb-967f-4a7115f7fcf9.png" width="30%" height="30%"> <img src = "https://user-images.githubusercontent.com/80964488/121545462-8520b700-ca45-11eb-9e71-e9f79ca34c96.png" width="30%" height="30%"> <img src = "https://user-images.githubusercontent.com/80964488/121545475-881ba780-ca45-11eb-9969-d22fb45706fd.png" width="30%" height="30%">

##### Parameter
##### Result
 <img src = "https://user-images.githubusercontent.com/80964488/121543944-476f5e80-ca44-11eb-8ecc-15737bae8156.png" width="30%" height="30%"> <img src = "https://user-images.githubusercontent.com/80964488/121543992-535b2080-ca44-11eb-9f4d-b5b4719d514e.png" width="50%" height="50%">



***


***
##### Conclusion
   >- 
