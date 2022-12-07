import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# load save model
model_fraud = pickle.load(open('model_Prediksi_SMS.sav','rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("fitur_baru_tf-idf.sav", "rb"))))


# judul halaman
st.title('------------------------------------------------')
st.title('Aplikasi Prediksi Jenis SMS')
st.title('------------------------------------------------')
clean_teks = st.text_input('Silahkan masukan Teks SMS yang di dapat')

fraud_detection = ''

if st.button('Hasil Deteksi'):
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))
    
    if (predict_fraud == 0):
        fraud_detection = 'SMS Normal'
    elif (predict_fraud == 1):
        fraud_detection = 'SMS Penipuan'
    else :
        fraud_detection = 'SMS Promo'

st.success(fraud_detection)
st.title('------------------------------------------------')
st.title('Alif Fajar Panjalu (191351110)')

