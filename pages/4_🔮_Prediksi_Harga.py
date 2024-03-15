import streamlit as st
import pandas as pd
import numpy as np
import joblib
import random


st.set_page_config(page_title = "Dashboard Prediksi Harga Rumah")


df = pd.read_csv('data/jogja___.csv')

def format_price(value,pos):
  milyar = '{:.1f} Milyar'.format(value * 1e-9) if value >= 1e9 else ''
  juta = '{:.1f} Juta'.format(value * 1e-6) if 1e6 <= value <= 1e9 else ''
  ribu = '{:.1f} Ribu'.format(value * 1e-3) if 1e3 <= value < 1e6 else ''

  return '{}{}{}'.format(milyar,juta,ribu)

model_prediksi = joblib.load('model/random_forest_model.pkl')



def predict():
    with st.container():
        st.markdown("<div style='text-align: center;'><h2>Prediksi Harga Rumah</h2></div>", unsafe_allow_html=True)
        st.divider()
        st.info('kamar tidur, bangunan, lahan, dan kamar mandi tidak boleh 0')
        col1,col2 = st.columns(2)
        with col1:
            kamar_tidur = st.number_input('Jumlah Kamar Tidur',value=0,step=1)
            bangunan = st.number_input('Ukuran Bangunan (m²)',value=0,step=1)
        with col2:
            lahan =  st.number_input('Ukuran Lahan (m²)',value=0,step=1)
            kamar_mandi = st.number_input('jumlah kamar mandi',value=0,step=1)
        kota = st.selectbox('Pilih Lokasi', sorted(df['lokasi'].unique().tolist()))
        selected_city = df[df['lokasi'] == kota]
        latitude = selected_city['latitude'].astype(float).values[0]
        longitude = selected_city['longitude'].astype(float).values[0]
        col1,col2,col3 = st.columns(3)
        with col1:
            sistem_alarm_check = st.checkbox("Sistem Alarm", value=False)
            sistem_alarm = "Y" if sistem_alarm_check else "N"
            gym_check = st.checkbox("Gym", value=False)
            gym = "Y" if gym_check else 'N'
            internet_broadband_wifi_check = st.checkbox("Internet Broadband/Wifi", value=False)
            internet_broadband_wifi = "Y" if internet_broadband_wifi_check else 'N'
            tv_kabel_check = st.checkbox("TV Kabel", value=False)
            tv_kabel = 'Y' if tv_kabel_check else 'N'
            pemanas_ruangan_check = st.checkbox("Pemanas Ruangan", value=False)
            pemanas_ruangan = "Y" if pemanas_ruangan_check else 'N'
            pendingin_ruangan_check = st.checkbox('Pendingin ruangan (AC)',value=False)
            pendingin_ruangan = 'Y' if pendingin_ruangan_check else 'N'
            air_panas_check = st.checkbox("Air Panas", value=False)
            air_panas = 'Y' if air_panas_check else 'N'
            telepon_check = st.checkbox("Telepon", value=False)
            telepon = 'Y' if telepon_check else 'N'
        with col2:
            televisi_check = st.checkbox("Televisi", value=False)
            televisi = 'Y' if televisi_check else 'N'
            kitchen_set_check = st.checkbox("Kitchen Set", value=False)
            kitchen_set = 'Y' if kitchen_set_check else 'N'
            garasi_check = st.checkbox("Garasi", value=False)
            garasi = 'Y' if garasi_check else 'N'
            secure_parking_check = st.checkbox("Secure Parking", value=False)
            secure_parking = 'Y' if secure_parking_check else 'N'
            kolam_renang_check = st.checkbox("Kolam Renang", value=False)
            kolam_renang = 'Y' if kolam_renang_check else 'N'
            lapangan_tenis_check = st.checkbox("Lapangan Tenis", value=False)
            lapangan_tenis = 'Y' if lapangan_tenis_check else 'N'
            balkon_check = st.checkbox("Balkon", value=False)
            balkon = 'Y' if balkon_check else 'N'
        with col3:
            dek_check = st.checkbox("Dek", value=False)
            dek = 'Y' if dek_check else 'N' 
            halaman_terbuka_check = st.checkbox("Halaman Terbuka", value=False)
            halaman_terbuka = 'Y' if halaman_terbuka_check else 'N'
            area_hiburan_outdoor = st.checkbox("Area Hiburan Outdoor", value=False)
            area_hiburan_outdoor =  'Y' if area_hiburan_outdoor else 'N'
            pagar_penuh_check = st.checkbox("Pagar Penuh", value=False)
            pagar_penuh = 'Y' if pagar_penuh_check else 'N'
            taman_check = st.checkbox("Taman", value=False)
            taman = 'Y' if taman_check else 'N'
            keamanan_24_jam_check = st.checkbox('Keamanan 24 Jam',value=False)
            keamanan_24_jam = 'Y' if keamanan_24_jam_check else 'N'	
            taman_bermain_anak_check = st.checkbox('Taman Bermain Anak',value=False)
            taman_bermain_anak = 'Y' if taman_bermain_anak_check else 'N'
        
        # with st.expander('Sekitar Lokasi'):
        #     col1,col2,col3 = st.columns(3)
        #     with col1:
        #         malioboro_check = st.checkbox('Malioboro', value=False)
        #         malioboro = 'Y' if malioboro_check else 'N'

        #         masjid_jogokariyan_check = st.checkbox('Masjid Jogokariyan', value=False)
        #         masjid_jogokariyan = 'Y' if masjid_jogokariyan_check else 'N'

        #         malioboro_mall_check = st.checkbox('Malioboro Mall', value=False)
        #         malioboro_mall = 'Y' if malioboro_mall_check else 'N'

        #         universitas_ahmad_dahlan_check = st.checkbox('Universitas Ahmad Dahlan', value=False)
        #         universitas_ahmad_dahlan = 'Y' if universitas_ahmad_dahlan_check else 'N'

        #         terminal_giwangan_check = st.checkbox('Terminal Giwangan', value=False)
        #         terminal_giwangan = 'Y' if terminal_giwangan_check else 'N'

        #         universitas_gadjah_mada_check = st.checkbox('Universitas Gadjah Mada', value=False)
        #         universitas_gadjah_mada = 'Y' if universitas_gadjah_mada_check else 'N'

        #         universitas_sarjanawiyata_tamansiswa_check = st.checkbox('Universitas Sarjanawiyata Tamansiswa', value=False)
        #         universitas_sarjanawiyata_tamansiswa = 'Y' if universitas_sarjanawiyata_tamansiswa_check else 'N'

        #         universitas_pembangunan_nasional_veteran_yogyakarta_check = st.checkbox('Universitas Pembangunan Nasional Veteran Yogyakarta', value=False)
        #         universitas_pembangunan_nasional_veteran_yogyakarta = 'Y' if universitas_pembangunan_nasional_veteran_yogyakarta_check else 'N'

        #         lippo_plaza_jogja_check = st.checkbox('Lippo Plaza Jogja', value=False)
        #         lippo_plaza_jogja = 'Y' if lippo_plaza_jogja_check else 'N'

        #         masjid_gedhe_kauman_check = st.checkbox('Masjid Gedhe Kauman', value=False)
        #         masjid_gedhe_kauman = 'Y' if masjid_gedhe_kauman_check else 'N'

        #         universitas_islam_indonesia_check = st.checkbox('Universitas Islam Indonesia', value=False)
        #         universitas_islam_indonesia = 'Y' if universitas_islam_indonesia_check else 'N'
            
        #         sleman_city_hall_check = st.checkbox('Sleman City Hall', value=False)
        #         sleman_city_hall = 'Y' if sleman_city_hall_check else 'N'

        #         institut_seni_indonesia_yogyakarta_check = st.checkbox('Institut Seni Indonesia Yogyakarta', value=False)
        #         institut_seni_indonesia_yogyakarta = 'Y' if institut_seni_indonesia_yogyakarta_check else 'N'

        #         sekolah_tinggi_teknologi_adisutjipto_check = st.checkbox('Sekolah Tinggi Teknologi Adisutjipto', value=False)
        #         sekolah_tinggi_teknologi_adisutjipto = 'Y' if sekolah_tinggi_teknologi_adisutjipto_check else 'N'
        
        #     with col2:
        #         universitas_jenderal_achmad_yani_check = st.checkbox('Universitas Jenderal Achmad Yani', value=False)
        #         universitas_jenderal_achmad_yani = 'Y' if universitas_jenderal_achmad_yani_check else 'N'

        #         universitas_tidar_check = st.checkbox('Universitas Tidar', value=False)
        #         universitas_tidar = 'Y' if universitas_tidar_check else 'N'
            
        #         jogja_city_mall_check = st.checkbox('Jogja City Mall', value=False)
        #         jogja_city_mall = 'Y' if jogja_city_mall_check else 'N'

        #         ambarrukmo_plaza_check = st.checkbox('Ambarrukmo Plaza', value=False)
        #         ambarrukmo_plaza = 'Y' if ambarrukmo_plaza_check else 'N'
                
        #         universitas_muhammadiyah_yogyakarta_check = st.checkbox('Universitas Muhammadiyah Yogyakarta', value=False)
        #         universitas_muhammadiyah_yogyakarta = 'Y' if universitas_muhammadiyah_yogyakarta_check else 'N'

        #         monumen_jogja_kembali_check = st.checkbox('Monumen Jogja Kembali', value=False)
        #         monumen_jogja_kembali = 'Y' if monumen_jogja_kembali_check else 'N'

        #         stasiun_yogyakarta_check = st.checkbox('Stasiun Yogyakarta', value=False)
        #         stasiun_yogyakarta = 'Y' if stasiun_yogyakarta_check else 'N'

        #         universitas_teknologi_yogyakarta_check = st.checkbox('Universitas Teknologi Yogyakarta', value=False)
        #         universitas_teknologi_yogyakarta = 'Y' if universitas_teknologi_yogyakarta_check else 'N'

        #         universitas_negeri_yogyakarta_check = st.checkbox('Universitas Negeri Yogyakarta', value=False)
        #         universitas_negeri_yogyakarta = 'Y' if universitas_negeri_yogyakarta_check else 'N'

        #         sman_1_teladan_yogyakarta_check = st.checkbox('Sman 1 Teladan Yogyakarta', value=False)
        #         sman_1_teladan_yogyakarta = 'Y' if sman_1_teladan_yogyakarta_check else 'N'

        #         rs_panti_nugroho_check = st.checkbox('RS Panti Nugroho', value=False)
        #         rs_panti_nugroho = 'Y' if rs_panti_nugroho_check else 'N'

        #         galeria_mall_check = st.checkbox('Galeria Mall', value=False)
        #         galeria_mall = 'Y' if galeria_mall_check else 'N'

        #         rumah_sakit_jogja_international_hospital_check = st.checkbox('Rumah Sakit Jogja International Hospital', value=False)
        #         rumah_sakit_jogja_international_hospital = 'Y' if rumah_sakit_jogja_international_hospital_check else 'N'

        #         universitas_kristen_duta_wacana_check = st.checkbox('Universitas Kristen Duta Wacana', value=False)
        #         universitas_kristen_duta_wacana = 'Y' if universitas_kristen_duta_wacana_check else 'N'

        #     with col3:
        #         stasiun_tugu_check = st.checkbox('Stasiun Tugu', value=False)
        #         stasiun_tugu = 'Y' if stasiun_tugu_check else 'N'

        #         institut_sains_dan_teknologi_akprind_check = st.checkbox('Institut Sains dan Teknologi Akprind', value=False)
        #         institut_sains_dan_teknologi_akprind = 'Y' if institut_sains_dan_teknologi_akprind_check else 'N'

        #         tugu_yogyakarta_check = st.checkbox('Tugu Yogyakarta', value=False)
        #         tugu_yogyakarta = 'Y' if tugu_yogyakarta_check else 'N'

        #         universitas_aisyiyah_check = st.checkbox('Universitas Aisyiyah', value=False)
        #         universitas_aisyiyah = 'Y' if universitas_aisyiyah_check else 'N'

        #         universitas_atmajaya_yogyakarta_check = st.checkbox('Universitas Atma Jaya Yogyakarta', value=False)
        #         universitas_atmajaya_yogyakarta = 'Y' if universitas_atmajaya_yogyakarta_check else 'N'

        #         rs_sardjito_yogyakarta_check = st.checkbox('RS Sardjito Yogyakarta', value=False)
        #         rs_sardjito_yogyakarta = 'Y' if rs_sardjito_yogyakarta_check else 'N'

        #         sman_6_yogyakarta_check = st.checkbox('Sman 6 Yogyakarta', value=False)
        #         sman_6_yogyakarta = 'Y' if sman_6_yogyakarta_check else 'N'

        #         stmik_amikom_yogyakarta_check = st.checkbox('STMIK Amikom Yogyakarta', value=False)
        #         stmik_amikom_yogyakarta = 'Y' if stmik_amikom_yogyakarta_check else 'N'

        #         universitas_islam_negeri_sunan_kalijaga_check = st.checkbox('Universitas Islam Negeri Sunan Kalijaga', value=False)
        #         universitas_islam_negeri_sunan_kalijaga = 'Y' if universitas_islam_negeri_sunan_kalijaga_check else 'N'

        #         gereja_saint_francis_xaverius_yogyakarta_check = st.checkbox('Gereja Saint Francius Xaverius Yogyakarta', value=False)
        #         gereja_saint_francis_xaverius_yogyakarta = 'Y' if gereja_saint_francis_xaverius_yogyakarta_check else 'N'

        #         sahid_j_walk_check = st.checkbox('Sahid J-Walk', value=False)
        #         sahid_j_walk = 'Y' if sahid_j_walk_check else 'N'

        #         rumah_sakit_panti_rapih_check = st.checkbox('Rumah Sakit Panti Rapih', value=False)
        #         rumah_sakit_panti_rapih = 'Y' if rumah_sakit_panti_rapih_check else 'N'

        #         universitas_sanata_dharma_yogyakarta_check = st.checkbox('Universitas Sanata Dharma Yogyakarta', value=False)
        #         universitas_sanata_dharma_yogyakarta = 'Y' if universitas_sanata_dharma_yogyakarta_check else 'N'

        #         sman_3_yogyakarta_check = st.checkbox('Sman 3 Yogyakarta', value=False)
        #         sman_3_yogyakarta = 'Y' if sman_3_yogyakarta_check else 'N'
        start_column = 'malioboro'
        end_column = 'sman_3_yogyakarta'
        filtered_columns = selected_city.columns[selected_city.columns.get_loc(start_column):selected_city.columns.get_loc(end_column) + 1]
        fitur_2_list = {}
        nama_deskriptif = {
        'malioboro': 'Malioboro',
        'masjid_jogokariyan': 'Masjid Jogokariyan',
        'malioboro_mall': 'Malioboro Mall',
        'universitas_ahmad_dahlan' : 'Universitas Ahmad Dahlan',	
        'terminal_giwangan' : 'Terminal Giwangan',	
        'universitas_gadjah_mada' : 'Universitas Gadjah Mada',
        'universitas_sarjanawiyata_tamansiswa':'Univesitas Sarjanawiyata Tamansiswa',
        'universitas_pembangunan_nasional_veteran_yogyakarta' : 'Universitas Pembangunan Nasional Veteran Yogyakarta',
        'lippo_plaza_jogja' : 'Lippo Plaza Jogja',
        'masjid_gedhe_kauman' : 'Masjid Gedhe Kauman',	
        'universitas_islam_indonesia' : 'Universitas Islam Indonesia',
        'sleman_city_hall' : 'Sleman City Hall',
        'institut_seni_indonesia_yogyakarta' : 'Institut Seni Indonesia Yogyakarta',
        'sekolah_tinggi_teknologi_adisutjipto' : 'Sekolah Tinggi Teknologi Adisutjipto',
        'universitas_jenderal_achmad_yani' : 'Universitas Jendaral Achmad Yani',
        'universitas_tidar' : 'Universitas Tidar',
        'jogja_city_mall' : 'Jogja City Mall',
        'ambarrukmo_plaza' : 'Amabarukmo Plaza',
        'universitas_muhammadiyah_yogyakarta' : 'Universitas Muhammadiyah Yogyakarta',
        'monumen_jogja_kembali' : 'Monumen Jogja Kembali',
        'stasiun_yogyakarta' : 'Stasiun Yogyakarta',
        'universitas_teknologi_yogyakarta' : 'Universitas Teknologi Yogyakarta',
        'universitas_negeri_yogyakarta' : 'Universitas Teknologi Yogyakarta',
        'sman_1_teladan_yogyakarta' : 'SMAN 1 Teladan Yogyakarta',
        'rs_panti_nugroho' : 'Rumah Sakit Panti Nugroho',
        'galeria_mall' : 'Galeria Mall',
        'rumah_sakit_jogja_international_hospital' : 'Rumah Sakit Jogja International Hospital',	
        'universitas_kristen_duta_wacana' : 'Universitas Kristen Duta Wacana',
        'stasiun_tugu' : 'Stasiun Tugu',
        'institut_sains_dan_teknologi_akprind' : 'Institut Sains dan Teknologi Akprind',	
        'tugu_yogyakarta' : 'Tugu Yogyakarta',
        'universitas_aisyiyah' : 'Univesitas Aisyiyah',
        'universitas_atmajaya_yogyakarta' : 'Universitas Atmajaya Yogyakarta',
        'rs_sardjito_yogyakarta' : 'Rumah Sakit Sardjito Yogyakarta',
        'sman_6_yogyakarta' : 'SMAN 6 Yogyakarta',
        'stmik_amikom_yogyakarta' : 'Stmik Amikom Yogyakarta',
        'universitas_islam_negeri_sunan_kalijaga' : 'Universitas Islam Negeri Sunan Kalijaga',
        'gereja_saint_francis_xaverius_yogyakarta' : 'Gereja Saint Francis Xaverius Yogyakarta',
        'sahid_j_walk' : 'Sahid J Walk',
        'rumah_sakit_panti_rapih' : 'Rumah Sakit Panti Rapih',
        'universitas_sanata_dharma_yogyakarta' : 'Universitas Sanata Dharma Yogyakarta',
        'sman_3_yogyakarta' : 'SMA 3 Yogyakarta'}
        with st.expander('Sekitar Lokasi'):
            num_columns = 3  # Jumlah kolom yang diinginkan
            cols = st.columns(num_columns)
            i = 0
            for i, col in enumerate(filtered_columns):
                nama = nama_deskriptif.get(col, col)
                if 'Y' in selected_city[col].unique():
                    fitur_2_list[col] = cols[i % num_columns].checkbox(nama, value=False, key=f"{col}_{i}")
                    i += 1                
                else:
                    fitur_2_list[col] = 'N'
        if st.button('Submit'):
            st.write('')
            st.write('')
            if any(value <= 0 for value in [kamar_tidur, bangunan, lahan, kamar_mandi]):
                if all(value == 0 for value in [kamar_tidur, bangunan, lahan, kamar_mandi]):
                    st.subheader('Input Random')
                    kamar_tidur = random.randint(1, 50)
                    bangunan = random.randint(1, 1000)
                    lahan = random.randint(1, 1500)
                    kamar_mandi = random.randint(1, 50)
                    latitude = selected_city['latitude'].astype(float).values[0]
                    longitude = selected_city['longitude'].astype(float).values[0]
                    mapping = {'Y': 1, 'N': 0}
                    fitur_1 = [
                        mapping[sistem_alarm], mapping[gym], mapping[internet_broadband_wifi],
                        mapping[tv_kabel], mapping[pemanas_ruangan],mapping[pendingin_ruangan],mapping[halaman_terbuka],
                        mapping[air_panas], mapping[telepon], mapping[televisi],
                        mapping[kitchen_set], mapping[garasi], mapping[secure_parking],
                        mapping[kolam_renang], mapping[lapangan_tenis], mapping[balkon],
                        mapping[dek], mapping[area_hiburan_outdoor], mapping[pagar_penuh],
                        mapping[taman],mapping[keamanan_24_jam],mapping[taman_bermain_anak]
                    ]
                    for col, value in fitur_2_list.items():
                        if value == 'N':
                            fitur_2_list[col] = 0
                    fitur_2 = list(fitur_2_list.values())
                    # fitur_2 = [
                    #     mapping[malioboro],mapping[masjid_jogokariyan],mapping[malioboro_mall],mapping[universitas_ahmad_dahlan],
                    #     mapping[terminal_giwangan],mapping[universitas_gadjah_mada],mapping[universitas_sarjanawiyata_tamansiswa],mapping[universitas_pembangunan_nasional_veteran_yogyakarta],	
                    #     mapping[lippo_plaza_jogja],mapping[masjid_gedhe_kauman],mapping[sleman_city_hall],mapping[institut_seni_indonesia_yogyakarta],
                    #     mapping[sekolah_tinggi_teknologi_adisutjipto],mapping[universitas_jenderal_achmad_yani],mapping[universitas_tidar],mapping[jogja_city_mall],
                    #     mapping[ambarrukmo_plaza],mapping[universitas_muhammadiyah_yogyakarta],mapping[monumen_jogja_kembali],mapping[stasiun_yogyakarta],mapping[universitas_islam_indonesia],	
                    #     mapping[universitas_teknologi_yogyakarta],mapping[universitas_negeri_yogyakarta],mapping[sman_1_teladan_yogyakarta],mapping[rs_panti_nugroho],mapping[galeria_mall],mapping[rumah_sakit_jogja_international_hospital],	
                    #     mapping[universitas_kristen_duta_wacana],mapping[stasiun_tugu],mapping[institut_sains_dan_teknologi_akprind],mapping[tugu_yogyakarta],mapping[universitas_aisyiyah],mapping[universitas_atmajaya_yogyakarta],
                    #     mapping[rs_sardjito_yogyakarta],mapping[sman_6_yogyakarta],mapping[stmik_amikom_yogyakarta],mapping[universitas_islam_negeri_sunan_kalijaga],mapping[gereja_saint_francis_xaverius_yogyakarta],
                    #     mapping[sahid_j_walk],mapping[rumah_sakit_panti_rapih],mapping[universitas_sanata_dharma_yogyakarta],mapping[sman_3_yogyakarta]]	
                    col1,col2 = st.columns(2)
                    with col1:
                        st.warning(f'Kamar Tidur: {kamar_tidur}')
                        st.warning(f'Bangunan: {bangunan}')
                    with col2:
                        st.warning(f'Lahan: {lahan}')
                        st.warning(f'Kamar Mandi: {kamar_mandi}')
                else:
                    st.warning('Masukkan angka yang benar untuk kamar tidur, bangunan, lahan, dan kamar mandi.')
                    st.write('')
                    st.write('')
                    st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")
                    return
            if model_prediksi is not None:
                mapping = {'Y': 1, 'N': 0}
                fitur_1 = [
                    mapping[sistem_alarm], mapping[gym], mapping[internet_broadband_wifi],
                    mapping[tv_kabel], mapping[pemanas_ruangan],mapping[pendingin_ruangan],mapping[halaman_terbuka],
                    mapping[air_panas], mapping[telepon], mapping[televisi],
                    mapping[kitchen_set], mapping[garasi], mapping[secure_parking],
                    mapping[kolam_renang], mapping[lapangan_tenis], mapping[balkon],
                    mapping[dek], mapping[area_hiburan_outdoor], mapping[pagar_penuh],
                    mapping[taman],mapping[keamanan_24_jam],mapping[taman_bermain_anak]
                ]
                for col, value in fitur_2_list.items():
                    if value == 'N':
                        fitur_2_list[col] = 0
                fitur_2 = list(fitur_2_list.values())
                # fitur_2 = [
                #     mapping[malioboro],mapping[masjid_jogokariyan],mapping[malioboro_mall],mapping[universitas_ahmad_dahlan],
                #     mapping[terminal_giwangan],mapping[universitas_gadjah_mada],mapping[universitas_sarjanawiyata_tamansiswa],mapping[universitas_pembangunan_nasional_veteran_yogyakarta],	
                #     mapping[lippo_plaza_jogja],mapping[masjid_gedhe_kauman],mapping[sleman_city_hall],mapping[institut_seni_indonesia_yogyakarta],
                #     mapping[sekolah_tinggi_teknologi_adisutjipto],mapping[universitas_jenderal_achmad_yani],mapping[universitas_tidar],mapping[jogja_city_mall],
                #     mapping[ambarrukmo_plaza],mapping[universitas_muhammadiyah_yogyakarta],mapping[monumen_jogja_kembali],mapping[stasiun_yogyakarta],mapping[universitas_islam_indonesia],	
                #     mapping[universitas_teknologi_yogyakarta],mapping[universitas_negeri_yogyakarta],mapping[sman_1_teladan_yogyakarta],mapping[rs_panti_nugroho],mapping[galeria_mall],mapping[rumah_sakit_jogja_international_hospital],	
                #     mapping[universitas_kristen_duta_wacana],mapping[stasiun_tugu],mapping[institut_sains_dan_teknologi_akprind],mapping[tugu_yogyakarta],mapping[universitas_aisyiyah],mapping[universitas_atmajaya_yogyakarta],
                #     mapping[rs_sardjito_yogyakarta],mapping[sman_6_yogyakarta],mapping[stmik_amikom_yogyakarta],mapping[universitas_islam_negeri_sunan_kalijaga],mapping[gereja_saint_francis_xaverius_yogyakarta],
                #     mapping[sahid_j_walk],mapping[rumah_sakit_panti_rapih],mapping[universitas_sanata_dharma_yogyakarta],mapping[sman_3_yogyakarta]]	
                
                features = [[kamar_tidur, bangunan, lahan, kamar_mandi,latitude,longitude ] + fitur_1 + fitur_2]
                predict_house1 = model_prediksi.predict(features)
                prediction = np.expm1(predict_house1)
            st.write('')
            st.write('')
            st.subheader('Prediksi Harga Rumah : ')
            prediction_value = float(prediction[0])
            st.write(f'Rp. {format_price(prediction_value,0)}')
            st.success('ini hanyalah prediksi dan tidak 100% tepat tergantung faktor lainya dan sesungguhnya prediksi yang tepat hanya milik tuhan semata ingatlah itu ki sanak')
            st.write('')
            st.write('')
    st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")

if __name__ == '__main__':
    predict()
