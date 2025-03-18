import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(layout="wide")
col1, col2= st.columns([1,2])
content1 = """
I am a Python Developer and Data Engineer with expertise in backend and API development, 
as well as scalable data engineering solutions. I specialize in Python, SQL, Django, FastAPI, REST, 
and GraphQL, alongside major Data Engineering technologies like Apache Kafka, PySpark, Databricks, and cloud platforms 
including Azure, AWS, and GCP.

As a Microsoft-certified Azure Data Engineer, I have hands-on experience in building and optimizing ETL pipelines, 
real-time data processing, and cloud-based architectures. I hold a Master’s in Data Engineering from the University of North Texas 
and am passionate about delivering efficient, data-driven solutions that enhance business intelligence and performance.

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



col3,col4 = st.columns(2)


df = pd.read_csv("data.csv", sep=';')

with col3:
     for index,row in df[0::2].iterrows():
          st.header(row["title"])
        
with col4:
     for index,row in df[1::2].iterrows():
          st.header(row['title'])