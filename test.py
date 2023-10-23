import streamlit as st
import pandas as pd

df = pd.read_csv('auto-mpg.csv')
st.title("aut-mpg")
st.write(df)
st.text("this is a pen")

value_to_filter = st.slider('model year', 70, 85, 82)
filtered_data = df[df['model year'] <= value_to_filter]

st.scatter_chart(filtered_data, y='mpg', width=700, height=700, x='acceleration',color='cylinders',size='weight')
