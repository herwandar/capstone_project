import streamlit as st
from PIL import Image
import pandas as pd
import pickle
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/jogja_fix____.csv')
df.dropna()
df_mean = df.groupby('alamat')['harga'].mean().reset_index()
df_mean_sorted = df_mean.sort_values(by='harga',ascending=False)
df_desc = df.copy()
df_desc = df.drop(['latitude','longitude'],axis=1)

def format_price(value,pos):
  milyar = '{:.1f} Milyar'.format(value * 1e-9) if value >= 1e9 else ''
  juta = '{:.1f} Juta'.format(value * 1e-6) if 1e6 <= value <= 1e9 else ''
  ribu = '{:.1f} Ribu'.format(value * 1e-3) if 1e3 <= value < 1e6 else ''

  return '{}{}{}'.format(milyar,juta,ribu)

with open('model/random_forest_model.pkl', 'rb') as file:
    model_prediksi = pickle.load(file)

def main():
    selected_tab = st.sidebar.radio("Pilih Halaman", ["Home", "Analisa", "Prediksi Harga", "Kesimpulan"])
    if selected_tab == "Home":
        index()
    elif selected_tab == "Analisa":
        analisa_data()
    elif selected_tab == "Prediksi Harga":
        prediksi()
    elif selected_tab == "Kesimpulan":
        kesimpulan_data()
    st.sidebar.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")

def index():
    with st.container():
        st.markdown("<div style='text-align: center;'><h2>Dashboard Prediksi Harga Rumah Di Kota Yogyakarta</h2></div>", unsafe_allow_html=True)
        home_image = Image.open('Gambar/rumah.jpg')
        st.image(home_image,caption='sumber freepik',use_column_width=True)
        st.header('Definisi Rumah')
        st.write('mengutip dari situs [lamudi](https://www.lamudi.co.id/journal/definisi-rumah/). Pengertian rumah bisa dilihat dari dua sudut pandang utama, yaitu secara fisik dan psikologis. Berikut adalah pengertian hunian selengkapnya')
        st.subheader('Pengertian Rumah Secara Fisik')
        st.write("""Rumah secara fisik adalah suatu bangunan tempat tinggal yang memberikan perlindungan dari cuaca eksternal, seperti hujan, panas terik matahari, dan dingin. Menurut Kamus Besar Bahasa Indonesia (KBBI), rumah adalah “bangunan tempat tinggal.
                 'Undang-Undang Nomor 4 tahun 1992 tentang Perumahan dan Permukiman juga mendefinisikan rumah sebagai 'bangunan yang berfungsi sebagai tempat tinggal manusia atau hunian dan sarana pembinaan keluarga.'""")
        st.subheader('Pengertian Hunian Secara Psikologis')
        st.write("""Secara psikologis, rumah adalah tempat di mana penghuninya merasa nyaman, damai, dan bahagia. 
                 Hal ini menciptakan ruang bagi mereka untuk melakukan aktivitas sehari-hari dan pulang dengan perasaan tenang. 
                 Kualitas psikologis rumah ini sangat penting untuk kesejahteraan penghuninya""")
       
        st.header('Fungsi Rumah')
        st.write('Rumah memiliki beberapa fungsi yang sangat vital dalam kehidupan manusia. Fungsi utama rumah meliputi:')
        st.subheader('Tempat Tinggal')
        st.write("""Fungsi utama rumah adalah sebagai tempat tinggal atau hunian, di mana manusia dapat beristirahat, tidur, dan melindungi diri dari cuaca eksternal setelah beraktivitas di luar. Selain itu, 
                 rumah juga bisa diubah menjadi tempat usaha.""")
        st.subheader('Tempat Berlindung dari Kondisi Alam')
        st.write("""Rumah menyediakan tempat berteduh dan perlindungan dari berbagai kondisi alam, seperti hujan, panas terik, atau cuaca buruk lainnya. 
                 Penting untuk memastikan atap rumah dalam kondisi baik agar tidak terjadi kebocoran saat hujan turun.""")
        st.write("""Rumah adalah tempat utama di mana sebagian besar aktivitas harian manusia dilakukan, seperti makan, tidur, mandi, dan lain-lain. 
                 Kesejahteraan penghuni tergantung pada kenyamanan dan kebersihan rumah.""")
        st.subheader('Menunjukkan Identitas Penghuni')
        st.write("""Rumah juga mencerminkan identitas penghuninya. Cara rumah diatur dan didekorasi, model bangunannya, dan lokasinya dapat mencerminkan status sosial dan jati diri penghuninya.""")
        st.subheader('Tempat Berkumpulnya Keluarga')
        st.write("""Rumah adalah tempat di mana keluarga berkumpul, terutama saat mereka jarang bertemu selama berhari-hari. Ini adalah tempat di mana momen berharga dalam kehidupan keluarga terjadi.""")

        st.header("Tujuan")
        st.write("""Tujuan saya membuat dashboard ini agar pengguna memperkirakan harga rumah yang dinginkan dengan memasukan jumlah kamar tidur,ukuran bangunan,ukuran lahan,jumlah kamar mandi, dan fasilitas yang diinginkan""")



def prediksi():
    kamar_tidur = st.number_input('Jumlah Kamar Tidur',value=0,step=1)
    bangunan = st.number_input('Ukuran Bangunan (m²)',value=0,step=1)
    lahan =  st.number_input('Ukuran Lahan (m²)',value=0,step=1)
    kamar_mandi = st.number_input('jumlah kamar mandi',value=0,step=1)
    kota = st.selectbox('Pilih Lokasi', sorted(df['alamat'].unique().tolist()))
    selected_city = df[df['alamat'] == kota]
    latitude = selected_city['latitude'].astype(float).values[0]
    longitude = selected_city['longitude'].astype(float).values[0]
    sistem_alarm = st.select_slider("Sistem Alarm", options=["N", "Y"])
    gym = st.select_slider("Gym", options=["N", "Y"])
    internet_broadband_wifi = st.select_slider("Internet Broadband/Wifi", options=["N", "Y"])
    tv_kabel = st.select_slider("TV Kabel", options=["N", "Y"])
    pemanas_ruangan = st.select_slider("Pemanas Ruangan", options=["N", "Y"])
    air_panas = st.select_slider("Air Panas", options=["N", "Y"])
    telepon = st.select_slider("Telepon", options=["N", "Y"])
    televisi = st.select_slider("Televisi", options=["N", "Y"])
    kitchen_set = st.select_slider("Kitchen Set", options=["N", "Y"])
    garasi = st.select_slider("Garasi", options=["N", "Y"])
    secure_parking = st.select_slider("Secure Parking", options=["N", "Y"])
    kolam_renang = st.select_slider("Kolam Renang", options=["N", "Y"])
    lapangan_tenis = st.select_slider("Lapangan Tenis", options=["N", "Y"])
    balkon = st.select_slider("Balkon", options=["N", "Y"])
    dek = st.select_slider("Dek", options=["N", "Y"])
    halaman_terbuka = st.select_slider("Halaman Terbuka", options=["N", "Y"])
    area_hiburan_outdoor = st.select_slider("Area Hiburan Outdoor", options=["N", "Y"])
    pagar_penuh = st.select_slider("Pagar Penuh", options=["N", "Y"])
    taman = st.select_slider("Taman", options=["N", "Y"])
    keamanan_24_jam = st.select_slider("Keamanan 24 Jam", options=["N", "Y"])
    taman_bermain_anak = st.select_slider("Taman Bermain Anak", options=["N", "Y"])
    if st.button('Submit'):
        if model_prediksi is not None:
            mapping = {'Y': 1, 'N': 0}
            fasilitas = [
                mapping[sistem_alarm], mapping[gym], mapping[internet_broadband_wifi],
                mapping[tv_kabel], mapping[pemanas_ruangan], mapping[halaman_terbuka],
                mapping[air_panas], mapping[telepon], mapping[televisi],
                mapping[kitchen_set], mapping[garasi], mapping[secure_parking],
                mapping[kolam_renang], mapping[lapangan_tenis], mapping[balkon],
                mapping[dek], mapping[area_hiburan_outdoor], mapping[pagar_penuh],
                mapping[taman], mapping[keamanan_24_jam], mapping[taman_bermain_anak]
            ]
            features = [[kamar_tidur, bangunan, lahan, kamar_mandi,latitude,longitude ] + fasilitas]
            # predict_house1 = round(model_prediksi.predict(features)[0])
            predict_house1 = model_prediksi.predict(features)
            prediction = np.expm1(predict_house1)
        st.subheader('Prediksi Harga Rumah : ')
        st.write(f'Rp. {format_price(prediction[0],0)}')

def analisa_data():
        with st.container():
            opsi = st.selectbox('Opsi',('Harga','Kamar Tidur','Kamar Mandi','Bangunan','Lahan'))
            st.write('')
            st.write('')
            if opsi == 'Harga':
                with st.container():
                    col1 = st.columns(1)
                    col2 = st.columns(1)
                    with col1[0]:
                        harga = alt.Chart(df).transform_density(
                                density='harga',
                                as_=['harga', 'density'],
                            ).mark_area().encode(
                                x=alt.X('harga:Q',title=''),
                                y=alt.Y('density:Q',title='')
                            ).interactive()
                        st.altair_chart(harga,use_container_width=True)
                        st.text("""
                                terdapat rumah dengan harga yang lebih mahal dari rumah lainya 
                                yang membuat distribusi skew ke kanan""")
                        st.write('')
                        st.write('')
                    with col2[0]:
                        fig, ax = plt.subplots(figsize=(9, 6))
                        sns.boxplot(x=None, y='harga', data=df, ax=ax,)
                        plt.xlabel('')
                        plt.ylabel('')
                        st.pyplot(fig,use_container_width=True)
                        st.text("banyak outlier dan ada yang outlier extreme")
                        st.write('')
                        st.write('')
            elif opsi == 'Kamar Tidur':
                with st.container():
                    col1 = st.columns(1)
                    col2 = st.columns(1)
                    col3 = st.columns(1)
                    with col1[0]:
                        kamar_tidur = alt.Chart(df).mark_bar().encode(
                                x = alt.X('kamar_tidur',title=''),
                                y = alt.Y('harga',title=''),
                            ).interactive()
                        st.altair_chart(kamar_tidur,use_container_width=True)
                        st.text('kamar tidur paling banyak 4 dan ada rumah yang mempunyai kamar tidur 64')
                        st.write('')
                        st.write('')
                    with col2[0]:
                        fig, ax = plt.subplots(figsize=(9,6))
                        sns.boxplot(x=None, y='kamar_tidur', data=df, ax=ax,)
                        st.pyplot(fig,use_container_width=True)
                        plt.xlabel('')
                        plt.ylabel('')
                        st.text('outlier masih banyak')
                        st.write('')
                        st.write('')
                    with col3[0]:
                        kamar_tidur2 = alt.Chart(df).mark_circle().encode(
                            x=alt.X('kamar_tidur',title=''),
                            y=alt.Y('harga',title='')
                        ).interactive()
                        st.altair_chart(kamar_tidur2,use_container_width=True)
                        st.text("""rumah dengan jumlah kmar tidur yang sama banyak memiliki variasi harga""")
                        st.write('')
                        st.write('')
            elif opsi == 'Kamar Mandi':
                with st.container():
                    col1 = st.columns(1)
                    col2 = st.columns(1)
                    col3 = st.columns(1)
                    with col1[0]:
                        kamar_mandi = alt.Chart(df).mark_bar().encode(
                                x = alt.X('kamar_mandi',title=''),
                                y = alt.Y('harga',title=''),
                            ).interactive()
                        st.altair_chart(kamar_mandi,use_container_width=True)
                        st.text('mayoritas rumah mempunyai kamar mandi dibawah 5')
                        st.write('')
                        st.write('')
                    with col2[0]:
                        fig, ax = plt.subplots(figsize=(9, 6))
                        sns.boxplot(x=None, y='kamar_mandi', data=df, ax=ax,)
                        plt.xlabel('')
                        plt.ylabel('')
                        st.pyplot(fig,use_container_width=True)
                        st.text('masih banyak outlier dan outlier extreme')
                        st.write('')
                        st.write('')
                    with col3[0]:
                        kamar_mandi2 = alt.Chart(df).mark_circle().encode(
                            x=alt.X('kamar_mandi',title=''),
                            y=alt.Y('harga',title='')
                        ).interactive()
                        st.altair_chart(kamar_mandi2,use_container_width=True)
                        st.text("""
                                jumlah kamar mandi setiap nilai mempunyai variasi harga yang beragam
                                terdapat jumlah kamar mandi yang banyak dengan harga rendah""")
                        st.write('')
                        st.write('')
            elif opsi == 'Bangunan':
                with st.container():
                    col1 = st.columns(1)
                    col2 = st.columns(1)
                    col3 = st.columns(1)
                    with col1[0]:
                        bangunan = alt.Chart(df).transform_density(
                            density='bangunan',
                            as_=['bangunan','density']
                        ).mark_area().encode(
                                x = alt.X('bangunan:Q',title=''),
                                y = alt.Y('density:Q',title=''),
                            ).interactive()
                        st.altair_chart(bangunan,use_container_width=True)
                        st.text('terdapat bangunan yang lebih mahal dari yang lainya sehingga skew ke kanan')
                        st.write('')
                        st.write('')
                    with col2[0]:
                        fig, ax = plt.subplots(figsize=(9, 6))
                        sns.boxplot(x=None, y='bangunan', data=df, ax=ax,)
                        plt.xlabel('')
                        plt.ylabel('')
                        st.pyplot(fig)
                        st.text("""
                                mayoritas rumah memiliki luas bangunan di bawah 500 meter persegi
                                masih banyak outlier
                                """)
                        st.write('')
                        st.write('')
                    with col3[0]:
                        bangunan2 = alt.Chart(df).mark_circle().encode(
                            x=alt.X('bangunan',title=''),
                            y=alt.Y('harga',title='')
                        ).interactive()
                        st.altair_chart(bangunan2,use_container_width=True)
                        st.text("""
                                terdapat rumah dengan luas 1200 meter persegu dengan harga 55 M
                                walaupun ada bangunanya lebih luas 2400 meter persegi dengan harga di bawahnya 25 M 
                                """) 
                        st.write('')
                        st.write('')
            elif opsi == 'Lahan':
                with st.container():
                    col1 = st.columns(1)
                    col2 = st.columns(1)
                    col3 = st.columns(1)
                    with col1[0]:
                        lahan = alt.Chart(df).transform_density(
                            density='lahan',
                            as_=['lahan','density']
                        ).mark_area().encode(
                                x = alt.X('lahan:Q',title=''),
                                y = alt.Y('density:Q',title=''),
                            ).interactive()
                        st.altair_chart(lahan,use_container_width=True)
                        st.text('ada harga lahan yang lebih mahal dari yang lainya dan mengakibatkan skew ke kanan')
                        st.write('')
                        st.write('')
                    with col2[0]:
                        fig, ax = plt.subplots(figsize=(9, 6))
                        sns.boxplot(x=None, y='lahan', data=df, ax=ax,)
                        st.pyplot(fig)
                        plt.xlabel('')
                        plt.ylabel('')
                        st.text('banyak outlier dan outlier yang ekstreme')  
                        st.write('')
                        st.write('') 
                    with col3[0]:
                        lahan2 = alt.Chart(df).mark_circle().encode(
                            x=alt.X('lahan',title=''),
                            y=alt.Y('harga',title='')
                        ).interactive()
                        st.altair_chart(lahan2,use_container_width=True) 
                        st.text("""
                                lahan paling mahal seharga 55 M dengan luas 1900 meter persegi
                                tetapi ada yang lebih luas dengan harga dibawahnya 3400 meter persegi dengan harga 9.95 M
                                """)
                        st.write('')
                        st.write('')
            gambar = 'Gambar/output_image (1).png'
            image = Image.open(gambar)
            st.image(image,use_column_width=True)
            st.text("""
                    jumlah fasilitas mayoritas tidak semua rumah mempunyai fasilitas itu 
                    entah memang tidak ada atau memang lupa tak dicantumkan""")
            st.write('')
            st.write('')
            rata2_lokasi = alt.Chart(df_mean_sorted).mark_bar().encode(
                x=alt.X('harga:Q',title=''),
                y=alt.Y('alamat:N',title='',sort='-x')
            ).interactive()
            st.altair_chart(rata2_lokasi,use_container_width=True)
            st.text("""
                    pakualaman mempunyai harga rata-rata yang tinggi daripada yang lainya 
                    diikuti gondomanan,gondokusuman, dan danurejan di bawahnya
                    """)
            st.write('')
            st.write('')
            gambar2 = 'Gambar/heatmap_image.png'
            image2 = Image.open(gambar2)
            st.image(image2)
            st.text("""
                    dari heatmap semakin merah maka semakin kuat korelasinya sebaliknya jika semakin biru maka semakin lemah korelasinya
                    korelasi harga dengan kamar tidur,kamar mandi,dan lahan positif yang semakin banyak maka semakin mahal tapi lemah yang kenaikan harganya tidak signifikan
                    sedangkan harga dengan bangunan korelasi positif kuat berarti semakin mahal dan kenaikanya signifikan 
                    """)
def kesimpulan_data():
    with st.container():
        st.subheader('Kesimpulan')
        st.write("""Harga rumah juga ditentukan dengan beberapa faktor lainya selain luas lahan,luas bangunan,jumlah kamar tidur,dan kota 
                 mengutip dari [aesia](https://aesia.kemenkeu.go.id/berita-properti/properti/5-faktor-yang-mempengaruhi-harga-jual-rumah-98.html) ada 5 faktor yang mempengaruhi harga rumah :""")
        st.write("""1. Lokasi Rumah""")
        st.write("""Seperti yang sudah dijelaskan sebelumnya, lokasi merupakan faktor utama yang mempengaruhi nilai dan harga jual rumah. Lokasi meliputi lingkungan di sekitar rumah secara fisik maupun sosial.
                    Faktor penentu harga dari segi fisik yakni faktor landscape, vegetasi, temperatur udara, kualitas air, hingga suasana sekitar rumah. Sedangkan faktor sosial yang mempengaruhi harga yakni tingkat hidup dan sikap warga sekitar lokasi.""")
        st.write("2. Aksesibilitas Rumah")
        st.write("""Faktor yang mempengaruhi harga jual rumah selanjutnya adalah akses rumah ke pusat kegiatan atau keramaian. Bagi orang yang memiliki mobilitas tinggi, faktor ini dijadikan sebagai penentu utama dalam memilih sebuah hunian. 
                      Rumah yang memiliki akses mudah ke pusat keramaian, pusat perbelanjaan, pusat perkantoran, serta jalan tol memiliki nilai jual yang lebih tinggi dibanding rumah yang jauh dari pusat keramaian.""")
        st.write('3. Kondisi Fisik Rumah')
        st.write("""Kondisi fisik rumah menjadi salah satu faktor penting dalam menentukan harga jual rumah karena semua konsumen ingin memiliki hunian yang aman dan nyaman. Rumah dengan tipe baru akan lebih banyak diminati dibanding rumah tipe lama. Sama halnya dengan usia bangunan, semakin tua usia rumah, maka peminatnya akan semakin sedikit.""")
        st.write('4. Harga Properti di Sekitar Lokasi Rumah')
        st.write("""Faktor lain yang menentukan harga jual rumah yakni harga properti di sekitar lokasi rumah. Hal ini karena harga rumah cenderung mengikuti harga properti lain yang sudah terjual lebih dulu di sekitar lokasi rumah. Untuk itu, Anda perlu melakukan riset pasar harga di wilayah sekitar rumah yang akan dijual.""")
        st.write("""5. Kelengkapan Surat""")
        st.write("""Sebelum memutuskan untuk melakukan transaksi jual beli rumah, pastikan legalitas rumah sudah aman dan melengkapi semua surat-surat berharga seperti IMB, Akta Jual Beli (AJB), serta Sertifikat Hak Milik. Surat-surat ini akan mempengaruhi nilai dan harga jual rumah.""")
        
        st.subheader('Tentang Project')
        st.write("""Pengumpulan data dilakukan dengan metode web scraping menggunakan Octoparse 8 
                    pada tanggal 25 Februari 2024 di website [lamudi](https://www.lamudi.co.id/)""")
        
        with st.container():
            st.subheader('Pengembangan')
            st.write("""
                     untuk pengembangangan : \n 
                    1. Gunakan dataset yang mendetail seperti kelengkapan surat,dekat dengan tempat wisata,akses ke jalan raya,fasilitas,dan sebagainya 
                    2. Untuk model prediksi rumah masih perlu banyak pengembangan""")     


if __name__ == "__main__":
    main()