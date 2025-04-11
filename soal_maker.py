import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time

from process import clear_background
clear_background()
soal_added = False
with st.form(key="soal-maker-form"):
    st.header("Pembuat Soal")
    st.subheader("List soal")
    
    # Check excel file, if not exist, create one
    cwd = os.getcwd()
    if not os.path.exists(os.path.join(cwd, "soal.xlsx")):
        df = pd.DataFrame(columns=["Soal","Type","Jawaban"])
        df.to_excel(os.path.join(cwd, "soal.xlsx"), index=False)
    else:
        df = pd.read_excel(os.path.join(cwd, "soal.xlsx"))
        
    #Display df
    st.write(df, use_container_width=True)
    # Get input from user
    
    st.text_input("Soal", key='soal')
    
    type_soal = st.selectbox("Type Soal", ["Matematika", "Pemrograman"])
    
    st.text_input("Jawaban", key='jawaban')
    
    def clear_form():
        st.session_state.soal = ""
        st.session_state.jawaban = ""
    
    if soal_added:
        st.success("Soal berhasil ditambahkan")
        soal_added = False
    
    # st.form_submit_button("Add Soal")
    f1,f2 = st.columns([1,1])
    
    with f1 :
        clear = st.form_submit_button("Clear Form", on_click=clear_form)
    with f2:
        add = st.form_submit_button("Add Soal")
    if add:
        if st.session_state.soal == "" or st.session_state.jawaban  == "":
            st.warning("Soal atau Jawaban tidak boleh kosong")
            
        df = pd.concat([df, pd.DataFrame({"Soal":[st.session_state.soal], "Type":[type_soal], "Jawaban":[st.session_state.jawaban]})], ignore_index=True)
        # 
        df.to_excel(os.path.join(cwd, "soal.xlsx"), index=False)
        soal_added = True
        #clear soal & jawaban
        st.rerun()