


import streamlit as st 


st.set_page_config(layout="wide")


import pandas as pd


import plotly.graph_objects as go

import plotly.express as px





st.markdown("<h2 style='text-align: center; color: blue;'>SCATTERPLOT<br><br></h5>", unsafe_allow_html=True)



col1, col2, col3 = st.columns([2,7,3])


pilih_var1 = col1.radio(
    "Variabel Pertama (Sumbu-X)",
    ('Return on Assets (ROA)', 'Return on Equity (ROE)', 
     'Ukuran Perusahaan',
     'Basic EPS',
     'Basic Average Shares',
     'Total Assets',
     'Free Cash Flow',
     'Debt to Asset Ratio (DAR)',
     'Debt to Equity Ratio (DER)'))


pilih_var2 = col1.radio(
    "Variabel Kedua (Sumbu-Y)",
    ('Return on Assets (ROA)', 'Return on Equity (ROE)', 
     'Ukuran Perusahaan',
     'Basic EPS',
     'Basic Average Shares',
     'Total Assets',
     'Free Cash Flow',
     'Debt to Asset Ratio (DAR)',
     'Debt to Equity Ratio (DER)'))




ukuran_titik = col1.slider('Ukuran Titik', 1, 50, 10)


df = pd.read_excel('data_gabungan_seluruh_sektor.xlsx', index_col=0) 
fig = px.scatter(df, x = pilih_var1, y = pilih_var2, color="Sektor",  symbol="Sektor",
                  hover_data=['Perusahaan', 'Tahun']
                  )
fig.update_traces(marker_size=ukuran_titik)
col2.plotly_chart(fig, theme=None, use_container_width=True)







df = pd.read_excel('data_gabungan_seluruh_sektor.xlsx', index_col=0) 
col3.dataframe(df, use_container_width=True )












