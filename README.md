# FP&A AI Agent - CFO-Grade Financial Planning & Analysis

🚀 **A Fully Autonomous Financial Planning & Analysis AI Agent** powered by advanced LLM with 20+ years of virtual CFO expertise.

## Overview

This FP&A AI Agent is a cutting-edge solution for financial teams looking to automate and accelerate their planning, forecasting, and analysis workflows. It works across multiple industries including:

- **Manufacturing** - Capacity utilization, RM cost, yield, EBITDA margin
- **BFSI** - NIM, CASA, credit cost, ROE
- **Retail** - Same-store sales, inventory turns, gross margin
- **SaaS** - ARR, churn, LTV/CAC, burn rate
- **Logistics** - Cost per km, fleet utilization
- **Healthcare** - ARPU, bed occupancy
- **Energy** - Realization, operating leverage

## Features

✅ **Financial Planning & Budgeting**
- Annual Operating Plan (AOP)
- Rolling Forecasts (Monthly/Quarterly)
- Bottom-up & Top-down models
- Driver-based forecasting
- Zero-based budgeting

✅ **Financial Modeling**
- Integrated 3-Statement Model
- Scenario & Sensitivity Analysis
- Stress testing & What-if analysis
- Valuation (DCF, Multiples)

✅ **Variance & Performance Analysis**
- Budget vs Actual
- Forecast vs Actual
- Volume/Price/Mix analysis
- Root cause identification

✅ **Strategic Finance**
- Make vs Buy decisions
- Pricing strategy
- Cost restructuring
- Capital allocation
- M&A financial assessment

✅ **Cash Flow & Working Capital**
- Operating cash flow optimization
- DSO, DPO, Inventory analysis
- Cash runway analysis
- Liquidity stress scenarios

✅ **Audience-Aware Communication**
- CEO: Strategic, concise
- Board: High-level, risk-focused
- Finance Team: Detailed, structured
- Operations: Practical, action-oriented

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- OpenAI API key

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/skiddie007/FP-A-AI-Agent.git
cd FP-A-AI-Agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Create a .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

Or on Windows PowerShell:
```powershell
@'
OPENAI_API_KEY=your_api_key_here
'@ | Out-File -FilePath .env -Encoding UTF8
```

## Quick Start

### Basic Usage

```python
from fp_a_agent import run_fp_a_agent

# Simple FP&A query
prompt = """
You are advising a Series B SaaS startup with:
- ARR: $8M
- Burn rate: $250k/month
- Monthly churn: 2%
- Goal: Scale to $20M ARR in 3 years

Prepare a 3-year high-level FP&A view with key KPIs and risks.
"""

response = run_fp_a_agent(prompt, audience="CEO")
print(response)
```

### Audience-Specific Output

```python
# For CEO - Executive Summary
response_ceo = run_fp_a_agent(prompt, audience="CEO")

# For Board - Risk-Focused View
response_board = run_fp_a_agent(prompt, audience="Board")

# For Finance Team - Detailed Analysis
response_finance = run_fp_a_agent(prompt, audience="Finance Team")

# For Operations - Action-Oriented
response_ops = run_fp_a_agent(prompt, audience="Operations")
```

### Streamlit Web App (Windows & Desktop)

You can run a simple UI using Streamlit.

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Ensure your `.env` file is in the project folder:

```text
OPENAI_API_KEY=your_api_key_here
```

3. Start the app:

```bash
streamlit run app_streamlit.py
```

The app will open in your browser at `http://localhost:8501`.  
Enter your prompt and choose the audience (CEO / CFO / Board / Finance Team / Operations).

### Windows Console App

For a lightweight Windows console app:

1. Install deps:

```bash
pip install -r requirements.txt
```

2. Create `.env`:

```text
OPENAI_API_KEY=your_api_key_here
```

3. Run:

```bash
python app_cli.py
```

#### Build a single .exe (optional)

To create a standalone Windows executable:

```bash
pip install pyinstaller
pyinstaller --onefile --console --name "FP-A-AI-Agent" app_cli.py
```

Then use `dist/FP-A-AI-Agent.exe` on any Windows machine with your `.env` file in the same folder.



## Core Capabilities

### 1. Budgeting & Forecasting
- Driver-based forecasting models
- Scenario planning (base/upside/downside)
- Rolling forecasts for agility

### 2. Variance Analysis
- Automated variance investigation
- Root cause analysis
- Actionable recommendations

### 3. KPI & Dashboard Design
- Leading & lagging KPIs
- Industry-specific metrics
- Early warning indicators

### 4. Strategic Decision Support
- Pricing strategy optimization
- Cost restructuring analysis
- Capital allocation decisions
- M&A financial assessment

## Example Use Cases

### 1. SaaS Growth Planning
```python
prompt = """
Our SaaS company has:
- Current ARR: $5M
- CAC: $2,000
- LTV: $25,000
- Churn: 3% monthly

We want to achieve $15M ARR in 2 years. What's the financial roadmap?
"""
response = run_fp_a_agent(prompt, audience="CEO")
```

### 2. Manufacturing Cost Optimization
```python
prompt = """
Manufacturing business:
- Revenue: $50M
- COGS: 60% of revenue
- Raw material inflation: 15% YoY
- Current capacity utilization: 75%

How can we optimize costs and improve margins by 5%?
"""
response = run_fp_a_agent(prompt, audience="CFO")
```

### 3. Retail Financial Planning
```python
prompt = """
Retail chain with 50 stores:
- Same-store sales growth: 2% YoY
- Inventory turns: 4.5x per year
- Gross margin: 35%
- Rent as % of sales: 8%

Plan for expansion to 75 stores. What's the financial impact?
"""
response = run_fp_a_agent(prompt, audience="Board")
```

## How It Works

1. **Industry Identification** - Agent identifies industry, business model, revenue drivers
2. **Financial Analysis** - Applies FP&A frameworks and best practices
3. **Scenario Modeling** - Creates multiple scenarios with sensitivities
4. **Insights Generation** - Identifies risks, opportunities, and recommendations
5. **Audience Adaptation** - Tailors output based on recipient
6. **Actionable Output** - Provides structured, decision-ready insights

## Financial Thinking Framework

The agent follows this hierarchy:
```
Revenue → Margin → EBITDA → Cash Flow → ROCE
```

**Key Principles:**
- Profitability is useless without cash
- Growth is useless without returns
- Strategy must be quantified
- Numbers must be conservative and achievable

## System Prompt Architecture

The agent uses a comprehensive system prompt that includes:
- CFO-level expertise across 7+ industries
- Financial modeling frameworks
- Accounting standards (IFRS, Ind AS, US GAAP)
- Ethical guidelines and professional standards
- Fail-safe behaviors for vague or unrealistic requests

## API Models Supported

- **gpt-4-turbo** (Recommended) - Best accuracy for complex financial analysis
- **gpt-4** - Excellent for detailed modeling
- **gpt-4-mini** - Fast and cost-effective for simpler queries

## Configuration

### Adjust Parameters

```python
from openai import OpenAI

client = OpenAI()

# Customize model
model = "gpt-4-turbo"  # or gpt-4, gpt-4-mini

# Adjust response length
max_tokens = 3000  # Increase for more detailed analysis

# Control randomness
temperature = 0.7  # 0-1, lower = more deterministic
```

## Best Practices

✅ **DO:**
- Provide industry context upfront
- Include key financial metrics
- Specify audience/stakeholder
- Request specific analysis types (budget, forecast, variance, etc.)
- Include data assumptions
- Ask for sensitivity analysis

❌ **DON'T:**
- Provide sensitive/confidential information
- Ask for illegal financial advice
- Use without verifying outputs with domain experts
- Rely solely on AI output for critical decisions
- Expect real-time market data

## Output Structure

All responses follow this format:

1. **Executive Summary** - Key findings in 2-3 lines
2. **Key Insights** - Main points and observations
3. **Financial Impact** - Quantified outcomes
4. **Risks & Assumptions** - Critical dependencies
5. **Recommended Actions** - Next steps
6. **Optional Models/KPIs** - Supporting analysis

## Troubleshooting

### Issue: API Key Error
```
Solution: Ensure OPENAI_API_KEY is set in .env file
echo "OPENAI_API_KEY=sk-..." > .env
```

### Issue: Timeout Error
```
Solution: Increase timeout or use gpt-4-mini for faster responses
```

### Issue: Poor Response Quality
```
Solution: 
- Provide more context
- Be specific about industry and business model
- Include key metrics and assumptions
- Specify the audience
```

## Future Enhancements

🔮 Planned Features:
- Excel/CSV file integration for direct data upload
- Real-time market data integration
- Automated dashboard generation
- Industry-specific sub-agents
- Multi-step reasoning chains
- Custom financial models
- API for enterprise integration

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or suggestions:
- GitHub Issues: [Report a bug](https://github.com/skiddie007/FP-A-AI-Agent/issues)
- Email: [Your Email]
- LinkedIn: [Your Profile]

## Disclaimer

This AI agent is designed to assist with financial analysis and planning. It should NOT be used as a substitute for professional financial, legal, or accounting advice. Always verify outputs with qualified financial professionals before making critical business decisions.

## Author

Built by **skiddie007** - Financial Technology Developer
- 5+ years FP&A expertise
- CFA,MBA (Finance)
- Specialist in AI-powered financial automation

---

**Made with 💙 for CFOs and Finance Teams**
