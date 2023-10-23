import streamlit as st
import math
from matplotlib import pyplot as plt

st.write('matplotlib chart')

fig, ax = plt.subplots()

x = [i * math.pi * 2 / 1000 for i in range(0,1000)]
y = [math.sin(i) for i in x]
ax.plot(x, y)

st.pyplot(fig)

