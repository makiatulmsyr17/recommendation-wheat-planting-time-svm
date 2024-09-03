import pickle
import streamlit as st
import pandas as pd

# Load model dari file model_svm.pkl
with open('./models\model_svm.pkl', 'rb') as file:
    model = pickle.load(file)

# Aplikasi Streamlit
st.title('Gandum Grow: Cuaca Ideal untuk Penanaman')

# CSS untuk membuat desain hitam putih dan tombol hitam
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #000000;
        color: #FFFFFF;
        border-radius: 5px;
        border: 1px solid #FFFFFF;
    }
    .stButton>button:hover {
        background-color: #333333;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Fungsi untuk reset input
def reset_input():
    st.session_state['Iws'] = 0.0
    st.session_state['Ir'] = 0.0
    st.session_state['pm25'] = 0.0
    st.session_state['PRES'] = 0.0
    st.session_state['cbwd'] = 0.0
    st.session_state['DEWP'] = 0.0
    st.session_state['delta_Temperature'] = 0.0
    st.session_state['delta_PRESS'] = 0.0
    st.session_state['Ir_category'] = 0.0
    st.session_state['pm2.5_category'] = 0.0

# Tombol Reset ditekan
if 'reset' not in st.session_state:
    st.session_state['reset'] = False

if st.button('Reset'):
    reset_input()
    st.session_state['reset'] = True

# Input dari pengguna sesuai urutan yang benar
Iws = st.number_input('Masukkan nilai untuk Iws:', value=st.session_state.get('Iws', 0.0), key='Iws')
Ir = st.number_input('Masukkan nilai untuk Ir:', value=st.session_state.get('Ir', 0.0), key='Ir')
pm25 = st.number_input('Masukkan nilai untuk pm2.5:', value=st.session_state.get('pm25', 0.0), key='pm25')
PRES = st.number_input('Masukkan nilai untuk PRES:', value=st.session_state.get('PRES', 0.0), key='PRES')
cbwd = st.number_input('Masukkan nilai untuk cbwd:', value=st.session_state.get('cbwd', 0.0), key='cbwd')
DEWP = st.number_input('Masukkan nilai untuk DEWP:', value=st.session_state.get('DEWP', 0.0), key='DEWP')
delta_Temperature = st.number_input('Masukkan nilai untuk delta_Temperature:', value=st.session_state.get('delta_Temperature', 0.0), key='delta_Temperature')
delta_PRESS = st.number_input('Masukkan nilai untuk delta_PRESS:', value=st.session_state.get('delta_PRESS', 0.0), key='delta_PRESS')
Ir_category = st.number_input('Masukkan nilai untuk Ir_category:', value=st.session_state.get('Ir_category', 0.0), key='Ir_category')
pm25_category = st.number_input('Masukkan nilai untuk pm2.5_category:', value=st.session_state.get('pm2.5_category', 0.0), key='pm2.5_category')

# Tombol Predict
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
