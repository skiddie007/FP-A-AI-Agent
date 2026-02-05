from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fp-a-ai-agent",
    version="1.0.0",
    author="skiddie007",
    author_email="skiddie007@github.com",
    description="CFO-Grade Financial Planning & Analysis AI Agent powered by OpenAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skiddie007/FP-A-AI-Agent",
    project_urls={
        "Bug Tracker": "https://github.com/skiddie007/FP-A-AI-Agent/issues",
        "Documentation": "https://github.com/skiddie007/FP-A-AI-Agent#readme",
        "Source Code": "https://github.com/skiddie007/FP-A-AI-Agent",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.3.0",
        "python-dotenv>=0.19.0",
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "fp-a-agent=fp_a_agent:main",
        ],
    },
    keywords=["financial planning", "FP&A", "AI agent", "CFO", "OpenAI", "finance", "forecasting"],
    include_package_data=True,
    zip_safe=False,
)
