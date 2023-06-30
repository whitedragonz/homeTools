##!./homeTools-env/bin/python
# python -m pip install streamlit pandas ffmpy pillow selenium
# python -m pip install git+https://github.com/pytube/pytube --upgrade

import streamlit as st
from pytube import YouTube
from pytube import Playlist
import pandas as pd
import urllib.request
import ffmpy
from PIL import Image
from os.path import exists
import os
st.set_page_config(layout="wide")
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    os.remove('solaractivity.gif')
    os.remove('solaractivity.mp4')
    os.remove('iSWACygnetStreamer.gif')
    os.remove('schumann_resonance.jpg')
    os.remove('schumann_resonance_amplitude.jpg')
    os.remove('schumann_resonance_quality.jpg')
except:
    pass

def get_url(url):
    #extra = request.args.get("extra")
    #if extra: #if extra exists
    #url = 'https://www.youtube.com/watch?v=' + v_url
    if 'playlist' in url:
        p = Playlist(url)
        for yt in p.videos:
            yt.streams \
                .filter(progressive=True, file_extension='mp4') \
                .order_by('resolution') \
                .desc() \
                .first() \
                .download('/Users/simonbricteux/Downloads')
    else:
        yt = YouTube(url)
        yt.streams \
            .filter(progressive=True, file_extension='mp4') \
            .order_by('resolution') \
            .desc() \
            .first() \
            .download('/Users/simonbricteux/Downloads')

    return "Download complete!"

def input_comm(url):
    if url!='':
        st.write("The video url entered is {}".format(url))
        try: 
            get_url(url)
            #st.write("Download complete!")
            st.success("Download complete!",icon="🎊")
        except:
            st.write("Download error. Please check your url.")


st.title("Our home tools :smiley:")
st.session_state['text_key'] = ''
video_url= st.session_state.text_key

def proc(video_url):
    st.write(st.session_state.text_key)
    input_comm(video_url)

tab1, tab2, tab3 = st.tabs(['Solar weather','Schumann Resonance','Video download'])

#@st.cache_data
with tab1:
    kp = pd.read_json("https://services.swpc.noaa.gov/json/planetary_k_index_1m.json")
    kp.columns = ['Date Time', 'Kp Index', 'Estimated Kp', 'kp']
    kp.iloc[:,0] = pd.to_datetime(kp.iloc[:,0])
    kp.iloc[:,2] = pd.to_numeric(kp.iloc[:,2])
    kp_delta = round(kp.at[kp.shape[0]-1,"Estimated Kp"] - kp.at[0,"Estimated Kp"],2)
    st.metric(label = "Latest kp",value=kp.at[kp.shape[0]-1,"Estimated Kp"],delta=kp_delta,help="kp change in the last hour")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Real Time 1 min Kp")
        st.line_chart(data=kp,x="Date Time",y="Estimated Kp",width=1,use_container_width=True)
    with col2:
        st.subheader("Estimated Planetary K Index (3 hours)")
        kp_6h = pd.read_json('https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json')
        kp_6h.columns = ['Date Time', 'Kp', 'a_running', 'station_count']
        kp_6h.drop(index=[0],inplace=True) #,1))
        kp_6h.iloc[:,0] = pd.to_datetime(kp_6h.iloc[:,0])
        kp_6h.iloc[:,1] = pd.to_numeric(kp_6h.iloc[:,1])
        st.bar_chart(data=kp_6h,x="Date Time",y="Kp")

    urllib.request.urlretrieve('https://iswa.gsfc.nasa.gov/IswaSystemWebApp/iSWACygnetStreamer?timestamp=2038-01-23+00%3A44%3A00&window=-1&cygnetId=261','solaractivity.gif')
    try:
        ffmpy.FFmpeg(
            global_options=['-y'],
            inputs={'solaractivity.gif': None},
            outputs={'solaractivity.mp4': None}
        ).run()
    except:
        pass
    st.video('solaractivity.mp4', format="video/mp4", start_time=0)

with tab3:
    st.subheader("Video download")
    st.session_state.text_key= st.text_input(label="Enter a video url", help="YouTube only",key=11) #,label_visibility='hidden')
    video_url= st.session_state.text_key
    if video_url!='':
        input_comm(video_url)

with tab2:
    #Source: http://sosrff.tsu.ru/?page_id=7
    urllib.request.urlretrieve('http://sosrff.tsu.ru/srimage2/shm.jpg','schumann_resonance.jpg')
    image = Image.open('schumann_resonance.jpg')
    st.image(image, caption='Schumann Resonance')
    urllib.request.urlretrieve('http://sosrff.tsu.ru/srimage2/sra.jpg','schumann_resonance_amplitude.jpg')
    image = Image.open('schumann_resonance_amplitude.jpg')
    st.image(image, caption='Schumann Resonance Amplitude')
    urllib.request.urlretrieve('http://sosrff.tsu.ru/srimage2/srq.jpg','schumann_resonance_quality.jpg')
    image = Image.open('schumann_resonance_quality.jpg')
    st.image(image, caption='Schumann Resonance Quality')

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.timeanddate.com/weather/russia/tomsk/historic')
    sleep(1)

    e = driver.find_element(By.XPATH,'//*[@id="weatherContainer"]')
    location = e.location
    size = e.size
    w, h = size['width'], size['height']
    # driver.manage().window().setPosition(location['x'],location['y'])
    # e = driver.find_element(By.XPATH,'//*[@id="weatherContainer"]')
    # location = e.location
    # size = e.size
    # w, h = size['width'], size['height']
    st.write(location)
    st.write(size)
    st.write(w, h)

    driver.get_screenshot_as_file("tomsk_weather.png")
    driver.quit()
    image = Image.open('tomsk_weather.png')
    image_crop = image.crop((location['x'],location['y'],location['x']+w,location['y']+h))
    st.image(image_crop, caption='Past Weather in Tomsk')

    

#@st.cache_data

#https://youtu.be/KLyvfH1nDvk

##!/bin/zsh
#cd ~/PythonWork/pycharmprojects/api_test
# source ./venv/bin/activate
# streamlit run streamlit.py
#subprocess.run(["streamlit","run","streamlit.py"])
#streamlit hello

#~/.streamlit/config.toml