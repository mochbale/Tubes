import pandas as pd
import streamlit as st
from bokeh.io import show
from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool
from bokeh.palettes import Category10
from bokeh.plotting import figure

# baca dataset dari tautan GitHub
df = pd.read_csv('https://raw.githubusercontent.com/mochbale/Tubes/main/Dataset2.csv')

# daftar negara di Asia Tenggara
countries = ['Brunei Darussalam', 'Cambodia', 'Indonesia', "Lao People's Democratic Republic", 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Viet Nam']

p = figure(title="Penghasilan Beras di Asia Tenggara", x_axis_label='Tahun', y_axis_label='Penghasilan (Ton)')

# tambahkan garis untuk setiap negara
for i, country in enumerate(countries):
    df_country = df[df['Area'] == country]
    source_country = ColumnDataSource(df_country)
    p.line(x='Year', y='Value', source=source_country, legend_label=country, color=Category10[10][i])

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
