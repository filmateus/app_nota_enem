# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:31:28 2022
@author: p.santosh.dandale
"""

import pandas as pd
import streamlit as st
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")
from PIL import Image

# import os
# import joblib


pickle_in = open("Naive Bayes_classifier.pkl","rb")
classifier = pickle.load(pickle_in)

# classifier = joblib.load("alg.joblib")

def predict_type_school(NU_NOTA_CH, NU_NOTA_CN, NU_NOTA_MT, NU_NOTA_LC, NU_NOTA_REDACAO):
    prediction = classifier.predict([[NU_NOTA_CH, NU_NOTA_CN, NU_NOTA_MT, NU_NOTA_LC, NU_NOTA_REDACAO]])
    if prediction == 3:
        prediction = 'Escola Privada'
    else:
        prediction = 'Escola Pública'
    print(prediction)
    return prediction 

def Input_Output():
    st.title("Tipo de Escola baseado na nota do ENEM")
    st.image("https://conteudo.imguol.com.br/c/noticias/b6/2020/12/08/ilustra-enem-seriado-1607450891464_v2_900x506.jpg.webp", width=600)
    
    st.markdown("You are using Streamlit...",unsafe_allow_html=True)
    NU_NOTA_CH  = st.text_input("Digite a nota de Humanidades" , "")
    NU_NOTA_CN  = st.text_input("Digite a nota de Naturezas" , "")
    NU_NOTA_MT  = st.text_input("Digite a nota de Matemática" , "")
    NU_NOTA_LC  = st.text_input("Digite a nota de Linguaguem" , "")
    NU_NOTA_REDACAO  = st.text_input("Digite a nota de Redação" , "")


    if NU_NOTA_CH.strip() and NU_NOTA_CN.strip() and NU_NOTA_MT.strip() and NU_NOTA_LC.strip() and NU_NOTA_REDACAO.strip():
        NU_NOTA_CH = float(NU_NOTA_CH)
        NU_NOTA_CN = float(NU_NOTA_CN)
        NU_NOTA_MT = float(NU_NOTA_MT)
        NU_NOTA_LC = float(NU_NOTA_LC)
        NU_NOTA_REDACAO = float(NU_NOTA_REDACAO)
        result = predict_type_school(NU_NOTA_CH, NU_NOTA_CN, NU_NOTA_MT, NU_NOTA_LC, NU_NOTA_REDACAO)

    if st.button("Enter"):
        st.success('As notas indicam que a origem de {}'.format(result))

if __name__ ==  '__main__':
    Input_Output()
