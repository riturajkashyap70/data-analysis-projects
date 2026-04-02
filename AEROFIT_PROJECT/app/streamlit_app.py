import streamlit as st
from recommender import recommend_treadmill
st.title("AeroFit Recommendation System")

income = st.slider("Income", 20000, 100000)
fitness = st.slider("Fitness Level", 1, 5)
usage = st.slider("Usage per week", 1, 7)

if st.button("Recommend"):
    result = recommend_treadmill(income, fitness, usage)
    st.success(f"Recommended Product: {result}")