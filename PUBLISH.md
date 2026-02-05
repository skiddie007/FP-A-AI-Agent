# 📦 PyPI Package Publishing Guide

## FP&A AI Agent - Publishing to PyPI (Python Package Index)

This guide will help you publish the FP&A AI Agent package to PyPI so users can install it using `pip`.

---

## ✅ Pre-Requisites

1. **Python 3.8+** installed
2. **Git** (to manage repository)
3. **PyPI Account** (free at https://pypi.org/account/register/)
4. **TestPyPI Account** (optional, for testing - https://test.pypi.org/account/register/)
5. **PyPI API Token** for authentication

---

## 📋 Step 1: Verify Package Files

Ensure your project has these files:

```
FP-A-AI-Agent/
├── setup.py              ✅ (Package configuration)
├── requirements.txt      ✅ (Dependencies)
├── README.md             ✅ (Long description)
├── fp_a_agent.py         ✅ (Main module)
├── LICENSE               ⏳ (Recommended)
└── MANIFEST.in           ⏳ (Optional)
```

---

## 🔧 Step 2: Install Build Tools

**On Windows (PowerShell):**
```powershell
pip install --upgrade pip setuptools wheel twine
```

**On Mac/Linux (Terminal):**
```bash
pip3 install --upgrade pip setuptools wheel twine
```

**What each tool does:**
- `setuptools` - Package creation
- `wheel` - Binary distribution format
- `twine` - Upload to PyPI securely

---

## 🏗️ Step 3: Build Distribution Files

Navigate to your project root (where setup.py is located):

**All Platforms:**
```bash
python setup.py sdist bdist_wheel
```

This creates:
- `dist/fp-a-ai-agent-1.0.0.tar.gz` (source distribution)
- `dist/fp-a-ai-agent-1.0.0-py3-none-any.whl` (wheel distribution)

**Verify the build:**
```bash
twine check dist/*
```

---

## 🔑 Step 4: Generate PyPI API Token

1. Go to https://pypi.org/account/
2. Log in with your account
3. Navigate to "Account settings" → "API tokens"
4. Click "Add API token"
5. Name it: `fp-a-ai-agent-token`
6. Copy the token (starts with `pypi-`)

⚠️ **IMPORTANT**: Save this token safely. You won't see it again!

---

## 🧪 Step 5: Test on TestPyPI (Recommended)

Before publishing to PyPI, test on TestPyPI:

**Upload to TestPyPI:**
```bash
twine upload --repository testpypi dist/*
```

**When prompted, enter:**
- Username: `__token__`
- Password: `<your-testpypi-token>`

**Test installation from TestPyPI:**
```bash
pip install --index-url https://test.pypi.org/simple/ fp-a-ai-agent
```

**Verify it works:**
```python
from fp_a_agent import run_fp_a_agent
print("✅ Package installed successfully!")
```

If successful, proceed to Step 6.

---

## 🚀 Step 6: Publish to PyPI

**Upload distribution files:**
```bash
twine upload dist/*
```

**When prompted, enter:**
- Username: `__token__`
- Password: `<your-pypi-token>`

**Expected output:**
```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading fp-a-ai-agent-1.0.0.tar.gz
Uploading fp-a-ai-agent-1.0.0-py3-none-any.whl
100% ════════════════════ 42.0/42.0 kB ✓
View at:
https://pypi.org/project/fp-a-ai-agent/1.0.0/
```

---

## ✅ Step 7: Verify Package on PyPI

1. Visit: https://pypi.org/project/fp-a-ai-agent/
2. You should see your package with version 1.0.0
3. Check that README and metadata display correctly

**Test real installation:**
```bash
pip install fp-a-ai-agent
```

**Verify installation:**
```python
from fp_a_agent import run_fp_a_agent
print(run_fp_a_agent("Test prompt", audience="CEO"))
```

---

## 📝 Step 8: Update Version for Next Release

For future releases, update the version:

**In setup.py:**
```python
version="1.1.0",  # Increment version
```

**Tag in Git:**
```bash
git tag v1.1.0
git push origin v1.1.0
```

**Create GitHub Release:**
- Go to https://github.com/skiddie007/FP-A-AI-Agent/releases/new
- Create release with tag v1.1.0
- Add release notes
- Publish

**Then rebuild and upload:**
```bash
rm -rf dist build *.egg-info  # Clean old builds
python setup.py sdist bdist_wheel
twine upload dist/*
```

---

## 🔐 Security Best Practices

✅ **DO:**
- Use API tokens instead of passwords
- Keep tokens in secure location (not in git)
- Use `.pypirc` file for credentials:

```bash
# ~/.pypirc (Linux/Mac) or %APPDATA%\.pypirc (Windows)
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: __token__
password: pypi-AgEIcHlwaS5vcmc...

[testpypi]
repository: https://test.pypi.org/legacy/
username: __token__
password: pypi-AgEIcHlwaS5vcmc...
```

Then upload simply as:
```bash
twine upload dist/*
```

❌ **DON'T:**
- Commit API tokens to git
- Share tokens in emails or messages
- Use passwords (use API tokens instead)
- Publish test versions to main PyPI

---

## 🐛 Troubleshooting

### Error: "Invalid distribution"
```bash
# Solution: Rebuild distribution
rm -rf dist build *.egg-info
python setup.py sdist bdist_wheel
twine check dist/*
```

### Error: "401 Unauthorized"
```bash
# Solution: Check API token
# Make sure token starts with 'pypi-'
# Verify token hasn't expired
# Try using ~/.pypirc file
```

### Error: "Filename already exists"
```bash
# Solution: Increment version number
# Each release needs a unique version
setup.py: version="1.0.1"  # Bump version
```

### Package installed but import fails
```bash
# Solution: Check package name
from fp_a_agent import run_fp_a_agent  # ✅ Correct
# Note: PyPI package name is 'fp-a-ai-agent'
# But import is 'fp_a_agent' (underscores)
```

---

## 📊 Package Statistics

Once published, track your package:

- **PyPI Page**: https://pypi.org/project/fp-a-ai-agent/
- **Downloads**: https://pypistats.org/packages/fp-a-ai-agent
- **GitHub Stars**: https://github.com/skiddie007/FP-A-AI-Agent

---

## 🎯 Success Checklist

- ✅ Package created successfully
- ✅ Tested on TestPyPI
- ✅ Published to PyPI
- ✅ Package installed via `pip install fp-a-ai-agent`
- ✅ Import works: `from fp_a_agent import run_fp_a_agent`
- ✅ PyPI page is live and visible
- ✅ README displays correctly
- ✅ All metadata is accurate

---

## 📚 Additional Resources

- **PyPI**: https://pypi.org/
- **Packaging Guide**: https://packaging.python.org/
- **Twine Docs**: https://twine.readthedocs.io/
- **Setuptools Docs**: https://setuptools.pypa.io/

---

## 🎉 Congratulations!

Your FP&A AI Agent is now available for download via:

```bash
pip install fp-a-ai-agent
```

Users worldwide can now easily install and use your package! 🚀
