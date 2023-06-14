import pandas as pd
import streamlit as st
from bokeh.io import show
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.layouts import column

# baca dataset dari tautan GitHub
df = pd.read_csv('https://raw.githubusercontent.com/mochbale/Tubes/main/Dataset2.csv')

df_indonesia = df[df['Area'] == 'Indonesia']

source = ColumnDataSource(df_indonesia)

p = figure(title="Penghasilan Beras di Indonesia", x_axis_label='Tahun', y_axis_label='Penghasilan')
p.line(x='Year', y='Value', source=source)

select = Select(title="Pilih Tahun:", value="1961", options=df_indonesia['Year'].unique().tolist())

def update_plot(attr, old, new):
    selected_year = select.value
    new_data = df_indonesia[df_indonesia['Year'] == selected_year]
    source.data = new_data

select.on_change('value', update_plot)

layout = column(select, p)
st.bokeh_chart(layout)
