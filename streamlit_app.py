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

# tambahkan widget slider untuk memilih rentang tahun
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
start_year, end_year = st.slider('Pilih Rentang Tahun:', min_year, max_year, (min_year, max_year))

# filter DataFrame untuk hanya menyertakan data untuk rentang tahun yang dipilih
df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

# hitung rata-rata penghasilan beras untuk rentang tahun yang dipilih dan negara yang dipilih
if selected_country == 'Semua Negara':
    avg_production = df['Value'].mean()
else:
    avg_production = df[df['Area'] == selected_country]['Value'].mean()
st.write(f"Rata-rata Penghasilan Beras: {avg_production:,.0f} Ton")

# hitung total penghasilan beras untuk setiap negara di Asia Tenggara dari tahun 1961 hingga 2021
total_production = df.groupby('Area')['Value'].sum().reset_index()

# urutkan negara berdasarkan total penghasilan beras dan ambil tiga negara teratas
top_countries = total_production[total_production['Area'].isin(countries)].sort_values(by='Value', ascending=False).head(3)

# tampilkan tiga negara teratas dan total produksi beras mereka
st.write("Top 3 Negara Penghasil Beras:")
for i, row in top_countries.iterrows():
    st.write(f"{row['Area']}: {row['Value']:,.0f} Ton")

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
