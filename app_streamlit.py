import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from fp_a_agent import run_fp_a_agent
import io
from datetime import datetime

# Load .env (GOOGLE_API_KEY)
load_dotenv()

st.set_page_config(page_title="FP&A AI Agent", layout="wide")
st.title("FP&A AI Agent – CFO-Grade FP&A with Data Analytics")
st.markdown(
    """
    Use this app to run advanced FP&A analysis with a virtual CFO-level AI agent. 
    Provide your business context, metrics, upload financial data, and get comprehensive analysis with visualizations.
    """
)

api_key = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key

if not api_key:
    st.error(
        "GOOGLE_API_KEY is not set. Create a `.env` file in the project folder "
        "and add `GOOGLE_API_KEY=your_key_here`."
    )
else:
    # File upload section
    st.markdown("### 📎 Upload Financial Data (Optional)")
    uploaded_file = st.file_uploader(
        "Upload Excel/CSV file with financial data",
        type=["xlsx", "xls", "csv"],
        help="Upload your financial statements, budgets, or actuals for analysis"
    )
    
    uploaded_data = None
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                uploaded_data = pd.read_csv(uploaded_file)
            else:
                uploaded_data = pd.read_excel(uploaded_file)
            st.success(f"✅ File uploaded: {uploaded_file.name} ({len(uploaded_data)} rows)")
            with st.expander("Preview uploaded data"):
                st.dataframe(uploaded_data.head(10))
        except Exception as e:
            st.error(f"Error reading file: {e}")

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
            height=200,
            placeholder=(
                "Example:\n"
                "We are a Series B SaaS startup with ARR, churn, CAC, burn, etc.\n"
                "We want a 3-year plan, key KPIs, risks, and recommendations."
            ),
        )
        
        # Add checkbox for enhanced output
        include_charts = st.checkbox("Include data visualizations and metrics", value=True)
        include_formulas = st.checkbox("Generate Google Sheets formulas", value=True)

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
                    # Build enhanced prompt
                    enhanced_prompt = prompt
                    
                    if uploaded_data is not None:
                        data_summary = f"\n\nUploaded Data Summary:\n"
                        data_summary += f"- Rows: {len(uploaded_data)}\n"
                        data_summary += f"- Columns: {', '.join(uploaded_data.columns.tolist())}\n"
                        enhanced_prompt += data_summary
                    
                    if include_charts:
                        enhanced_prompt += "\n\nPlease include specific numerical KPIs and metrics in your analysis."
                    
                    if include_formulas:
                        enhanced_prompt += "\n\nProvide Google Sheets formulas with IFERROR statements for key calculations."
                    
                    # Get AI response
                    response = run_fp_a_agent(enhanced_prompt, audience=audience)
                    
                    with col2:
                        output_placeholder.markdown(response)
                        
                        # Generate sample visualizations if data is uploaded
                        if uploaded_data is not None and include_charts:
                            st.markdown("---")
                            st.markdown("### 📊 Data Visualizations")
                            
                            # Try to detect numeric columns
                            numeric_cols = uploaded_data.select_dtypes(include=['number']).columns.tolist()
                            
                            if len(numeric_cols) > 0:
                                # Sample chart 1: Line chart
                                if len(numeric_cols) >= 1:
                                    fig1 = px.line(uploaded_data, y=numeric_cols[0], 
                                                  title=f"{numeric_cols[0]} Trend")
                                    st.plotly_chart(fig1, use_container_width=True)
                                
                                # Sample chart 2: Bar chart
                                if len(numeric_cols) >= 2:
                                    fig2 = px.bar(uploaded_data.head(10), y=numeric_cols[:min(2, len(numeric_cols))],
                                                 title="Key Metrics Comparison")
                                    st.plotly_chart(fig2, use_container_width=True)
                        
                        # Display Google Sheets formulas if requested
                        if include_formulas:
                            st.markdown("---")
                            st.markdown("### 📐 Google Sheets Formulas")
                            st.code("""
# Revenue Growth Rate
=IFERROR((B2-B1)/B1, 0)

# EBITDA Margin
=IFERROR(EBITDA/Revenue, 0)

# Burn Rate (Monthly)
=IFERROR(SUM(Expenses)/COUNT(Months), 0)

# Customer Acquisition Cost (CAC)
=IFERROR(Sales_Marketing_Spend/New_Customers, 0)

# Lifetime Value (LTV)
=IFERROR(ARPU*Customer_Lifetime_Months, 0)

# LTV/CAC Ratio
=IFERROR(LTV/CAC, 0)

# Cash Runway (Months)
=IFERROR(Cash_Balance/Monthly_Burn, 0)

# Gross Margin
=IFERROR((Revenue-COGS)/Revenue, 0)

# Operating Cash Flow
=IFERROR(EBITDA-CapEx-Working_Capital_Change, 0)

# Return on Equity (ROE)
=IFERROR(Net_Income/Shareholders_Equity, 0)
                            """, language="excel")
                            
                except Exception as e:
                    st.error(f"Error running FP&A AI Agent: {e}")
