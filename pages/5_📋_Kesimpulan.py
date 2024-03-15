import streamlit as st


st.set_page_config(page_title = "Kesimpulan")


st.markdown("<div style='text-align: center;'><h2>Kesimpulan</h2></div>", unsafe_allow_html=True)
st.divider()
st.write("""Harga rumah juga ditentukan dengan beberapa faktor lainya selain luas lahan,luas bangunan,jumlah kamar tidur,jumlah kamar mandi,lokasi dan fasilitas
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
            pada tanggal 25 Februari 2024 di website [lamudi](https://www.lamudi.co.id/) yang memperoleh kurang lebih 1200 data
            dengan mengurutkan dari yang terbaru sampai yang terlama dan scrapping dari page 1 sampai 50 dengan filter rumah yang dijual""")
st.write("""
                untuk pengembangangan : \n 
            1. Gunakan dataset yang mendetail seperti kelengkapan surat,dekat dengan tempat wisata,akses ke jalan raya,fasilitas,dan sebagainya, serta alamat yang lebih banyak agar bisa memprediksi di sebuah alamat dari lokasi yang dipilih 
            2. Untuk model prediksi rumah masih perlu banyak pengembangan""")
