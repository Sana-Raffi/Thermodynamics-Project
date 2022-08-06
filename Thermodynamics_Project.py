# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 15:38:53 2021

@author: sanar
"""

#Using Refrigerant as R134a.
#Without diffuser.

#Using experimental values and data collected from property chart of R134a

P11 = 137.89 #kPa
T11 = 8 #Degee Celsius
#Corresponding saturation Temperature
T1s1 = -19.15 #Degree Celsius
Cp = 0.958
h1g1 = 238.98 #kJ/Kg
H11 = h1g1 + Cp*(T11-T1s1)

P12 = 770 #kPa
T12 = 75 #Degee Celsius
#Corresponding saturation Temperature
T1s2 = 29.92 #Degree Celsius
h1g2 = 266.64 #kJ/Kg
H12 = h1g2 + Cp*(T12-T1s2)
H13 = 93.155 #kJ/Kg
H14 = H13
 
#Coefficient of performance
COP1 = (H11-H14)/(H12-H11)
print("COP without diffuser =",COP1)

#With diffuser(diffuser angle is 15 Degree).

#Using experimental values and data collected from property chart of R134a

P21 = 137.89 #kPa
T21 = 8 #Degee Celsius
#Corresponding saturation Temperature
T2s1 = -19.15 #Degree Celsius
Cp = 0.958
h2g1 = 238.98 #kJ/Kg
H21 = h2g1 + Cp*(T21-T2s1)


P22 = 764.9 #kPa
T22 = 60.4 #Degee Celsius
#Corresponding saturation Temperature
T2s2 = 29.69 #Degree Celsius
h2g2 = 266.53 #kJ/Kg
H22 = h2g2 + Cp*(T22-T2s2)
H23 = 93.155 #kJ/Kg
H24 = H23
 
#Coefficient of performance
COP2 = (H21-H24)/(H22-H21)
print("COP with diffuser =",COP2)

#Increase in COP while using diffuser
I = ((COP2-COP1)/COP2)*100

print("Enhancement of COP is",I,"%")




