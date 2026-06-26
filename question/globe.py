import streamlit as st
from streamlit_globe import streamlit_globe

st.subheader("Globe")
pointsData=[{'lat': 49.19788311472706, 'lng': 8.114625722364316, 'size': 0.3, 'color': 'red'}]
labelsData=[{'lat': 49.19788311472706, 'lng': 8.114625722364316, 'size': 0.3, 'color': 'red', 'text': 'Landau'}]
streamlit_globe(pointsData=pointsData, labelsData=labelsData, daytime='day', width=800, height=600)