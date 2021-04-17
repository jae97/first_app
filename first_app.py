import streamlit as st
import numpy as np
import pandas as pd

st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

if st.sidebar.checkbox('Show dataframe'):
  chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
  chart_data
  st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 20] + [37.76, -122.4],
    columns=['lat', 'lon'])

map_data
st.map(map_data)
