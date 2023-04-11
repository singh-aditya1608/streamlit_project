from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#------------Find the emoji's here https://www.webfx.com/tools/emoji-cheat-sheet/ -----------------
st.set_page_config(page_title="My blog", page_icon=":tada:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ----------Loading Assests ----------
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_w51pcehl.json")
#lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2glqweqs.json")
lottie_code = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_htnujcuh.json")
lottie_art = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_SCkAdr.json")
img= Image.open("images/rose.jpeg")


# ---------- Header Section ----------
with st.container():
    st.subheader("Hey :wave: This is Aditya Prakash Singh.")
    st.title("I am Techie by profession and a biker by heart")
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

        st.write("---")
        # ------ About the art work done by my partner in crime ------
        st.header("About the art work done by my partner in crime")
        st.write("##")
        st.write(
            """ 
            Swathi is also a techie by profession and by heart she is a traveller & artist.

                - Working as a full fledge data analyst in a start up 
                - she is trained in bharatanatyam & mohiniyattam
                - Here are some glimpse of the artwork done by her.
            """
            
        )
        st.write("[artwork >]("")")
# --images--
with st.container():
    image_coloumn, text_coloumn = st.columns((1,2))
    with image_coloumn:
        st.image(img)        

        



    with right_column:
         st_lottie(lottie_coding,height= 300, key="coding")
         st_lottie(lottie_code,height = 200, key="code")
         st_lottie(lottie_art,height= 300, key="art")


#--------- Use local CSS------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


#--------- CONTACT ------
with st.container():
    st.write("---")
    st.header("Get in touch with me !")   
    st.write("##")

# ----DOCUMENTATION https://formsubmit.co/-------

    contact_form= """

    <form action="https://formsubmit.co/singh.aditya1608@gmail.com" method="POST">
    <input type = "hidden" name = "_captcha" value = "false" >
     <input type="text" name="name" placeholder = "your name " required>
     <input type="email" name="email" placeholder = "your email " required>
     <textarea name = "message" placeholder = "your msg" required ></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.empty()    


     
    
