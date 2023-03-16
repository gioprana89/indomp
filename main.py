import streamlit as st 
import pandas as pd


import plotly.graph_objects as go

import plotly.express as px





tab1, tab2, tab3, tab4, tab5 = st.tabs(["Tentang", "Data", "Visualisasi Data", "Analisis Statistik", "Hasil Artikel di Jurnal Nasional/Internasional"])

with tab1:
   st.header(":blue[Tentang]")
tab1.markdown("<h5 style='text-align: justify; color: blue;'>Hadirnya website ini bertujuan untuk menyimpan, mengumpulkan, menyajikan dan melakukan analisis statistik, pada data kinerja keuangan perusahaan yang terdaftar di <a href = 'https://www.idx.co.id/id' target = '_blank'><font color = 'red'>Bursa Efek Indonesia (BEI)</font></a>. Sumber data berasal dari BEI dan <a href = 'https://finance.yahoo.com/?fr=sycsrp_catchall' target = '_blank'> <font color = 'red'>Yahoo Finance</a>.</h5>", unsafe_allow_html=True)

tab1.markdown("<h5 style='text-align: justify; color: blue;'><br>Pengguna website ini dapat mengakses data kinerja keuangan, seperti <i><font color = 'orange'>return on asset (ROA), return on equity (ROE), net interest margin (NIM)</font>,</i> dan sebagainya, yang sudah disajikan dalam tabel, pada Menu <b><font color = 'red'>Data</font></b>.</h5>", unsafe_allow_html=True)


tab1.markdown("<h5 style='text-align: justify; color: blue;'><br>Selain itu, pada menu <b><font color = 'red'>Visualisasi Data</font></b> menyajikan berbagai visualisasi data dalam bentuk grafik batang, garis, boxplot, scatterplot, dan sebagainya, berdasarkan data kinerja keuangan. Sementara pada menu <b><font color = 'red'>Analisis Statistik</font></b> disajikan hasil perhitungan statistik, seperti statistik deskriptif, korelasi, regresi, dan sebagainya.</h5>", unsafe_allow_html=True)


tab1.markdown("<h5 style='text-align: justify; color: blue;'>Terakhir, pada menu <b><font color = 'red'>Hasil Artikel di Jurnal Nasional/Internasional</font></b> disajikan hasil artikel kami, yang dipublikasi di jurnal nasional atau internasional. Semoga dengan hadirnya website ini dapat memberi manfaat.<br><br><br></h5>", unsafe_allow_html=True)




tab1.columns(3)[1].image("ugi.png", caption='', width = 350)



tab1.markdown("<h5 style='text-align: justify; color: red;'><br><br>               Supported by:<br></h5>", unsafe_allow_html=True)



tab1.image("gambar.png", caption='', width = 450)




with tab2:
   st.header(":blue[Data]")


tab2.markdown("<h5 style='text-align: justify; color: blue;'>Berikut disajikan data kinerja keuangan dari perusahaan yang terdaftar di Bursa Efek Indonesia (BEI). Data disajikan dalam bentuk tabel.<br><br></h5>", unsafe_allow_html=True)




df = pd.read_excel('data_gabungan_seluruh_sektor.xlsx', index_col=0) 
tab2.dataframe(df, use_container_width=True )












with tab3:
   st.header(":blue[Visualisasi Data]")
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
tab3.plotly_chart(fig, theme=None, use_container_width=True)










with tab4:
   st.header(":blue[Analisis Statistik]")





with tab5:
   st.header(":blue[Hasil Artikel di Jurnal Nasional/Internasional]")




