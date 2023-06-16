import pandas as pd
import streamlit as st
from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool
from bokeh.palettes import Category10
from bokeh.plotting import figure

# baca dataset dari tautan GitHub
df = pd.read_csv('https://raw.githubusercontent.com/mochbale/Tubes/main/Dataset2.csv')

# daftar negara di Asia Tenggara
countries = ['Brunei Darussalam', 'Cambodia', 'Indonesia', "Lao People's Democratic Republic", 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Viet Nam']

# tambahkan widget selectbox untuk memilih negara
selected_country = st.selectbox('Pilih Negara:', ['Semua Negara'] + countries)

# tambahkan tombol reset
if st.button('Reset'):
    selected_country = 'Semua Negara'

# buat plot baru dengan lebar dan tinggi yang ditentukan
p = figure(title="Penghasilan Beras di Asia Tenggara 1961~2021", x_axis_label='Tahun', y_axis_label='Penghasilan (Ton)', plot_width=920, plot_height=680)

if selected_country == 'Semua Negara':
    # tampilkan semua negara
    for i, country in enumerate(countries):
        df_country = df[df['Area'] == country]
        source_country = ColumnDataSource(df_country)
        p.line(x='Year', y='Value', source=source_country, legend_label=country, color=Category10[10][i])
else:
    # tampilkan hanya negara yang dipilih
    df_country = df[df['Area'] == selected_country]
    source_country = ColumnDataSource(df_country)
    p.line(x='Year', y='Value', source=source_country, legend_label=selected_country, color=Category10[10][0])

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
