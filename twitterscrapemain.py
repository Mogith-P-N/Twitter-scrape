import pandas as pd
import streamlit as st
import snscrape.modules.twitter as sntwitter

#page setup 
st.set_page_config(page_title="Twitter scrape", page_icon="🐍", layout="wide")
st.title("Twitter scrape")

#input account name or topic or hashtag to scrape data from twitter
name= st.text_input("Scrape data by name or hastag", value="")

tweet_data=[]
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+name).get_items()):
   if i>10:
        break
   tweet_data.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
df=pd.DataFrame(tweet_data)
st.write(df)
st.download_button(
    label="Click this button to download the data",
    data=df,
    mime='text/csv',
)
