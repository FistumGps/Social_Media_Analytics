# Import base streamlit dependency
import streamlit as st
# Import pandas to load the analytics data
import pandas as pd
#import for Lottie Animation 
import json

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

#lottie Code
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_keymopaz.json")

st_lottie(lottie_hello,
          height = 100,
          width = 100,key="tiktok")
st.title("Tik-Tok")
# Create sidebar
st.sidebar.markdown("<div><img src='https://png2png.com/wp-content/uploads/2021/08/Tiktok-logo-png.png' width=100 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to analyse trending 📈  tiktoks using Python and Streamlit.")
st.sidebar.markdown("To get started <ol><li>Enter the <i>hashtag</i> you wish to analyse</li> <li>Hit <i>Get Data</i>.</li> <li>Get analyzing</li></ol>",unsafe_allow_html=True)

hastag_options = ["#EthiopianAirlines", "#SafaricomEthiopia", "#TPLF"]
# Input
#hashtag =  st.text_input('Search for a hashtag here', value ="")
hashtag =  st.selectbox('Select a hashtag here', options =hastag_options)

# Button
if st.button('Get Data'):
    # Run get data function here 
    # Load existing data to test it out
    get_data(hashtag)
    if hashtag =="#EthiopianAirlines":
        df = pd.read_csv('EthiopianAirlines.csv')
    if hashtag =="#SafaricomEthiopia":
        df = pd.read_csv('SafaricomEthiopia.csv')    
    if hashtag =="#TPLF":
        df = pd.read_csv('TPLF.csv')
    # plotly Viz here
    fig =px.histogram(df,x='authorMeta_name', hover_data=['text'] ,y='diggCount',height=300) 
    st.plotly_chart(fig,use_container_width=True)

    # Split columns
    left_col, right_col = st.columns(2)

    # First Chart - video stats
    scatter1 = px.scatter(df, x='shareCount', y='commentCount', hover_data=['text'], size='playCount', color='playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second Chart
    scatter2 = px.scatter(df, x='authorMeta_video', y='authorMeta_heart', hover_data=['authorMeta_nickName'], size='authorMeta_fans', color='authorMeta_fans')
    right_col.plotly_chart(scatter2, use_container_width=True)

    # Show tabular dataframe in streamlit
    df
    with open("tiktokdata.csv", "rb") as file:
        btn = st.download_button(
            label="click me to download csv",
            data=file,
            file_name="tiktokdata.csv",
            mime="application/octet-stream"
            )

