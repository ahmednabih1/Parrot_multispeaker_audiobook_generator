# %%
#!pip install streamlit
#!pip install hydralit
# %%
from tkinter import CENTER
from turtle import position, width
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from annotated_text import annotated_text
from streamlit_option_menu import option_menu
# %%

st.set_page_config(page_title= "Parrot", page_icon=":tada",layout = "wide") 
#-----------------------------------------------------------------functions

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None

    return r.json()


def header(url):
         st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
# %%

#header section
fulllogo = Image.open("images/fulllogo.png")
st.image(fulllogo,width = 230)
st.subheader("Hi, Welcome to Parrot :wave:")



# %%


#---------------------------------------------------------------------------------------------img 1
with st.container():
    st.write("---")
    left_column,center_column, right_column = st.columns((1, 1, 1))

    with right_column:
        st.write("##")
        st.write("##")
        st.image("images/undraw_Bibliophile_re_xarc.png" , width = 300)

    with left_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.markdown("<h1 style='text-align: left; color: black;'>Parrot is an app that gives life to your stories using AI</h1>", unsafe_allow_html=True)


st.write("##")
st.write("##")

#-------------------------------------------------------------------------------------------img 2
with st.container():
    left_column,center_column, right_column = st.columns((1.3, 1, 1.3))

    with left_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")


        st.image("images/undraw_summer_1wi4.png" , width = 400)

    with right_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.markdown("<h1 style='text-align: left; color: black;'>With a few clicks you can turn your favorite novel or story...</h1>", unsafe_allow_html=True)



st.write("##")
st.write("##")
st.write("##")


#---------------------------------------------------------------------------------------------img 3
with st.container():
    st.write("##")
    st.write("##")

    left_column,center_column, right_column = st.columns((1.3, 1, 1.2))

    with right_column:
        st.write("##")
        st.write("##")
        st.write("##")

        st.image("images/undraw_Audio_conversation_re_3t38.png" , width = 450)

    with left_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.markdown("<h1 style='text-align: left; color: black;'>into a full multi speaker audiobook, giving each character their personality</h1>", unsafe_allow_html=True)


#--------------------------------------------------------------------------------------------img 4
with st.container():
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")


    left_column,center_column, right_column = st.columns((1, 1, 1.4))

    with left_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")


        st.image("images/undraw_Imagination_re_i0xi.png" , width = 400)

    with right_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.markdown("<h1 style='text-align: left; color: black;'>and enjoy multitasking while listening to your beloved characters telling their stories.</h1>", unsafe_allow_html=True)




st.write("##")
st.write("##")
st.write("##")


st.markdown("<h1 style='text-align: center; color: #480ca8;'>Try it now</h1>", unsafe_allow_html=True)
#---------------------------------------------------------------------------------Swapping between story generation and inventory

st.write("##")
st.write("##")

with st.container():
        selected2 = option_menu(None, ["Make a story", "List inventory"], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal")

    

        if selected2 =="List inventory":
                        st.write("##")
                        st.write("##")


                        with st.container():
                            first,second,third = st.columns((1,1,1))

                            with second:
                                option = st.selectbox(
                            'Chose your story',
                            ('Iron Fathi ', 'Fight club', 'Harry potter and the Philospher stone'))

                            st.write("##")
                            st.write("##")


                        with st.container():
                            st.write("##")
                            st.write("##")

                            first1,second1,third1 = st.columns((1,0.5,1))

                            with second:
                                g1 = st.markdown("""
                                <style>
                                div.stButton > button:first-child {
                                    background-color: #480ca8;
                                    color:white;
                                    width:100;
                                    height:200;
                                    font-size:25px;
                                    height:3em;
                                    width:100%;
                                    position:center;
                                    border-radius:10px 10px 10px 10px;
                                }
                                </style>""", unsafe_allow_html=True)

                                g1 = st.button("Generate")   
                        
            
        else:
            
            st.write("##")

            with st.container():
                left,center,right = st.columns((1,3,1))

                with center:
                    st.write("##")
                    sentence = st.text_area('Enter your story here:', height=200 , key= "txt")

            #-----------------------------------------------------------------------------------upload file
            with st.container():
                left2,center2,right2 = st.columns((1,1,1))

                with center2:
                    st.file_uploader("upload here")

            #-----------------------------------------------------------------------------------buttons
            with st.container():
                st.write("##")
                right, centerright, centerleft, left = st.columns((2,1,1,2))
                
                with centerleft:
                    m = st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background-color: #480ca8;
                        color:white;
                    }
                    </style>""", unsafe_allow_html=True)

                    b = st.button("Process")        

                    #st.button(' Process', help="this lets parrot read the story first")
                with centerright:
                    m2 = st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background-color: #480ca8;
                        color:white;
                        width:100;
                        height:200;
                        font-size:25px;
                        height:3em;
                        width:10em;
                        position:center;
                        border-radius:10px 10px 10px 10px;
                    }
                    
                    </style>""", unsafe_allow_html=True)

                    b2 = st.button("Generate")   

                    #st.button("Generate", help="this will generate your story as audio")

#-------------------------------------------------------------------------------------------Contact form
with st.container():
    st.write("---")
    st.header("Get In Touch With The Team")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/ANABIH7000@GMAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
#-------------------------------------------------------------test




# 3. CSS style definitions
