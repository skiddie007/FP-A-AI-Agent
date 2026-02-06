import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from fp_a_agent import run_fp_a_agent
import io
from data_analyzer import DataAnalyzer
from datetime import datetime

# Load .env (GOOGLE_API_KEY)
load_dotenv()

st.set_page_config(page_title="FP&A AI Agent", layout="wide")
st.title("FP&A AI Agent – CFO-Grade FP&A with Data Analytics")
st.markdown("""
    <div style='text-align: center; padding: 1rem 0 2rem 0;'>
        <p style='font-size: 1.2rem; color: #B0BEC5; font-weight: 400;'>
            🚀 Powered by Google Gemini AI | 📊 Advanced Analytics | 📈 Interactive Visualizations
        </p>
    </div>
""", unsafe_allow_html=True)

# Custom CSS for professional styling
st.markdown("""
"📊 FP&A AI Agent – CFO-Grade FP&A with Data Analytics")
