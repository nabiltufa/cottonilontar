import pickle
import streamlit as st

model = pickle.load(open('kernel_rbf.sav', 'rb'))

st.title('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii di Desa Lontar')

tahun = st.text_input('Input Tahun Prediksi')
bulan = st.text_input('Input Bulan Prediksi')
tanggal = st.text_input('Input Tanggal Prediksi')
arus = st.number_input('Input Arus Prediksi')
salinitas = st.number_input('Input Salinitas Prediksi')
suhu = st.text_input('Input Suhu Prediksi')
modal = st.text_input('Input Modal Prediksi')

predict = ''

if st.button ('Prediksi'):
    predict = model.predict(
        [[tahun,bulan,tanggal,arus,salinitas,suhu,modal]]
    )
    st.write('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii : ', predict)
