import streamlit as st
import pandas as pd

st.title("Peak Shaving Analyzer")

uploaded = st.file_uploader("CSV hochladen")

if uploaded:
    df = pd.read_csv(uploaded)

    st.line_chart(df["verbrauch_kw"])