import streamlit as st 
import pandas as pd

col1, col2, col3 = st.columns(3)











#st.header(":blue[Repositori Data Kinerja Keuangan Perusahaan Indonesia (Bursa Efek Indonesia)]")

st.markdown("<h1 style='text-align: center; color: blue;'>Repositori Data Kinerja Keuangan Perusahaan Indonesia (Bursa Efek Indonesia)</h1>", unsafe_allow_html=True)

st.image("ugi.jpg", caption='Prana Ugiana Gio', width = 500)


#st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)

df = pd.read_excel('data_gabungan_seluruh_sektor.xlsx', index_col=0) 

st.dataframe(df, use_container_width=True)