# Import base streamlit dependency
#from cgitb import text
#from enum import unique
#from tkinter.font import names
#from turtle import width
import streamlit as st
# Import pandas to load the analytics data
import pandas as pd
#import for Lottie Animation 
import json
import numpy as np

import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
#
from twitter import get_data
# Import time
import time
# Import plotly FOR VIZ
import plotly.express as px
# Set page width to wide
st.set_page_config(page_title= "Social Media Analytics", page_icon=":bar_chart:" ,layout='wide')
#st.header("Twitter")
@st.cache
#lottie Code
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_bz1uh69q.json")

st_lottie = st_lottie(lottie_hello,
          height = 100,
          width = 100,key="twitter")         
hastag_options = ["#EthiopianAirlines", "#SafaricomEthiopia", "#BeuDelivery"]
# Input

#my_bar = st.progress(0)

#for percent_complete in range(100):
    #time.sleep(0.1)
    #my_bar.progress(percent_complete + 1)

global numeric_columns
global text_columns

#hashtag =  st.text_input('Search for a hashtag here', value ="")
hashtag =  st.selectbox('Select a hashtag here', options = hastag_options)

if hashtag =="#EthiopianAirlines":
        df = pd.read_csv('EthiopianAirlines.csv')
if hashtag =="#SafaricomEthiopia":
        df = pd.read_csv('SafaricomEthiopia.csv')    
if hashtag =="#BeuDelivery":
        df = pd.read_csv('BeuDelivery.csv')
# Create sidebar
st.sidebar.markdown("<div><img src='https://help.twitter.com/content/dam/help-twitter/brand/logo.png' width=50 /><h1 style='display:inline-block'>Twitter Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to analyse trending 📈  Twitter data.")
              
st.markdown("""---""")
# Button
if st.sidebar.button('Get Additional Data'):
    # Run get data function here 
    get_data(hashtag)
    # Load existing data to test it out
    if hashtag =="#EthiopianAirlines":
        #df = df_selection
        df = pd.read_csv('EthiopianAirlines.csv')
    if hashtag =="#SafaricomEthiopia":
        #df = df_selection
        df = pd.read_csv('SafaricomEthiopia.csv')    
    if hashtag =="#BeuDelivery":
        #df = df_selection 
        df = pd.read_csv('BeuDelivery.csv')   

#df = df.replace({np.nan: None})
df['Date'] = pd.to_datetime(df['Date'],errors='ignore')
df = df.fillna('None')
# Select Numeric and Text columns from the dataframe          
numeric_columns = list(df.select_dtypes(['float64','int64','float32','int32','datetime64','datetime64[ns, UTC]']).columns)
text_columns = list(df.select_dtypes(['object']).columns)
location_column = df['Location'].unique()

# ---- SIDEBAR ----
check_box_top = st.sidebar.checkbox(label = "Display Dataset") 

if check_box_top:
    st.write(df)

# Add select widget
chart_select = st.sidebar.multiselect(
    label="Chart type",default=['Scatterplots', 'Lineplots','Histogram'],
    options=['Scatterplots', 'Lineplots','Histogram','Boxplots']
)

if 'Scatterplots' in chart_select:
    st.sidebar.subheader("Scatter plot Settings")
    x_values = st.sidebar.selectbox('X axis',options = numeric_columns)
    y_values = st.sidebar.selectbox('Y axis',options = numeric_columns)
    plot_scatter = px.scatter(data_frame = df, x = x_values, y = y_values, title = x_values +' '+"By"+' '+y_values+' '+"Scatter Plot")
    st.plotly_chart(plot_scatter,use_container_width=True)

if 'Lineplots' in chart_select:
    st.sidebar.subheader("Line plot Settings")
    future_selection = st.sidebar.multiselect('Add More Features To Plot',default=['Location','User'], options = text_columns)
    locations_dropdown = st.sidebar.selectbox('Location', options = location_column)
    df_location = df[df['Location'] == locations_dropdown]
    df_line = df_location[future_selection]
    plot_line = px.line(data_frame = df_line, x = df_line.index, y = future_selection, title = "Location"+' '+str(locations_dropdown) + ' '+'Tweeted')
    st.plotly_chart(plot_line,use_container_width=True)

if 'Histogram' in chart_select:
    st.sidebar.subheader("Histogram Chart Settings")
    select_box_his = st.sidebar.selectbox('Features',options = numeric_columns)
    histogram_slider = st.sidebar.slider(label="Number Of Bins",min_value=5,max_value=100,value=20)
    plot_histogram =px.histogram(df,x= select_box_his, nbins = histogram_slider,hover_data=['Tweet'], title="Count Tweet by"+' '+select_box_his) 
    st.plotly_chart(plot_histogram,use_container_width=True)

    #plot_scatter = px.scatter(data_frame = df, x = x_values, y = y_values, title = x_values +' '+"By"+' '+y_values+' '+"Scatter Plot")
    #st.plotly_chart(plot_scatter,use_container_width=True)

# plotly Viz here
#PIE CHART
col1,col2 = st.columns(2)
fig0 =px.pie(df.head(100),values='Likes_Count',names='User',width=400,color="User", title="Top 100 User With Most liked Tweet",hole=.4) 
fig0.update_traces(textposition='inside', textinfo='percent+label')
col1.plotly_chart(fig0,use_container_width=True)

# HISTOGRAM CHART-1
fig =px.histogram(df,x='User_FollowersCount', hover_data=['User_Verified'] ,y='User_Verified',width=300, color="User_Verified", title="Verified Users") 
col2.plotly_chart(fig,use_container_width=True)


# Split columns
#left_col, right_col = st.columns((5,5))

# First Chart - video stats
#scatter1 = px.scatter(df, x='User_Displayname', y='User_Location', hover_data=['User_Displayname'], size='User_FriendsCount', color='User_FriendsCount')
#left_col.plotly_chart(scatter1, use_container_width=True)

# Second Chart
#scatter2 = px.scatter(df, x='User_Displayname', y='User_Location', hover_data=['User_Displayname'], size='User_FollowersCount', color='User_FollowersCount')
#right_col.plotly_chart(scatter2, use_container_width=True)
df.info()
# Show tabular dataframe in streamlit
check_box_buttom = st.sidebar.checkbox(label = "Display Final Dataset") 

if check_box_buttom:
   st.dataframe(df)

if hashtag =="#EthiopianAirlines":
    with open("EthiopianAirlines.csv", "rb") as file:
        btn = st.download_button(
            label="Click me to download Data in csv",
            data=file,
            file_name="EthiopianAirlines.csv",
            mime="application/octet-stream"
            )
if hashtag =="#SafaricomEthiopia":
    with open("SafaricomEthiopia.csv", "rb") as file:
        btn = st.download_button(
            label="Click me to download Data in csv",
            data=file,
            file_name="SafaricomEthiopia.csv",
            mime="application/octet-stream"
            )
if hashtag =="#BeuDelivery":
    with open("BeuDelivery.csv", "rb") as file:
        btn = st.download_button(
            label="Click me to download Data in csv",
            data=file,
            file_name="BeuDelivery.csv",
            mime="application/octet-stream"
            )
    
        

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



#city = st.sidebar.multiselect(
    #"Is the User Verified:",
    #options=df["User_Verified"].unique(),
    #default=df["User_Verified"].unique()
#)



#df_selection = df.query(
 #"User_Verified == @user_verified")  
#st.dataframe(df_selection)   

#list = df.columns.tolist()
#choice = st.multiselect("Choose Data point", list, default="Location")
#data = df[choice]
#st.dataframe(data)

#st.line_chart(data)
