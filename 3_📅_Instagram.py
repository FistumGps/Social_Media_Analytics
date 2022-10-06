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
from instagram import get_data

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

lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/datafiles/cQiEsPrJCutfedV/data.json")

st_lottie(lottie_hello,
          height = 100,
          width = 100,key="instagram")
st.title("Instagram")
# Create sidebar
st.sidebar.markdown("<div><img src='https://cdn2.iconfinder.com/data/icons/social-media-icons-23/800/instagram-512.png' width=100 /><h1 style='display:inline-block'>instagram Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to analyse trending 📈  Instagram using Python and Streamlit.")
st.sidebar.markdown("To get started <ol><li>Enter the <i>username</i> you wish to analyse</li> <li>Hit <i>Get Data</i>.</li> <li>Get analyzing</li></ol>",unsafe_allow_html=True)

# Input
hastag_options = ["#EthiopianAirlines", "#SafaricomEthiopia", "#TPLF"]
#hashtag =  st.text_input('Search for a hashtag here', value ="")
hashtag =  st.selectbox('Select a hashtag here', options =hastag_options)
# Button
if st.button('Get Data'):
    # Run get data function here 
    get_data(hashtag)
    # Load existing data to test it out
    if hashtag =="#EthiopianAirlines":
        df = pd.read_csv('EthiopianAirlines.csv')
    if hashtag =="#SafaricomEthiopia":
        df = pd.read_csv('SafaricomEthiopia.csv')    
    if hashtag =="#TPLF":
        df = pd.read_csv('TPLF.csv')
    # plotly Viz here
    fig =px.histogram(df,x='commentsCount', hover_data=['caption'] ,y='likesCount',height=300) 
    st.plotly_chart(fig,use_container_width=True)

    # Split columns
    left_col, right_col = st.columns(2)

    # First Chart - video stats
    scatter1 = px.scatter(df, x='likesCount', y='commentsCount', hover_data=['caption'], size='likesCount', color='likesCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second Chart
    scatter2 = px.scatter(df, x='likesCount', y='commentsCount', hover_data=['caption'], size='likesCount', color='likesCount')
    right_col.plotly_chart(scatter2, use_container_width=True)

    # Show tabular dataframe in streamlit
    df
    with open("instagramdata.csv", "rb") as file:
        btn = st.download_button(
            label="click me to download csv",
            data=file,
            file_name="instagramdata.csv",
            mime="application/octet-stream"
            )

