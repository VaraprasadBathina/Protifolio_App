import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(layout="wide")
col1, col2= st.columns([1,2])
content1 = """
I'm a Python Developer and Data Engineer with expertise in Backend Development, API architecture, and scalable data solutions. 
I specialize in Python, SQL, Django, FastAPI, and RESTful & GraphQL APIs, building high-performance applications that enhance efficiency and innovation.

With hands-on experience in Big Data processing, real-time streaming (Apache Kafka, PySpark, Databricks), and cloud platforms (Azure, AWS, GCP), I design and optimize ETL pipelines and cloud-native architectures. 
As a Microsoft-certified Azure Data Engineer with a Master’s in Data Engineering from UNT, I’m passionate about transforming complex data into actionable insights that drive business success.

"""

content2 = " Below You Can Find some of the Python & Data Engineering projects I have Personally Done!"  

img = Image.open("images/photo.png")
img = img.resize((325, 350))


with col1:
    st.image(img)

with col2:

     st.title("Vidhyalakshmivaraprasad Bathina")
     st.info(content1)


col5 = st.container()
with col5:
     st.write(content2)



col3,empty_col,col4 = st.columns([1,1,1])


df = pd.read_csv("data.csv", sep=';')

with col3:
     for index,row in df[0::2].iterrows():
          st.header(row["title"])
          st.write(row["description"])
          st.image("images/"+row["image"])
          st.write(f"[source code]({row['url']})")
        
with col4:
     for index,row in df[1::2].iterrows():
          st.header(row['title'])
          st.write(row["description"])
          st.image("images/"+row["image"])
          st.write(f"[source code]({row['url']})")