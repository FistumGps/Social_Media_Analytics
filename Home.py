# Import base streamlit dependency
import streamlit as st
# Import pandas to load the analytics data
import pandas as pd
#import for Lottie Animation 
import json

#pip install pipreqs
#pipreqs ./
#pipreqs --encoding=utf8


import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
#
from tiktok import get_data

# Import plotly FOR VIZ
import plotly.express as px

# Set page width to wide
st.set_page_config(
  page_title= "Social Media Analytics",
  layout='wide')

st.title("Social Media Analytics")
#lottie Code
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_BDdCMNoST6.json")

st_lottie(lottie_hello,
          height = 500,
          width = 900,key="socialmedia")
