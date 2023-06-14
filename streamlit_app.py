import pandas as pd
import streamlit as st
from bokeh.io import show
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Select
from bokeh.plotting import figure
from bokeh.layouts import column

# baca dataset dari tautan GitHub
df = pd.read_csv('https://raw.githubusercontent.com/mochbale/Tubes/main/Dataset2.csv')

df_indonesia = df[df['Area'] == 'Indonesia']

source = ColumnDataSource(df_indonesia)

p = figure(title="Penghasilan Beras di Indonesia", x_axis_label='Tahun', y_axis_label='Penghasilan')
p.line(x='Year', y='Value', source=source)

select = Select(title="Pilih Tahun:", value="1961", options=[str(year) for year in df_indonesia['Year'].unique()])

callback = CustomJS(args=dict(source=source, select=select), code="""
    var data = source.data;
    var selected_year = select.value;
    var new_data = {'Area': [], 'Year': [], 'Unit': [], 'Value': [], 'Flag': [], 'Flag Description': []};
    for (var i = 0; i < data['Year'].length; i++) {
        if (data['Year'][i] == selected_year) {
            new_data['Area'].push(data['Area'][i]);
            new_data['Year'].push(data['Year'][i]);
            new_data['Unit'].push(data['Unit'][i]);
            new_data['Value'].push(data['Value'][i]);
            new_data['Flag'].push(data['Flag'][i]);
            new_data['Flag Description'].push(data['Flag Description'][i]);
        }
    }
    source.data = new_data;
""")

select.js_on_change('value', callback)

layout = column(select, p)
st.bokeh_chart(layout)
