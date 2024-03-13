import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from matplotlib.ticker import FuncFormatter
from PIL import Image


df = pd.read_csv('data/jogja___.csv')
df_mean = df.groupby('lokasi')['harga'].mean().reset_index()
df_mean_sorted = df_mean.sort_values(by='harga',ascending=False)
jenis = df.groupby('jenis_rumah').size().reset_index(name='jumlah')
jumlah_rumah = df.groupby('lokasi').size().reset_index(name='jumlah_rumah')
jumlah_kategori = df.groupby('kategori').size().reset_index(name='Jumlah')



st.set_page_config(page_title = "Analisa Data")



def format_price(value,pos):
  milyar = '{:.1f}B'.format(value * 1e-9) if value >= 1e9 else ''
  juta = '{:.1f}M'.format(value * 1e-6) if 1e6 <= value <= 1e9 else ''
  ribu = '{:.1f}K'.format(value * 1e-3) if 1e3 <= value < 1e6 else ''

  return '{}{}{}'.format(milyar,juta,ribu)


st.markdown("<div style='text-align: center;'><h2>Analisa</h2></div>", unsafe_allow_html=True)
tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(['Harga','Kamar Tidur','Kamar Mandi','Bangunan','Lahan','Harga Rata-Rata','Fitur Dan Korelasi'])
with tab1:
    with st.container():
        harga = alt.Chart(df).transform_density(
                density='harga',
                as_=['harga', 'density'],
            ).mark_area().encode(
                x=alt.X('harga:Q',title=''),
                y=alt.Y('density:Q',title='')
            ).properties(
             title = 'Distribusi Harga Rumah'
             ).interactive()
        st.altair_chart(harga,use_container_width=True)
        st.write("""
                terdapat rumah dengan harga yang lebih mahal dari rumah lainya 
                yang membuat distribusi skew ke kanan""")
        st.write('')
        st.write('')
        fig, ax = plt.subplots(figsize=(9, 6))
        sns.boxplot(x=None, y='harga', data=df, ax=ax,)
        plt.gca().yaxis.set_major_formatter(FuncFormatter(format_price))
        ax.set_title('Boxplot Harga')
        plt.xlabel('')
        plt.ylabel('')
        st.pyplot(fig,use_container_width=True)
        st.write("banyak outlier")
        st.write('')
        st.write('')
        st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")

with tab2:
    with st.container():
        kamar_tidur = alt.Chart(df).mark_bar().encode(
                x = alt.X('kamar_tidur',title=''),
                y = alt.Y('harga',title=''),
            ).properties(
                 title='Distribusi Harga Kamar Tidur'
            ).interactive()
        st.altair_chart(kamar_tidur,use_container_width=True)
        st.write('kamar tidur paling banyak 4 dan 3')
        st.write('')
        st.write('')
        fig, ax = plt.subplots(figsize=(9,6))
        sns.boxplot(x=None, y='kamar_tidur', data=df, ax=ax,)
        st.pyplot(fig,use_container_width=True)
        ax.set_title('Boxplot Kamar Tidur')
        plt.xlabel('')
        plt.ylabel('')
        st.write('outlier masih banyak')
        st.write('')
        st.write('')
        kamar_tidur2 = alt.Chart(df).mark_circle().encode(
            x=alt.X('kamar_tidur',title=''),
            y=alt.Y('harga',title='')
        ).properties(
             title='Distribusi Kamar Tidur'
        ).interactive()
        st.altair_chart(kamar_tidur2,use_container_width=True)
        st.write("""rumah dengan jumlah kamar tidur yang sama banyak memiliki variasi harga""")
        st.write('')
        st.write('')
        st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")

with tab3:
        kamar_mandi = alt.Chart(df).mark_bar().encode(
                x = alt.X('kamar_mandi',title=''),
                y = alt.Y('harga',title=''),
            ).properties(
                 title='Distribusi Harga Kamar Mandi'
            ).interactive()
        st.altair_chart(kamar_mandi,use_container_width=True)
        st.write('mayoritas rumah mempunyai kamar mandi dibawah 5')
        st.write('')
        st.write('')
        fig, ax = plt.subplots(figsize=(9, 6))
        sns.boxplot(x=None, y='kamar_mandi', data=df, ax=ax,)
        ax.set_title('Boxplot Kamar Mandi')
        plt.xlabel('')
        plt.ylabel('')
        st.pyplot(fig,use_container_width=True)
        st.write('masih banyak outlier')
        st.write('')
        st.write('')
        kamar_mandi2 = alt.Chart(df).mark_circle().encode(
            x=alt.X('kamar_mandi',title=''),
            y=alt.Y('harga',title='')
        ).properties(
             title='Distribusi Kamar Mandi'
        ).interactive()
        st.altair_chart(kamar_mandi2,use_container_width=True)
        st.write("""
                jumlah kamar mandi setiap nilai mempunyai variasi harga yang beragam
                terdapat jumlah kamar mandi yang banyak dengan harga rendah""")
        st.write('')
        st.write('')
        st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")

with tab4:
        bangunan = alt.Chart(df).transform_density(
            density='bangunan',
            as_=['bangunan','density']
        ).mark_area().encode(
                x = alt.X('bangunan:Q',title=''),
                y = alt.Y('density:Q',title=''),
            ).properties(
                 title='Distribusi Luas Bangunan'
            ).interactive()
        st.altair_chart(bangunan,use_container_width=True)
        st.write('terdapat bangunan yang lebih mahal dari yang lainya sehingga skew ke kanan')
        st.write('')
        st.write('')
        fig, ax = plt.subplots(figsize=(9, 6))
        sns.boxplot(x=None, y='bangunan', data=df, ax=ax,)
        ax.set_title('Boxplot Bangunan')
        plt.xlabel('')
        plt.ylabel('')
        st.pyplot(fig)
        st.write("""
                mayoritas rumah memiliki luas bangunan di kurang lebih bawah 200 meter persegi dan
                masih banyak outlier
                """)
        st.write('')
        st.write('')
        bangunan2 = alt.Chart(df).mark_circle().encode(
            x=alt.X('bangunan',title=''),
            y=alt.Y('harga',title='')
        ).properties(
             title='Distribusi Harga Bangunan'
        ).interactive()
        st.altair_chart(bangunan2,use_container_width=True)
        st.write("""
                terdapat rumah dengan luas 500 meter persegi dengan harga 23,5 M
                walaupun ada bangunanya lebih luas 584 meter persegi dengan harga di bawahnya 3,7 M 
                """) 
        st.write('')
        st.write('')
        st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")

with tab5:
        lahan = alt.Chart(df).transform_density(
            density='lahan',
            as_=['lahan','density']
        ).mark_area().encode(
                x = alt.X('lahan:Q',title=''),
                y = alt.Y('density:Q',title=''),
            ).properties(
                 title='Distribusi Luas Lahan'
            ).interactive()
        st.altair_chart(lahan,use_container_width=True)
        st.write('ada harga lahan yang lebih mahal dari yang lainya dan mengakibatkan skew ke kanan')
        st.write('')
        st.write('')
        fig, ax = plt.subplots(figsize=(9, 6))
        sns.boxplot(x=None, y='lahan', data=df, ax=ax,)
        ax.set_title('Boxplot Lahan')
        plt.xlabel('')
        plt.ylabel('')
        st.pyplot(fig)
        st.write('banyak outlier')  
        st.write('')
        st.write('') 
        lahan2 = alt.Chart(df).mark_circle().encode(
            x=alt.X('lahan',title=''),
            y=alt.Y('harga',title='')
        ).properties(
             title='Distribusi Harga Lahan'
        ).interactive()
        st.altair_chart(lahan2,use_container_width=True) 
        st.write("""
                lahan paling mahal seharga 23,5 M dengan luas 506 meter persegi
                tetapi ada yang lebih luas dengan harga dibawahnya 547 meter persegi dengan harga 4,8 M
                """)
        st.write('')
        st.write('')
        st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")

with tab6:
    rata2_lokasi = alt.Chart(df_mean_sorted).mark_bar().encode(
    x=alt.X('harga:Q',title=''),
    y=alt.Y('lokasi:N',title='',sort='-x')
    ).properties(
         title='Harga Rata-Rata Lokasi'
    ).interactive()
    st.altair_chart(rata2_lokasi,use_container_width=True)
    st.write("""
        Gondomanan mempunyai harga rata-rata yang tinggi daripada yang lainya 
        """)
    st.write('')
    st.write('')
    rata_rata_harga = df.groupby(['lokasi', 'jenis_rumah'])['harga'].mean().reset_index()
    bar_chart_rata_rata_harga = alt.Chart(rata_rata_harga).mark_bar().encode(
    x=alt.X('mean(harga):Q', title=''),
    y=alt.Y('lokasi:N', title='', sort='-x'),
    color='jenis_rumah:N',
    tooltip=['lokasi:N', 'mean(harga):Q']
    ).properties(
         title='Harga Rata-Rata Jenis Rumah Per Lokasi'
    ).interactive()
    st.altair_chart(bar_chart_rata_rata_harga, use_container_width=True)
    st.write("""Bermacam-macam variasi dari harga rata-rata jenis rumah""")
    st.write('')
    st.write('')
    rata_rata_kategori = df.groupby(['lokasi', 'kategori'])['harga'].mean().reset_index()
    bar_chart_rata_rata_kategori= alt.Chart(rata_rata_kategori).mark_bar().encode(
    x=alt.X('mean(harga):Q', title=''),
    y=alt.Y('lokasi:N', title='', sort='-x'),
    color='kategori:N',
    tooltip=['lokasi:N', 'mean(harga):Q']
    ).properties(
         title='Harga Rata-Rata Kategori Rumah Per Lokasi'
    ).interactive()
    st.altair_chart(bar_chart_rata_rata_kategori, use_container_width=True)
    st.write("""bermacam-macam harga dari kategori rumah""")
    st.write('')
    st.write('')
    rumah_jumlah = alt.Chart(jumlah_rumah).mark_bar().encode(
    x=alt.X('jumlah_rumah:Q',title=''),
    y=alt.Y('lokasi:N',title='',sort='-x')
    ).properties(
         title='Jumlah Rumah Yang Di Jual Berdasarkan Lokasi'
    ).interactive()
    st.altair_chart(rumah_jumlah,use_container_width=True)
    st.write('Umbulharjo mempunyai jumlah paling banyak untuk rumah yang dijual')
    st.write('')
    st.write('')
    bar_chart_jumlah_rumah = alt.Chart(df).mark_bar().encode(
        x=alt.X('count():Q',title=''),
        y=alt.Y('lokasi:N',title='',sort='-x'),
        color='jenis_rumah:N',
        tooltip=['lokasi:N', 'count():Q']
    ).properties(
         title='Jumlah Rumah Yang Di Jual Berdasarkan Jenis Rumah Per Lokasi'
    ).interactive()
    st.altair_chart(bar_chart_jumlah_rumah,use_container_width=True)
    st.write('Rumah biasa paling banyak dijual dibanding jenis lainya')
    st.write('')
    st.write('')
    jumlah_rumah_kategori = df.groupby(['lokasi', 'kategori']).size().reset_index(name='jumlah_rumah')
    bar_chart_kategori_rumah = alt.Chart(df).mark_bar().encode(
        x=alt.X('count():Q',title=''),
        y=alt.Y('lokasi:N',title='',sort='-x'),
        color='kategori:N',
        tooltip=['lokasi:N', 'count():Q']
    ).properties(
         title='Jumlah Rumah Yang Di Jual Berdasarkan Kategori Rumah Per Lokasi'
    ).interactive()
    st.altair_chart(bar_chart_kategori_rumah,use_container_width=True)
    st.write('Rumah kategori non premium yang paling banyak dijual')
    st.write('')
    st.write('')

    
    st.subheader('Rata-Rata Harga Per Alamat')
    lokasi_pilihan = st.selectbox('Pilih Lokasi', sorted(df['lokasi'].unique(),key=lambda x: x))
    st.write('')
    st.write('')
    df_filtered = df[df['lokasi'] == lokasi_pilihan]
    lokasi_alamat = df_filtered.groupby('alamat').size().reset_index(name='jumlah_rumah')
    chart = alt.Chart(lokasi_alamat).mark_bar().encode(
    x=alt.X('jumlah_rumah:Q',title=''),
    y=alt.Y('alamat:N',title='',sort='-x')
    ).properties(
         title='Jumlah Rumah Yang Di Jual Per Alamat'
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
    st.write('')
    st.write('')
    lokasi_alamat_rata__ = df_filtered.groupby(['alamat'])['harga'].mean().reset_index()
    chart_1 = alt.Chart(lokasi_alamat_rata__).mark_bar().encode(
         x=alt.X('mean(harga):Q',title=''),
         y=alt.Y('alamat:N',title='',sort='-x')
    ).properties(
         title='Harga Rata-Rata Rumah Per Alamat'
    ).interactive()
    st.altair_chart(chart_1,use_container_width=True)
    st.write('')
    st.write('')
    jenis = df_filtered.groupby(['alamat','jenis_rumah']).size().reset_index(name='jumlah_rumah')
    chart_2 =  alt.Chart(jenis).mark_bar().encode(
         x=alt.X('count():Q',title=''),
        y=alt.Y('alamat:N',title='',sort='-x'),
        color='jenis_rumah:N',
        tooltip=['alamat:N', 'count():Q']
    ).properties(
         title='Jenis Rumah Yang Di Jual Per Alamat'
    ).interactive()
    st.altair_chart(chart_2,use_container_width=True)
    st.write('')
    st.write('')
    lokasi_alamat_rata = df_filtered.groupby(['alamat', 'jenis_rumah'])['harga'].mean().reset_index()
    lokasi_alamat_rata1 = alt.Chart(lokasi_alamat_rata).mark_bar().encode(
         x=alt.X('mean(harga):Q',title=''),
         y=alt.Y('alamat:N',title='',sort='-x'),
         color = 'jenis_rumah:N',
         tooltip=['alamat:N','mean(harga):Q']
    ).properties(
         title='Harga Rata-Rata Jenis Rumah Per Alamat'
    ).interactive()
    st.altair_chart(lokasi_alamat_rata1,use_container_width=True)
    st.write('')
    st.write('')
    kategori = df_filtered.groupby(['alamat','kategori']).size().reset_index(name='jumlah_rumah')
    chart_3 =  alt.Chart(kategori).mark_bar().encode(
         x=alt.X('count():Q',title=''),
        y=alt.Y('alamat:N',title='',sort='-x'),
        color='kategori:N',
        tooltip=['alamat:N', 'count():Q']
    ).properties(
         title='Kategori Rumah Yang Di Jual Per Alamat '
    ).interactive()
    st.altair_chart(chart_3,use_container_width=True)
    st.write('')
    st.write('')
    lokasi_alamat_rata2 = df_filtered.groupby(['alamat', 'kategori'])['harga'].mean().reset_index()
    lokasi_alamat_rata4 = alt.Chart(lokasi_alamat_rata2).mark_bar().encode(
         x=alt.X('mean(harga):Q',title=''),
         y=alt.Y('alamat:N',title='',sort='-x'),
         color = 'kategori:N',
         tooltip=['alamat:N','mean(harga):Q']
    ).properties(
         title='Harga Rata-Rata Kategori Rumah Per Alamat'
    ).interactive()
    st.altair_chart(lokasi_alamat_rata4,use_container_width=True)
    st.write('')
    st.write('')
    st.write("""Kita bisa melihat jumlah,harga rata-rata,jenis dan kategori dari alamat seusai dengan lokasi yang dipilih,
             begitu banyak variasi dari Jumlah,harga rata-rata,jenis dan kategori berdasarkan lokasi yang dipilh""")
    st.write('')
    st.write('')
    st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")

with tab7:
    st.subheader('Fitur Yang Ada Dalam Pembelian Rumah')
    gambar1 = 'gambar/pie.png'
    image1 = Image.open(gambar1)
    st.image(image1,use_column_width=True)
    st.write('Mayoritas tidak menampilkan fitur yang ada hanya sebagian saja')
    st.write('')
    st.write('')
    st.subheader('Sekitar Lokasi Rumah Yang Di Jual')
    gambar2 = 'gambar/lokasi.png'
    image2 = Image.open(gambar2)
    st.image(image2,use_column_width=True)
    st.write('Untuk sekitar lokasi ada mayoritas dekat keramaian dan tempat umum')
    st.write('')
    st.write('')
    st.subheader('Heatmap')
    gambar3 = 'gambar/heatmap.png'
    image3 = Image.open(gambar3)
    st.image(image3,use_column_width=True)
    st.write("""Korelasi harga dan kamar mandi,kamar tidur,bangunan dan lahan positif
             tetapi untuk korelasi harga dan kamar mandi beserta kamar tidur positif lemah jadi semakin harga mahal kenaikan tidak signifikan
             unruk harga dan lahan berserta bangunan positif kuat jadi semakin mahal harga kenaikan signifikan""")
    st.write('')
    st.write('')
    st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")