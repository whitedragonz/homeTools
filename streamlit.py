##!./venv/bin/python
import streamlit as st
from pytube import YouTube
from pytube import Playlist

def get_url(v_url):
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
    if video_url!='':
        st.write("The video url entered is {}".format(video_url))
        try: 
            get_url(video_url)
            st.write("Download complete!")
            st.success("Download complete!","🎊")
        except:
            st.write("Download error. Please check your url.")


st.title("Our home tools :smiley:")

st.session_state['text_key'] = ''
video_url= st.session_state.text_key

def proc():
    st.write(st.session_state.text_key)
    input_comm(video_url)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Video download")
    st.session_state['text_key'] = st.text_input(label="video url",on_change=proc, key=11,label_visibility='hidden') #next(widget_id),)
    #on_change=input_comm(video_url)
    if video_url!='':
        input_comm(video_url)
    st.write("Video url is: {}".format(video_url))

with col2:
    st.subheader("Solar weather")
    st.write("Work in progress")
#@st.cache_data

#https://youtu.be/KLyvfH1nDvk

##!/bin/zsh
#cd ~/PythonWork/pycharmprojects/api_test
# source ./venv/bin/activate
# streamlit run streamlit.py
#subprocess.run(["streamlit","run","streamlit.py"])
#streamlit hello

#~/.streamlit/config.toml