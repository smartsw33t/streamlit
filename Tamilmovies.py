#Basics and fundamentals


#Core package
import streamlit as st


# Load EDA packages

import pandas as pd 

#display data

df =pd.read_csv("Top100.csv")

#method 1

#st.dataframe(df)


#method 2 static table

#st.table(df)


#Adding a color style  from pandas

st.dataframe(df.style.highlight_max(axis=0))












#Working with Text
#st.text("Hello world this is a text")
#name ="bro"
#st.text("அருமை {}". format(name))

#Header
#st.header("This is a header")
#Sub header
#st.subheader("This is a subheader")
#Title
#st.title("This is a title")
#Markdown
#st.markdown("## Trying to figure out mark down")

#Colorful text like Bootstrap
#st.success("Successful")
#st.warning("Echarikkai")
#st.info("Thagavalgal")
#st.error("Engayo thappu nadandhu irukku")

#Superfunction
#st.write("##Idhu oru vaakkiyam")
#st.write(888+143)
#st.write(dir(st))
#Help
#st.help(range)