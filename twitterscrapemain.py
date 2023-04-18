import pandas as pd
import streamlit as st
import snscrape.modules.twitter as sntwitter


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

#page setup 
st.set_page_config(page_title="Twitter scrape", page_icon="🐍", layout="wide")
st.title("Twitter scrape")

#input account name or topic or hashtag to scrape data from twitter
name= st.text_input("Scrape data by name or hastag", value="")

tweet_data=[]
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+name).get_items()):
   if i>10:
        break
   tweet_data.append([tweet.date, tweet.content, tweet.id, tweet.url, tweet.user, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.lang])


df=pd.DataFrame(tweet_data)
st.write(df)

csv=convert_df(df)
st.download_button(
    label="Click this button to download the data",
    data=csv,
    file_name='scrapped_df.csv',
    mime='text/csv',
)
