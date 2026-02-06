import os
from dotenv import load_dotenv
import streamlit as st
from fp_a_agent import run_fp_a_agent

# Load .env (GOOGLE_API_KEY)
load_dotenv()

st.set_page_config(page_title="FP&A AI Agent", layout="wide")
st.title("FP&A AI Agent – CFO-Grade FP&A")

st.markdown(
    """
Use this app to run advanced FP&A analysis with a virtual CFO-level AI agent.
Provide your business context, metrics, and what you want the agent to do.
    """
)

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error(
        "GOOGLE_API_KEY is not set. Create a `.env` file in the project folder "
        "and add `GOOGLE_API_KEY=your_key_here`."
    )
else:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        audience = st.selectbox(
            "Audience (who will read this output?)",
            ["CEO", "CFO", "Board", "Finance Team", "Operations"],
            index=0,
        )
        
        st.markdown("### FP&A Prompt")
        prompt = st.text_area(
            "Describe the business, metrics, and what analysis you want.",
            height=260,
            placeholder=(
                "Example:\n"
                "We are a Series B SaaS startup with ARR, churn, CAC, burn, etc.\n"
                "We want a 3-year plan, key KPIs, risks, and recommendations."
            ),
        )
        
        run_button = st.button("Run FP&A Analysis", type="primary")
    
    with col2:
        st.markdown("### Output")
        output_placeholder = st.empty()
    
    if run_button:
        if not prompt.strip():
            st.warning("Please enter a prompt before running the agent.")
        else:
            with st.spinner("Running FP&A AI Agent..."):
                try:
                    response = run_fp_a_agent(prompt, audience=audience)
                    output_placeholder.markdown(response)
                except Exception as e:
                    st.error(f"Error running FP&A AI Agent: {e}")
