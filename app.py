import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import random
import time
import os
from connector import *

from process import clear_background, clearfirstOption, writeQuestion, writeDescription

clear_background()
list_soal_Matematika = []
list_soal_Pemrograman = []

#Max Soal = 30 (20 matematika + 10 pemrograman)
allSoal = []
allAnswer = []
rated = {}
st.session_state.answer = []


with st.form(key='Soal-quiz',clear_on_submit=False):
    st.header("Soal-soal pemrograman C++")
    st.subheader("List soal")
    
    # Check excel file, if not exist, call github user
    cwd = os.getcwd()
    if not os.path.exists(os.path.join(cwd, "soal.xlsx")):
        # df = pd.DataFrame(columns=["Soal","Type","Jawaban"])
        # df.to_excel(os.path.join(cwd, "soal.xlsx"), index=False)
        print('soal.xlsx not found')
        sys.exit(1)
    else:
        df = pd.read_excel(os.path.join(cwd, "soal.xlsx"))
        
    #Random soal generator
    def randSoalGenerator(type : str) -> list:
        """
        Generating random soal based on their type
        """
        # random.seed(0)
        soalGenerated = []
        tempDf = df[df["Type"] == type]
        choices = [i for i in range(len(tempDf))]
        Soalsize = 20 if type == "Matematika" else 10
        while(Soalsize > 0):
            # print("Choices", choices)
            rand = random.choice(choices)
            choices.remove(rand)
            # st.write(rand)
            #Check if the soal have <kode>
            soalStr = tempDf.iloc[rand]["Soal"]
            jwbStr = tempDf.iloc[rand]["Jawaban"]
            if soalStr.find("<kode>") != -1:
                numCode = int(soalStr.split("<kode>")[0])
                #Make sure the answer is the kode too
                try: int(jwbStr)
                except: continue
                if numCode == int(jwbStr):
                    #Not a soal, this is just a description for soal, find the other same code
                    # choices.pop(choices.index(rand))
                    soalGenerated.append(rand)
                    #delete the current soal
                    
                    # Soalsize+=1
                    while True:
                        try:
                            rand += 1
                            soalStr = tempDf.iloc[rand]["Soal"]
                            numCode = int(soalStr.split("<kode>")[0])
                            if numCode != int(jwbStr):
                                break
                            #delete the soal
                            # choices.pop(choices.index(rand))
                            soalGenerated.append(rand)
                            
                            Soalsize-=1
                            if(Soalsize <= 0):
                                break
                        except:
                            break
            else:
                # choices.pop(choices.index(rand))
                soalGenerated.append(rand)
                Soalsize -= 1
        # tempDf= tempDf.iloc[soalGenerated]
        return tempDf,soalGenerated        
    
    #randomly select 20 soal
        
    #display randsoalgenerator for matematika
    matdf,list_soal_Matematika = randSoalGenerator("Matematika")
    #display randsoalgenerator for pemrograman
    progdf,list_soal_Pemrograman = randSoalGenerator("Pemrograman")
    
    # st.write("Soal Matematika")
    # #display df but only the selected soal
    # st.write(matdf.iloc[list_soal_Matematika], use_container_width=True)
    # st.write("total soal : ", len(list_soal_Matematika))
        
    # st.write("Soal Pemrograman")
    # st.write(progdf.iloc[list_soal_Pemrograman], use_container_width=True)
    # st.write("total soal : ", len(list_soal_Pemrograman))


    # soalCount = 1
    def writeSoal(type):
        """
        Write soal to streamlit
        """
        
        soalCount = len(allSoal) + 1
        tempDf = matdf if type == "Matematika" else progdf
        list_soal = list_soal_Matematika if type == "Matematika" else list_soal_Pemrograman
        # list_soal.sort()
        flagCode = None
        for num,soal in enumerate(list_soal):
            all_jawaban = tempDf.iloc[soal]["Jawaban"].split(",")
            soalStr = tempDf.iloc[soal]["Soal"]
                #check if they have code
            if soalStr.find('<kode>') != -1:
                numCode = int(soalStr.split('<kode>')[0])
                if flagCode == numCode:
                    writeQuestion(f'{soalCount}. ' + soalStr.split('<kode>')[1])
                    random.shuffle(all_jawaban)
                    ans = st.radio('Jawaban :', ['']+all_jawaban, key=f'soalke-{soalCount}',index=0)
                    allAnswer.append(ans)
                    allSoal.append(soal)
                    clearfirstOption()
                else:
                    soalCount -= 1
                    flagCode = numCode
                    writeDescription(soalStr.split('<kode>')[1],type=type)
            
            else:
                # print(tempDf.iloc[soal]["Soal"])
                writeQuestion(f'{soalCount}. ' + soalStr)
                random.shuffle(all_jawaban)
                ans = st.radio('Jawaban :', ['']+all_jawaban, key=f'soalke-{soalCount}', index=0)
                allSoal.append(soal)
                allAnswer.append(ans)
                clearfirstOption()
            # st.write(all_jawaban)
            #Count the soal
            soalCount += 1
            
            

    # writeSoal("Matematika")
            
    writeSoal("Pemrograman")
        
    
    # @st.dialog('Confirmation')
    # def confirmation():
    #     # writeDescription("Apakah anda yakin sudah menjawab semua soal?")
    #     st.write("Apakah anda yakin sudah menjawab semua soal?")
    #     col1,col2 = st.columns(2)
    #     with col1:
    #         ya_button = st.button("Ya", key='ya')
    #     with col2:
    #         tidak_button = st.button("Tidak", key='tidak')
            
    #     if ya_button:
    #         #write to google sheet
    #         data = pd.DataFrame(columns=["Nama","Kelas","Soal","Jawaban"])
    #         #make data 1 row
    #         data = pd.concat(
    #             [data, pd.DataFrame({"Nama":['Dummy'],
    #                                  "Kelas":['Dummy'],
    #                                  "Soal":str(allSoal),
    #                                  "Jawaban":str(allAnswer)})],
    #             ignore_index=True
    #         )
            
    #         #append data to google sheet
    #         sheet.append_rows(data.values.tolist())
            
            
    #         st.success("Jawaban anda sudah terkirim")
    #         st.balloons()
    #         time.sleep(3)
    #         st.rerun()
    #     if tidak_button:
    #         st.session_state.confirmation_button = False
    #         st.success("Silahkan lanjutkan mengerjakan soal")
    #         #close dialog
        
    # st.write(allAnswer)
    
    button = st.form_submit_button("Submit Jawaban")
    
    if button:
        rated = {soal : ans for soal, ans in zip(allSoal, allAnswer)}
        st.session_state.answer = rated
        #write session state
        st.write(st.session_state.answer)

button2 = st.button("Lihat Jawaban")
if button2:
    st.write("Jawaban anda")
    st.write(st.session_state.answer)



    
    
    


