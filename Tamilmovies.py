#Basics and fundamentals


#Core package
import streamlit as st


# Load EDA packages

import pandas as pd 

#display data
st.header("Top 10 Tamil Movies")

df =pd.read_csv("Top100.csv")

#method 1

st.dataframe(df)


#method 2 static table

#st.table(df)


#Adding a color style  from pandas

#st.dataframe(df.style.highlight_max(axis=0))








