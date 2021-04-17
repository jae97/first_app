import streamlit as st
import numpy as np
import pandas as pd
import time

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

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
