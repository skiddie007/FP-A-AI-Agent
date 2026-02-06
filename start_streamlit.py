#!/usr/bin/env python3
import os
import sys
import subprocess

# Set environment variables for Streamlit
os.environ['STREAMLIT_SERVER_PORT'] = os.getenv('PORT', '10000')
os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
os.environ['STREAMLIT_LOGGER_LEVEL'] = 'info'

# Run Streamlit app
subprocess.run([
    sys.executable, '-m', 'streamlit', 'run',
    'app_streamlit.py',
    '--server.port', os.environ['STREAMLIT_SERVER_PORT'],
    '--server.address', '0.0.0.0',
    '--logger.level=info'
])
