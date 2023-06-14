import pandas as pd
import streamlit as st
from bokeh.io import show
from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool
from bokeh.plotting import figure

# baca dataset dari tautan GitHub
df = pd.read_csv('https://raw.githubusercontent.com/mochbale/Tubes/main/Dataset2.csv')

df_indonesia = df[df['Area'] == 'Indonesia']
df_malaysia = df[df['Area'] == 'Malaysia']

source_indonesia = ColumnDataSource(df_indonesia)
source_malaysia = ColumnDataSource(df_malaysia)

p = figure(title="Penghasilan Beras di Indonesia dan Malaysia", x_axis_label='Tahun', y_axis_label='Penghasilan (Ton)')
p.line(x='Year', y='Value', source=source_indonesia, legend_label="Indonesia", color="blue")
p.line(x='Year', y='Value', source=source_malaysia, legend_label="Malaysia", color="red")

# atur format tampilan angka pada sumbu y
p.yaxis[0].formatter = NumeralTickFormatter(format="0,0")

# tambahkan alat HoverTool ke plot
hover = HoverTool(tooltips=[("Negara", "@Area"), ("Tahun", "@Year"), ("Penghasilan", "@Value{0,0} Ton")])
p.add_tools(hover)

# tambahkan spasi antara judul dan plot
p.title.align = 'center'
p.title.text_font_size = '16pt'
p.title.offset = 20

st.bokeh_chart(p)
