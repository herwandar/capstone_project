import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(page_title = "Model")


st.markdown("<div style='text-align: center;'><h2>Model Prediksi</h2></div>", unsafe_allow_html=True)
tab1,tab2, = st.tabs(['Sebelum Skew','Setelah Skew'])
with tab1:
    st.subheader('Linear Regression')
    linear =  pd.DataFrame({
    'Mean Absolute Percentage Error': [0.4288361557580387],
    'Root Mean Squared Error': [1562907118.3936405],
    'Mean Squared Error ln': [2.4426786607255127e+18],
    'R-squared ln': [0.490146578393145],
    'Mean Absolute Error ln': [724055790.8697226]})
    st.table(linear)
    st.write('')
    st.write('')
    gambar1 = 'gambar/linear_sebelum_skew.png'
    Image1 = Image.open(gambar1)
    st.image(Image1,use_column_width=True)
    st.write('')
    st.write('')
    st.subheader('Random Forest Regressor')
    random =  pd.DataFrame({
    'Mean Absolute Percentage Error': [0.2760609737971662],
    'Root Mean Squared Error': [1305963905.3031328],
    'Mean Squared Error rf': [1.7055417219546102e+18],
    'R-squared rf': [0.6440070908166333],
    'Mean Absolute Error rf': [489956199.67115664]})
    st.table(random)
    st.write('')
    st.write('')
    gambar2 = ('gambar/random_forest_sebelum_skew.png')
    Image2 = Image.open(gambar2)
    st.image(Image2,use_column_width=True)
    st.write('')
    st.write('')
    st.subheader('Gradient Boosting Regressor')
    gradient = pd.DataFrame({
    'Mean Absolute Percentage Error': [0.33256225425220554],
    'Root Mean Squared Error': [1442622423.9601924],
    'Mean Squared Error': [2.081159458112781e+18],
    'R-squared': [0.5656054610502428],
    'Mean Absolute Error': [599577581.2188264]})
    st.table(gradient)
    st.write('')
    st.write('')
    gambar3 = ('gambar/gradirnt_sebelum_skew.png')
    Image3 = Image.open(gambar3)
    st.image(Image3,use_column_width=True)
    st.write("""Berhubung nilai mean squared error dan mean absolute extreme maka saya cari cara lainya untuk mengatasi nilai extreme""")
    st.write('')
    st.write('')
    st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")
with tab2:
    st.subheader('Perbedaan Sebelum Dan Sesudah di Skew')
    gambar4 = ('gambar/harga_tans.png')
    image1 = Image.open(gambar4)
    st.image(image1,use_column_width=True)
    gambar5 = ('gambar/harga_box_trans.png')
    image2 = Image.open(gambar5)
    st.image(image2,use_column_width=True)
    gambar6 = ('gambar/kamar_mandi_setelah_skew.png')
    image3 = Image.open(gambar6)
    st.image(image3,use_column_width=True)
    gambar7 = ('gambar/kamar_mandi_box.png')
    image4 = Image.open(gambar7)
    st.image(image4,use_column_width=True)
    gambar8 = ('gambar/kamar_tidur_skew.png')
    image5 = Image.open(gambar8)
    st.image(image5,use_column_width=True)
    gambar9 = ('gambar/kamar_tidur_box.png')
    image6 = Image.open(gambar9)
    st.image(image6,use_column_width=True)
    gambar10 = ('gambar/bangunan_setelah_skew.png')
    image7 = Image.open(gambar10)
    st.image(image7,use_column_width=True)
    gambar11 = ('gambar/bangunan_box.png')
    image8 = Image.open(gambar11)
    st.image(image8,use_column_width=True)
    gambar12 = ('gambar/lahan_setelah_skew.png')
    image9 = Image.open(gambar12)
    st.image(image9,use_column_width=True)
    gambar13 = ('gambar/lahan_box.png')
    image10 = Image.open(gambar13)
    st.image(image10,use_column_width=True)
    st.write('terlihat ada perubahan setelah melakukan skewness bisa dilihat dari visualisasi di atas')
    st.write('')
    st.write('')
    st.subheader('Linear Regression')
    ln = pd.DataFrame({'Mean Absolute Percentage Error': [0.014152548839752402],
    'Root Mean Squared Error': [0.40644495473455383],
    'Mean Squared Error': [0.1651975012291735],
    'R-squared': [0.7364679318444263],
    'Mean Absolute Error': [0.298043287378819]})
    st.table(ln)
    st.write('')
    st.write('')
    gambar14 = ('gambar/linear_setekah_skew.png')
    image11 = Image.open(gambar14)
    st.image(image11,use_column_width=True)
    st.write('')
    st.write('')
    st.subheader('Random Forest Regressor')
    rf = pd.DataFrame({'Mean Absolute Percentage Error': [0.010454637593238588],
    'Root Mean Squared Error': [0.33441212880804594],
    'Mean Squared Error': [0.11183147189392911],
    'R-squared': [0.8216003338197919],
    'Mean Absolute Error': [0.2199463540745569]})
    st.table(rf)
    st.write('')
    st.write('')
    gambar15 = ('gambar/random_forest_setelah_skew.png')
    image12 = Image.open(gambar15)
    st.image(image12,use_column_width=True)
    st.write('')
    st.write('')
    st.subheader('Gradient Boosting Regressor')
    gb = pd.DataFrame({'Mean Absolute Percentage Error': [0.012519011646905281],
    'Root Mean Squared Error': [0.37499362611656667],
    'Mean Squared Error': [0.1406202196280514],
    'R-squared': [0.7756749525426414],
    'Mean Absolute Error': [0.2643576780176472]})
    st.table(gb)
    st.write('')
    st.write('')
    gambar16 = ('gambar/gradirnt_setelah_skew.png')
    image13 = Image.open(gambar16)
    st.image(image13,use_column_width=True)
    st.write("""setelah melakukan skewnees terlihat skor dari MAE,MSE,MAPE,RMSE dan R squared normal,
             berhubung nilai dari random forest paling bagus maka putuskan menggunakan random forest""")
    st.write('')
    st.write('')
    st.subheader('Tuning Random Forest Regressor')
    data_best_model = pd.DataFrame({ 'Mean Absolute Percentage Error rf': [0.010361054003972876],
    'Root Mean Squared Error rf': [0.3343649302970225],
    'Mean Squared Error rf': [0.11179990661253274],
    'R-squared rf': [0.821650688479072],
    'Mean Absolute Error rf': [0.21792007006777436]})
    st.table(data_best_model)
    st.write('')
    st.write('')
    param_best = pd.DataFrame({'max_depth': [20],
    'max_features': ['auto'],
    'min_samples_leaf': [1],
    'min_samples_split': [2],
    'n_estimators': [150]})
    st.table(param_best)
    st.write('')
    st.write('')
    gambar17 = ('gambar/random_forest_tuning.png')
    image14 = Image.open(gambar17)
    st.image(image14,use_column_width=True)
    st.write("""Tuning dilakuakan dengan mencari best_params dengan GridCV,
             nilai setelah tuning ada peningkatan""")
    st.write('')
    st.write('')
    gambar18 = ('gambar/residual.png')
    image15 = Image.open(gambar18)
    st.image(image15,use_column_width=True)
    st.write('Residu baik jika acak')
    st.write('')
    st.write('')
    gambar19 = ('gambar/top 10.png')
    image16 = Image.open(gambar19)
    st.image(image16,use_column_width=True)
    st.write('Bangunan memiliki pengaruh besar diikuti lahan dalam model random forest')
    st.write('')
    st.write('')
    st.error("""Data Diambil Dengan Metode Web Scrapping Di Website [Lamudi](https://www.lamudi.co.id/)""")