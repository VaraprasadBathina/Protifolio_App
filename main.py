import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns([1,2])
content = """
I am a Python Developer and Data Engineer with expertise in backend and API development, 
as well as scalable data engineering solutions. I specialize in Python, SQL, Django, FastAPI, REST, 
and GraphQL, alongside major Data Engineering technologies like Apache Kafka, PySpark, Databricks, and cloud platforms 
including Azure, AWS, and GCP.

As a Microsoft-certified Azure Data Engineer, I have hands-on experience in building and optimizing ETL pipelines, 
real-time data processing, and cloud-based architectures. I hold a Master’s in Data Engineering from the University of North Texas 
and am passionate about delivering efficient, data-driven solutions that enhance business intelligence and performance.

"""


with col1:
    st.image("images/photo.png")

with col2:

     st.title("Vidhyalakshmivaraprasad Bathina")
     st.info(content)
     
    
