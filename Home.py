import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(layout="wide")
col1, col2= st.columns([1,2])
content1 = """
I am a highly skilled Python Developer and Data Engineer with expertise in backend development, API design, and scalable data engineering solutions. 
I specialize in Python, SQL, Django, and FastAPI for building high-performance backend systems, and I have extensive experience in developing RESTful and GraphQL APIs for seamless data exchange and service integration.

My technical expertise extends to big data processing and real-time streaming with Apache Kafka, PySpark, and Databricks, enabling efficient ETL pipelines and large-scale data transformations. 
I have hands-on experience deploying cloud-based architectures across Azure, AWS, and GCP, ensuring scalability, reliability, and cost efficiency.

As a Microsoft-certified Azure Data Engineer, I specialize in optimizing ETL workflows, real-time data pipelines, and cloud-native solutions that enhance business intelligence and operational efficiency. 
With a Master’s in Data Engineering from the University of North Texas, I am committed to leveraging data-driven strategies, advanced analytics, and robust infrastructure to drive impactful decision-making and business growth.

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