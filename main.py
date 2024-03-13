import streamlit as st
from PIL import Image
import pandas as pd
import pickle
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title = "Home")

st.markdown("<div style='text-align: center;'><h2>Dashboard Prediksi Harga Rumah Di Kota Yogyakarta</h2></div>", unsafe_allow_html=True)
st.divider()
st.write('')
st.write('')
st.write('Tujuan saya membuat prediksi rumah untuk : ')
st.subheader('1. Calon pembeli rumah')
st.write("""Membantu mereka menentukan apakah harga rumah yang mereka minati sesuai dengan anggaran mereka.
Memberikan gambaran tentang tren harga rumah di masa depan sehingga mereka dapat membuat keputusan pembelian yang tepat""")
st.subheader('2. Penjual rumah')
st.write("""Membantu mereka menentukan harga jual yang kompetitif untuk rumah mereka.
Memberikan gambaran tentang kemungkinan keuntungan atau kerugian yang akan mereka dapatkan dari penjualan rumah mereka.""")
st.subheader('3. Investor properti')
st.write("""Membantu mereka menentukan apakah suatu properti merupakan investasi yang baik.
Memberikan gambaran tentang potensi keuntungan atau kerugian yang akan mereka dapatkan dari investasi properti.""")
st.subheader('4. Pembuat kebijakan')
st.write("""Membantu mereka merumuskan kebijakan yang tepat untuk sektor perumahan.
Memberikan gambaran tentang dampak kebijakan yang dibuat terhadap pasar perumahan.""")
st.subheader('5. Masyarakat umum')
st.write("""Memberikan informasi tentang tren harga rumah di masa depan.
Membantu masyarakat memahami faktor-faktor yang mempengaruhi harga rumah""")
st.write('')
st.write('')
st.subheader('Alasan mengapa memprediksi harga rumah')
st.write("""Membantu dalam pengambilan keputusan: Prediksi harga rumah dapat membantu berbagai pihak dalam membuat keputusan yang tepat terkait dengan pembelian, penjualan, atau investasi properti.""")
st.write("""Memahami pasar properti: Prediksi harga rumah dapat membantu kita memahami tren dan faktor-faktor yang mempengaruhi pasar properti.""")
st.write("""Mempersiapkan diri untuk perubahan pasar: Prediksi harga rumah dapat membantu kita mempersiapkan diri untuk perubahan di pasar properti, seperti kenaikan suku bunga atau resesi ekonomi""")
st.error("""Perlu diingat bahwa prediksi harga rumah tidak selalu akurat. Ada banyak faktor yang dapat mempengaruhi harga rumah, dan prediksi hanya merupakan perkiraan. Namun, prediksi harga rumah dapat menjadi alat yang bermanfaat untuk membantu kita membuat keputusan yang tepat tentang properti.""")
st.write("""""")