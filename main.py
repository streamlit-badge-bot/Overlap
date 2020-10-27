import streamlit as st
import numpy as np
import pandas as pd

st.title('Overlap Calculator')
st.header('Shankar Dutt')
st.write('shankar.dutt@anu.edu.au')
Radius = st.number_input('Radius (nm)',min_value=1, max_value=10000,step=1)
Fluence = st.number_input('Fluence (ions/cm^2)',value = 1E8,format="%.1f",step = 1E8)
r = Radius*10**-7
b = np.pi*r**2*Fluence
a = (1-np.exp(-b))
c = ((b-a)/a)*100
st.write('The overlap is (%) ', c)