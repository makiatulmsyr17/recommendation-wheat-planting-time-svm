import pickle
import streamlit as st
import pandas as pd

# Load model dari file model_svm.pkl
with open('D:\\1.Data Science\\project\\recommendation-wheat-planting-time-svm\\recommendation-wheat-planting-time-svm\\models\\model_svm.pkl', 'rb') as file:
    model = pickle.load(file)

# Aplikasi Streamlit
st.title('Rekomendasi Bagus Atau Tidaknya Cuaca untuk Menanam Gandum')

# Input dari pengguna sesuai urutan yang benar
Iws = st.number_input('Masukkan nilai untuk Iws:')
Ir = st.number_input('Masukkan nilai untuk Ir:')
pm25 = st.number_input('Masukkan nilai untuk pm2.5:')
PRES = st.number_input('Masukkan nilai untuk PRES:')
cbwd = st.number_input('Masukkan nilai untuk cbwd:')
DEWP = st.number_input('Masukkan nilai untuk DEWP:')
delta_Temperature = st.number_input('Masukkan nilai untuk delta_Temperature:')
delta_PRESS = st.number_input('Masukkan nilai untuk delta_PRESS:')
Ir_category = st.number_input('Masukkan nilai untuk Ir_category:')
pm25_category = st.number_input('Masukkan nilai untuk pm2.5_category:')

if st.button('Predict'):
    # Buat DataFrame dari input pengguna sesuai dengan urutan fitur saat pelatihan
    input_data = pd.DataFrame({
        'Iws': [Iws],
        'Ir': [Ir],
        'pm2.5': [pm25],
        'PRES': [PRES],
        'cbwd': [cbwd],
        'DEWP': [DEWP],
        'delta_Temperature': [delta_Temperature],
        'delta_PRESS': [delta_PRESS],
        'Ir_category': [Ir_category],
        'pm2.5_category': [pm25_category]
    })

    # Prediksi menggunakan model yang sudah diload
    prediction = model.predict(input_data)
    
    # Tampilkan hasil prediksi
    if prediction[0] == 1.0:
        st.write('Hasil Prediksi: Cuaca saat ini **bagus** untuk menanam gandum.')
    elif prediction[0] == 0.0:
        st.write('Hasil Prediksi: Cuaca saat ini **tidak cocok** untuk menanam gandum.')
    else:
        st.write('Hasil Prediksi: Nilai prediksi tidak valid.')
