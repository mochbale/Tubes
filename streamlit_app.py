import pandas as pd
import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# Membaca dataset
url = 'https://raw.githubusercontent.com/mochbale/Tubes/main/Dataset2.csv'
data = pd.read_csv(url)

# Membuat data source
source = ColumnDataSource(data)

# Membuat plot
plot = figure(x_range=data['Year'].unique(), plot_height=400, plot_width=800, title='Penghasilan Beras di Asia',
              x_axis_label='Tahun', y_axis_label='Penghasilan (Unit)')
plot.vbar(x='Year', top='Value', width=0.9, source=source)

# Menambahkan judul plot dan label sumbu
plot.title.align = 'center'
plot.title.text_font_size = '18px'
plot.xaxis.axis_label_text_font_size = '14px'
plot.yaxis.axis_label_text_font_size = '14px'

# Mengatur tampilan plot
plot.xgrid.grid_line_color = None
plot.y_range.start = 0

# Menampilkan plot menggunakan Streamlit
st.bokeh_chart(plot)

# Menampilkan tabel dataset
st.write(data)
