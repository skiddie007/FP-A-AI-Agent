#!/bin/bash
set -e

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create .streamlit directory if it doesn't exist
mkdir -p .streamlit

# Run the Streamlit app
streamlit run app_streamlit.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
