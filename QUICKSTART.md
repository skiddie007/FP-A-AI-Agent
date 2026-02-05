# 🚀 Quick Start Guide - Run the FP&A AI Agent

## 5-Minute Setup & Run

Follow these simple steps to get the FP&A AI Agent running on your machine.

---

## Step 1: Prerequisites Check

### On Windows:
```powershell
# Check Python version (3.8 or higher)
python --version

# Check pip
pip --version
```

### On Mac/Linux:
```bash
# Check Python version (3.8 or higher)
python3 --version

# Check pip
pip3 --version
```

**Don't have Python?** Download from [python.org](https://www.python.org/downloads/)

---

## Step 2: Clone the Repository

```bash
# Clone the repo
git clone https://github.com/skiddie007/FP-A-AI-Agent.git

# Navigate to the directory
cd FP-A-AI-Agent
```

---

## Step 3: Install Dependencies

### On Windows (CMD or PowerShell):
```powershell
pip install -r requirements.txt
```

### On Mac/Linux (Terminal):
```bash
pip3 install -r requirements.txt
```

**What gets installed:**
- `openai` - OpenAI API client
- `python-dotenv` - Environment variables
- `pandas` - Data processing
- `numpy` - Numerical computations
- `requests` - HTTP library

---

## Step 4: Get OpenAI API Key

1. Go to [OpenAI API Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the API key (you'll use it next)

---

## Step 5: Set Environment Variable

### Option A: Create .env file (Recommended)

**On Windows (PowerShell):**
```powershell
@'
OPENAI_API_KEY=sk-your-api-key-here
'@ | Out-File -FilePath .env -Encoding UTF8
```

**On Windows (Command Prompt):**
```cmd
echo OPENAI_API_KEY=sk-your-api-key-here > .env
```

**On Mac/Linux:**
```bash
echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
```

### Option B: Set as System Environment Variable

**Windows:**
- Press `Win + X`, select "System"
- Click "Advanced system settings"
- Click "Environment Variables"
- New → Variable name: `OPENAI_API_KEY`, Value: `sk-your-api-key-here`
- Click OK and restart your terminal

**Mac/Linux:**
```bash
export OPENAI_API_KEY="sk-your-api-key-here"
# Or add to ~/.bash_profile or ~/.zshrc for persistence
echo 'export OPENAI_API_KEY="sk-your-api-key-here"' >> ~/.bash_profile
source ~/.bash_profile
```

---

## Step 6: Run the Agent

### Create a test script (test_agent.py):

```python
from fp_a_agent import run_fp_a_agent

# Example 1: SaaS Growth Planning
print("\n" + "="*80)
print("EXAMPLE 1: SaaS Growth Planning")
print("="*80 + "\n")

prompt_1 = """
Our SaaS startup has:
- Current ARR: $8M
- Monthly burn rate: $250k
- Monthly churn: 2%
- Goal: Scale to $20M ARR in 3 years

What's the financial roadmap? Include key KPIs and risks.
"""

response_1 = run_fp_a_agent(prompt_1, audience="CEO")
print(response_1)

# Example 2: Manufacturing Cost Optimization
print("\n" + "="*80)
print("EXAMPLE 2: Manufacturing Cost Optimization")
print("="*80 + "\n")

prompt_2 = """
Manufacturing company:
- Revenue: $50M
- COGS: 60% of revenue
- Capacity utilization: 75%
- Raw material inflation: 15% YoY

How can we improve margins by 5% without affecting quality?
Provide concrete cost optimization recommendations.
"""

response_2 = run_fp_a_agent(prompt_2, audience="Finance Team")
print(response_2)

# Example 3: Retail Expansion Planning
print("\n" + "="*80)
print("EXAMPLE 3: Retail Expansion Planning")
print("="*80 + "\n")

prompt_3 = """
Retail chain with 50 stores:
- Same-store sales growth: 2% YoY
- Gross margin: 35%
- Rent as % of sales: 8%
- Inventory turns: 4.5x

We want to expand to 75 stores in the next 2 years.
What's the financial impact? Include capital requirements and ROI.
"""

response_3 = run_fp_a_agent(prompt_3, audience="Board")
print(response_3)
```

### Run the script:

**On Windows:**
```powershell
python test_agent.py
```

**On Mac/Linux:**
```bash
python3 test_agent.py
```

---

## Step 7: View Results

The agent will output:

1. **Executive Summary** - High-level findings
2. **Key Insights** - Main points and observations
3. **Financial Impact** - Quantified outcomes
4. **Risks & Assumptions** - Critical dependencies
5. **Recommended Actions** - Next steps

---

## Using Different Audiences

```python
from fp_a_agent import run_fp_a_agent

prompt = "Your financial question here..."

# For CEO - Executive, concise
response_ceo = run_fp_a_agent(prompt, audience="CEO")

# For Board - Risk-focused, high-level
response_board = run_fp_a_agent(prompt, audience="Board")

# For Finance Team - Detailed, structured
response_finance = run_fp_a_agent(prompt, audience="Finance Team")

# For Operations - Practical, action-oriented
response_ops = run_fp_a_agent(prompt, audience="Operations")
```

---

## Common Issues & Fixes

### ❌ Error: "API key not found"

**Solution:** Ensure .env file exists in the project root with:
```
OPENAI_API_KEY=sk-your-api-key
```

OR set as environment variable and restart terminal.

### ❌ Error: "Module 'openai' not found"

**Solution:**
```bash
pip install -r requirements.txt
# or
pip install openai python-dotenv pandas numpy requests
```

### ❌ Error: "Connection timeout"

**Solution:** 
- Check internet connection
- Use `gpt-4-mini` model (faster)
- Increase timeout in `fp_a_agent.py`

### ❌ Error: "Insufficient quota"

**Solution:**
- Check OpenAI billing: https://platform.openai.com/account/billing/overview
- Add payment method
- Set usage limits

---

## Advanced: Customizing the Agent

### Change the Model:

Edit `fp_a_agent.py` line 174:
```python
# Change from:
model="gpt-4-turbo",

# To:
model="gpt-4-mini",  # Cheaper and faster
# or
model="gpt-4",       # More expensive, more accurate
```

### Adjust Response Length:

```python
# In fp_a_agent.py, change:
max_tokens=2000  # Increase for longer responses
```

### Control Randomness:

```python
# In fp_a_agent.py, change:
temperature=0.7  # 0=deterministic, 1=creative
```

---

## Next Steps

✅ **You've successfully run the FP&A AI Agent!**

Now explore:
1. Try different industries (SaaS, Manufacturing, Retail, etc.)
2. Ask specific FP&A questions (budgeting, forecasting, variance analysis)
3. Use different audiences (CEO, Board, Finance Team)
4. Integrate with your financial data
5. Build custom models based on the framework

---

## Need Help?

📚 **Documentation:** See [README.md](README.md)

💬 **Questions:** Open an issue on [GitHub](https://github.com/skiddie007/FP-A-AI-Agent/issues)

📧 **Email:** skiddie007@github.com

---

**Happy Financial Planning! 🎯**
