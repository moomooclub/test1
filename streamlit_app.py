import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# My first app
Hello *world!*
""")

# Table
st.write("""
# Table
""")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# Random NP

st.write("""
# Random NP
""")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


st.write("""
# Line Chart
""")
# Chart Data
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Plot a map

st.write("""
# Plot a map
""")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


# Using Widget
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

# Checkbox to show/ hide data
st.write("""
# Checkbox to show / hide data
""")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
