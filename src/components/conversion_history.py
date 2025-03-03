import streamlit as st
import pandas as pd

def conversion_history(history):
    df = pd.DataFrame(history, columns=["Value", "From Unit", "Result", "To Unit"])
    st.table(df)