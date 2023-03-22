import requests
import streamlit as st
from streamlit_lottie import st_lottie


#------------Find the emoji's here https://www.webfx.com/tools/emoji-cheat-sheet/ ----------------
st.set_page_config(page_title="My blog", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ----------Loading Assests ----------
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_w51pcehl.json")


# ---------- Header Section ----------
with st.container():
    st.subheader("I am Aditya Prakash Singh. :wave:")
    st.title("Techie by profession and a biker by heart")
    st.write("I have made this project for my personal use as well as to display some glimpse from the rides that I have already done.")
    st.write("[Here is the link to my blog] (https://singh-aditya1608.github.io/)")

# ---- What I do----
with st.container():
    st.write("---")            
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """ 
            This section has my professional details 
               - Currently I am working as a devops engineer with byjus for the last 2 years
               - I have worked on different services of aws 
               - Right now I am also working on a streamlit project which is based on python

             If you want to follow this project or my work that I did please follow the link 
             """

         )
        st.write("[github link >](https://github.com/singh-aditya1608)")

        with right_column:
            st_lottie(lottie_coding,height= 300, key= "coding")
