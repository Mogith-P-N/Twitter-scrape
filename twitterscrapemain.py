import pandas as pd
import streamlit as st

#page setup 
st.set_page_config(page_title="Twitter scrape", page_icon="🐍", layout="wide")
st.title("Twitter scrape")

#input account name or topic or hashtag to scrape data from twitter
name= st.text_input("Scrape data by name or hastag", value="")
