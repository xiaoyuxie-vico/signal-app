#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 08:52:49 2021

@author: markfleming
"""
# import pandas as pd
import matplotlib.pyplot as plt
# from urllib.request import urlopen
# import base64
# import seaborn as sns
import numpy as np
import streamlit as st
import sounddevice as sd
import scipy.io.wavfile as wavfile


st.set_option('deprecation.showPyplotGlobalUse', False)

st.header('Welcome to the Signal Modification App')
st.text('This app will show the effects of modifying mechanistic features of a signal')
st.text('') 
st.text('Features that can be modified are the damping and the number of harmonics in a signal')
st.text('')
st.text('')

fs_rate, sgnl = wavfile.read("YamahaA4.wav")

tt = np.linspace(0,2,44100)
omega = 5.0
b = 2

freq = st.slider('Frequency',min_value=1.0,max_value=10.0,value=5.0)

damp=st.slider('Damping',min_value=0.1,max_value=5.0,step=0.1)
st.write('Damping is:',damp)

plt.figure('piano')
piano = np.sin(2*np.pi*omega*tt) * np.exp(-tt*b)
plt.figure()
plt.plot(tt,piano,label='Original signal')
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')

bg = 0.5*b
guitar = np.sin(2*np.pi*freq*tt) * np.exp(-tt*damp)

plt.plot(tt,guitar, alpha=0.5,label='Modified signal')
plt.legend()
st.pyplot()

# plot number of harmonics

plt.figure()

frq = st.slider('Frq',min_value=1.0,max_value=500.0, value=omega)
st.write('Frequency ', frq)
hrm = st.slider('Number of Harmonics',min_value=1,max_value=5)
st.write('Number of harmonics is:',hrm)
damp2=st.slider('Damping2',min_value=0.1,max_value=5.0,step=0.1,value=2.0)
st.write('Damping is:',damp2)


pno = np.zeros_like(tt)
for ihrm in range(hrm):
    jhrm = ihrm+1
    pno += np.sin(2*np.pi*frq*tt*jhrm) * np.exp(-tt*damp2)
plt.plot(tt,pno)
plt.grid()
plt.ylabel('Amplitude')
plt.xlabel('Time (sec)')
st.pyplot()

# result = st.button('Play sound')
# # st.write(result,44100)

# if result:
#     sd.play(pno,44100)
#     