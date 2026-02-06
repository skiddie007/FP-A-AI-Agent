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

                                           # Download OUTPUT buttons
                    st.markdown("---")
                    st.markdown("### 💾 Download Analysis Output")
                    
                    out_col1, out_col2, out_col3, out_col4 = st.columns(4)
                    
                    with out_col1:
                        txt_data = response.encode('utf-8')
                        st.download_button(
                            label="📄 Download TXT",
                            data=txt_data,
                            file_name=f"fpa_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain"
                        )
                    
                    with out_col2:
                        csv_output = response.encode('utf-8')
                        st.download_button(
                            label="📊 Download CSV",
                            data=csv_output,
                            file_name=f"fpa_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv"
                        )
                    
                    with out_col3:
                        # DOCX download
                        try:
                            from docx import Document
                            doc = Document()
                            doc.add_heading('FP&A Analysis Output', 0)
                            doc.add_paragraph(response)
                            docx_buffer = io.BytesIO()
                            doc.save(docx_buffer)
                            docx_buffer.seek(0)
                            st.download_button(
                                label="📃 Download DOCX",
                                data=docx_buffer,
                                file_name=f"fpa_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx",
                                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                            )
                        except ImportError:
                            st.info("Install python-docx for DOCX export")
                    
                    with out_col4:
                        # XLSX download (put response in a cell)
                        xlsx_buffer = io.BytesIO()
                        output_df = pd.DataFrame({'FP&A Analysis': [response]})
                        output_df.to_excel(xlsx_buffer, index=False)
                        xlsx_buffer.seek(0)
                        st.download_button(
                            label="📈 Download XLSX",
                            data=xlsx_buffer,
                            file_name=f"fpa_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
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


                # Advanced Data Exploration
                if uploaded_data is not None:
                    st.markdown("---")
                    st.markdown("### 🔍 Advanced Data Explorer")
                    st.markdown("Ask questions about your uploaded data or view comprehensive analysis.")
                    
                    # Initialize data analyzer
                    analyzer = DataAnalyzer(uploaded_data)
                    
                    # Tabs for different analysis views
                    tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat with Data", "📊 Summary Stats", "📈 Trends", "💰 Financial Insights"])
                    
                    with tab1:
                        st.markdown("#### Ask Questions About Your Data")
                        
                        # Initialize chat history
                        if 'data_chat_history' not in st.session_state:
                            st.session_state.data_chat_history = []
                        
                        # Display chat history
                        for msg in st.session_state.data_chat_history:
                            with st.chat_message(msg["role"]):
                                st.markdown(msg["content"])
                        
                        # Chat input
                        user_question = st.chat_input("Ask about your data (e.g., 'What is the total revenue?', 'Show me the averages')")
                        
                        if user_question:
                            # Add user message
                            st.session_state.data_chat_history.append({"role": "user", "content": user_question})
                            with st.chat_message("user"):
                                st.markdown(user_question)
                            
                            # Get response from analyzer
                            answer = analyzer.query_data(user_question)
                            st.session_state.data_chat_history.append({"role": "assistant", "content": answer})
                            with st.chat_message("assistant"):
                                st.markdown(answer)
                    
                    with tab2:
                        st.markdown("#### Comprehensive Summary Statistics")
                        summary = analyzer.get_summary_statistics()
                        
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.metric("Total Rows", summary['total_rows'])
                        with col_b:
                            st.metric("Total Columns", summary['total_columns'])
                        
                        if 'numeric_stats' in summary:
                            st.markdown("**Numeric Columns Analysis:**")
                            for col, stats in summary['numeric_stats'].items():
                                with st.expander(f"📊 {col}"):
                                    col1, col2, col3 = st.columns(3)
                                    col1.metric("Mean", f"{stats['mean']:.2f}")
                                    col2.metric("Median", f"{stats['median']:.2f}")
                                    col3.metric("Std Dev", f"{stats['std']:.2f}")
                                    col1.metric("Min", f"{stats['min']:.2f}")
                                    col2.metric("Max", f"{stats['max']:.2f}")
                                    col3.metric("Sum", f"{stats['sum']:.2f}")
                        
                        if 'categorical_stats' in summary:
                            st.markdown("**Categorical Columns Analysis:**")
                            for col, stats in summary['categorical_stats'].items():
                                with st.expander(f"🏷️ {col}"):
                                    st.write(f"Unique Values: {stats['unique_values']}")
                                    st.write("Most Common:")
                                    st.write(stats['most_common'])
                    
                    with tab3:
                        st.markdown("#### Trends and Patterns")
                        trends = analyzer.get_trends_and_patterns()
                        
                        if trends:
                            for col, trend_data in trends.items():
                                with st.expander(f"📈 {col}"):
                                    st.write(f"**Trend:** {trend_data['trend'].upper()}")
                                    col1, col2, col3 = st.columns(3)
                                    col1.metric("First Value", f"{trend_data['first_value']:.2f}")
                                    col2.metric("Last Value", f"{trend_data['last_value']:.2f}")
                                    col3.metric("Change %", f"{trend_data['change_percentage']:.2f}%")
                        else:
                            st.info("No trends detected. Upload time-series or sequential data.")
                    
                    with tab4:
                        st.markdown("#### Financial Analysis Insights")
                        fin_insights = analyzer.get_financial_insights()
                        
                        if fin_insights:
                            if 'financial_columns_detected' in fin_insights:
                                st.success(f"Found {len(fin_insights['financial_columns_detected'])} financial columns")
                                st.write("Columns:", ", ".join(fin_insights['financial_columns_detected']))
                                
                                for col, metrics in fin_insights.items():
                                    if col != 'financial_columns_detected':
                                        with st.expander(f"💰 {col}"):
                                            col1, col2 = st.columns(2)
                                            col1.metric("Total", f"{metrics['total']:.2f}")
                                            col2.metric("Average", f"{metrics['average']:.2f}")
                                            st.write(f"**Trend:** {metrics['trend']}")
                            else:
                                st.info("No financial columns detected. Try columns with keywords like 'revenue', 'cost', 'profit', etc.")
                        else:
                            st.info("No financial insights available.")
                    
                    # Download analyzed data button
                    st.markdown("---")
                    st.markdown("### 💾 Download Analysis Data")
                    
                    download_col1, download_col2, download_col3 = st.columns(3)
                    
                    with download_col1:
                        csv_data = uploaded_data.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="📄 Download as CSV",
                            data=csv_data,
                            file_name=f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv"
                        )
                    
                    with download_col2:
                        # Excel download
                        excel_buffer = io.BytesIO()
                        uploaded_data.to_excel(excel_buffer, index=False)
                        excel_buffer.seek(0)
                        st.download_button(
                            label="📊 Download as Excel",
                            data=excel_buffer,
                            file_name=f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
