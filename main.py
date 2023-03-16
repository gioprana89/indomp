import streamlit as st 
import pandas as pd


import plotly.graph_objects as go

import plotly.express as px





tab1, tab2, tab3, tab4, tab5 = st.tabs(["Tentang", "Data", "Visualisasi Data", "Analisis Statistik", "Hasil Artikel di Jurnal Nasional/Internasional"])

with tab1:
   st.header("Tentang")
tab1.markdown("<h5 style='text-align: justify; color: blue;'>Hadirnya website ini bertujuan untuk menyimpan, mengumpulkan, menyajikan dan melakukan analisis statistik, pada data kinerja keuangan perusahaan yang terdaftar di Bursa Efek Indonesia (BEI).</h5>", unsafe_allow_html=True)
tab1.image("ugi.jpg", caption='Prana Ugiana Gio', width = 500)









with tab2:
   st.header("Data")
df = pd.read_excel('data_gabungan_seluruh_sektor.xlsx', index_col=0) 
tab2.dataframe(df, use_container_width=True )












with tab3:
   st.header("Visualisasi Data")
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
tab3.plotly_chart(fig, theme=None, use_container_width=True)










with tab4:
   st.header("Analisis Statistik")





with tab5:
   st.header("Hasil Artikel di Jurnal Nasional/Internasional")




