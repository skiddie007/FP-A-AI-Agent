# 💻 LOCAL DEVELOPMENT SETUP - FP&A AI Agent

**Complete step-by-step guide to run the FP&A AI Agent on your Windows/Mac/Linux machine**

---

## 📋 Prerequisites

Before starting, ensure you have:

- **Python 3.8+** installed
- **Git** installed
- **OpenAI API Key** (get from https://platform.openai.com/api-keys)
- **Text Editor or IDE** (VS Code, PyCharm, Sublime, etc.)
- **Terminal/Command Prompt** access

### Check Python Installation

**Windows (Command Prompt or PowerShell):**
```cmd
python --version
pip --version
```

**Mac/Linux (Terminal):**
```bash
python3 --version
pip3 --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

---

## 🚀 COMPLETE SETUP (10 Minutes)

### STEP 1️⃣: Clone the Repository

**On Windows (PowerShell):**
```powershell
# Navigate to where you want the project
cd Desktop  # or any folder

# Clone the repository
git clone https://github.com/skiddie007/FP-A-AI-Agent.git

# Enter the project directory
cd FP-A-AI-Agent

# Verify files exist
dir  # You should see: fp_a_agent.py, requirements.txt, README.md, QUICKSTART.md
```

**On Mac/Linux (Terminal):**
```bash
# Navigate to where you want the project
cd Desktop  # or any folder

# Clone the repository
git clone https://github.com/skiddie007/FP-A-AI-Agent.git

# Enter the project directory
cd FP-A-AI-Agent

# Verify files exist
ls  # You should see: fp_a_agent.py, requirements.txt, README.md, QUICKSTART.md
```

✅ **Expected Output:**
You should see these files in the FP-A-AI-Agent folder:
```
├── fp_a_agent.py         # Main FP&A Agent
├── requirements.txt      # Dependencies
├── README.md            # Full documentation
├── QUICKSTART.md        # Quick guide
└── LOCAL_SETUP.md       # This file
```

---

### STEP 2️⃣: Create Virtual Environment (Recommended)

A virtual environment isolates project dependencies.

**On Windows (PowerShell):**
```powershell
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# You should see (venv) at the start of each line
```

**On Windows (Command Prompt):**
```cmd
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate.bat
```

**On Mac/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# You should see (venv) at the start of each line
```

✅ **Verification:** Your terminal should show `(venv)` prefix

---

### STEP 3️⃣: Install Dependencies

**All Platforms (with virtual environment activated):**
```bash
pip install -r requirements.txt
```

**What gets installed:**
- `openai` - OpenAI API client
- `python-dotenv` - Environment variable management
- `pandas` - Data processing
- `numpy` - Numerical computations
- `requests` - HTTP library

**Expected Output:**
```
Successfully installed openai python-dotenv pandas numpy requests
```

✅ **Verification:**
```bash
pip list
```
You should see all packages listed.

---

### STEP 4️⃣: Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign in with your OpenAI account (create if needed)
3. Click **"Create new secret key"**
4. Copy the key (it starts with `sk-`)
5. **Save it safely** - you can't see it again!

⚠️ **IMPORTANT:** Never commit this key to GitHub or share it.

---

### STEP 5️⃣: Create .env File

Create a file named `.env` in your project root with your API key.

**On Windows (PowerShell):**
```powershell
# Create .env file
@'
OPENAI_API_KEY=sk-your-actual-key-here
'@ | Out-File -FilePath .env -Encoding UTF8

# Verify it was created
cat .env
```

**On Windows (Command Prompt):**
```cmd
# Create .env file
echo OPENAI_API_KEY=sk-your-actual-key-here > .env

# Verify it was created
type .env
```

**On Mac/Linux:**
```bash
# Create .env file
echo "OPENAI_API_KEY=sk-your-actual-key-here" > .env

# Verify it was created
cat .env
```

✅ **Expected Output:**
```
OPENAI_API_KEY=sk-your-actual-key-here
```

⚠️ **SECURITY:** Add `.env` to `.gitignore` (already recommended):
```bash
echo ".env" >> .gitignore
```

---

### STEP 6️⃣: Run a Test Script

Create a test file to verify everything works.

**Create `test_agent.py` in your project root:**

```python
#!/usr/bin/env python3
"""
Test script for FP&A AI Agent
Runs 3 example use cases
"""

from fp_a_agent import run_fp_a_agent

print("\n" + "="*80)
print("FP&A AI AGENT - LOCAL SETUP TEST")
print("="*80 + "\n")

# Example 1: SaaS Financial Planning
print("[TEST 1/3] SaaS Growth Planning...\n")
prompt_1 = """
Series B SaaS startup:
- ARR: $8M
- Monthly burn: $250k
- Monthly churn: 2%
- Goal: $20M ARR in 3 years

Provide 3-year FP&A roadmap with key KPIs and risks.
"""

try:
    response_1 = run_fp_a_agent(prompt_1, audience="CEO")
    print(response_1)
    print("\n✅ Test 1 PASSED\n")
except Exception as e:
    print(f"❌ Test 1 FAILED: {str(e)}\n")

# Example 2: Manufacturing Cost Optimization
print("\n" + "="*80)
print("[TEST 2/3] Manufacturing Cost Analysis...\n")
prompt_2 = """
Manufacturing company:
- Revenue: $50M annually
- COGS: 60% of revenue
- Capacity utilization: 75%
- Goal: Improve margins by 5%

What are concrete cost optimization recommendations?
"""

try:
    response_2 = run_fp_a_agent(prompt_2, audience="Finance Team")
    print(response_2)
    print("\n✅ Test 2 PASSED\n")
except Exception as e:
    print(f"❌ Test 2 FAILED: {str(e)}\n")

# Example 3: Retail Expansion
print("\n" + "="*80)
print("[TEST 3/3] Retail Expansion Planning...\n")
prompt_3 = """
Retail chain:
- Current stores: 50
- Same-store sales growth: 2% YoY
- Gross margin: 35%
- Plan: Expand to 75 stores in 2 years

Analyze financial impact and capital requirements.
"""

try:
    response_3 = run_fp_a_agent(prompt_3, audience="Board")
    print(response_3)
    print("\n✅ Test 3 PASSED\n")
except Exception as e:
    print(f"❌ Test 3 FAILED: {str(e)}\n")

print("\n" + "="*80)
print("✅ ALL TESTS COMPLETED")
print("="*80)
```

**Run the test:**

**Windows:**
```powershell
python test_agent.py
```

**Mac/Linux:**
```bash
python3 test_agent.py
```

✅ **Success Indicators:**
- Tests run without errors
- You see detailed FP&A analysis for each prompt
- Output includes Executive Summary, Key Insights, Financial Impact

---

### STEP 7️⃣: Try Your Own Queries

Create `my_queries.py` and experiment:

```python
from fp_a_agent import run_fp_a_agent

# Your custom financial question
my_prompt = """
Your company/industry description here...
Your specific financial question...
"""

# Choose audience: "CEO", "Board", "Finance Team", "Operations"
response = run_fp_a_agent(my_prompt, audience="CEO")
print(response)
```

**Run it:**
```bash
python my_queries.py
```

---

## 🛠️ Common Issues & Solutions

### ❌ Error: "Module 'openai' not found"

**Cause:** Dependencies not installed

**Solution:**
```bash
# Ensure virtual environment is activated
# Then reinstall
pip install -r requirements.txt

# Or manually
pip install openai python-dotenv pandas numpy requests
```

---

### ❌ Error: "OPENAI_API_KEY not set"

**Cause:** .env file missing or incorrect format

**Solution:**
```bash
# Check if .env exists
ls -la .env  # Mac/Linux
dir .env    # Windows

# Verify contents (should NOT start with echo or output)
cat .env    # Mac/Linux
type .env   # Windows

# Recreate if needed:
echo "OPENAI_API_KEY=sk-your-key" > .env
```

---

### ❌ Error: "Invalid API key"

**Cause:** Wrong API key format or expired key

**Solution:**
1. Go to https://platform.openai.com/api-keys
2. Create a NEW key (old ones may have been revoked)
3. Update .env with the new key
4. Restart your terminal

---

### ❌ Error: "timeout" or "connection error"

**Cause:** Network issue or API overloaded

**Solution:**
```bash
# Try again after a few seconds
# Or use faster model (gpt-4-mini)

# Edit fp_a_agent.py line 174:
model="gpt-4-mini",  # Instead of gpt-4-turbo
```

---

### ❌ Error: "Insufficient quota"

**Cause:** OpenAI account out of credits

**Solution:**
1. Check billing: https://platform.openai.com/account/billing/overview
2. Add payment method
3. Check usage limits

---

## 📁 Project Structure

```
FP-A-AI-Agent/
├── fp_a_agent.py        # Main agent (DO NOT EDIT)
├── requirements.txt     # Dependencies (DO NOT EDIT)
├── README.md           # Full docs
├── QUICKSTART.md       # Quick guide
├── LOCAL_SETUP.md      # This file
├── .env               # YOUR API KEY (CREATE THIS)
├── venv/              # Virtual environment (CREATED BY YOU)
├── test_agent.py      # Test script (OPTIONAL, CREATE THIS)
└── my_queries.py      # Your queries (OPTIONAL, CREATE THIS)
```

---

## 🚀 Next Steps After Setup

✅ **Setup Complete!** Now:

1. **Read README.md** for detailed capabilities
2. **Try different industries** (Manufacturing, Retail, SaaS, etc.)
3. **Use different audiences** (CEO, Board, Finance Team, Operations)
4. **Integrate with your data** (CSV, Excel, SQL)
5. **Build custom models** based on the framework
6. **Automate workflows** in your organization

---

## 📞 Support

**Issues?**
- Check GitHub: https://github.com/skiddie007/FP-A-AI-Agent/issues
- Review README.md troubleshooting section
- Verify .env file and API key

**Questions?**
- Read QUICKSTART.md for examples
- Check README.md for detailed documentation

---

## ✨ Success Checklist

- [ ] Python 3.8+ installed
- [ ] Git installed
- [ ] Repository cloned
- [ ] Virtual environment created & activated
- [ ] Dependencies installed (`pip list` shows all packages)
- [ ] OpenAI API key obtained
- [ ] .env file created with API key
- [ ] test_agent.py created and runs successfully
- [ ] All 3 tests pass without errors
- [ ] You see detailed financial analysis output

---

**You're all set! Happy Financial Planning! 🎯**
