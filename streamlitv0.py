##!./venv/bin/python
import streamlit as st
import subprocess

st.title("Our home tools :smiley:")

url=''
while url=='':
    url = st.text_area(label="Video url",height=22,key=1)
#st.text_area(key=1,label
st.write("The video url entered is {}".format(url))

#@st.cache_data

#subprocess.run(["streamlit","run","streamlit.py"])
#streamlit hello
