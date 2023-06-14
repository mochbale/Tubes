import pandas as pd
import streamlit as st
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

# baca dataset dari tautan GitHub
df = pd.read_csv('https://raw.githubusercontent.com/mochbale/Tubes/main/Dataset2.csv')

df_indonesia = df[df['Area'] == 'Indonesia']

source = ColumnDataSource(df_indonesia)

p = figure(title="Penghasilan Beras di Indonesia", x_axis_label='Tahun', y_axis_label='Penghasilan')
p.line(x='Year', y='Value', source=source)

# atur format tampilan angka pada sumbu y
p.yaxis[0].formatter = NumeralTickFormatter(format="0,0")

st.bokeh_chart(p)
