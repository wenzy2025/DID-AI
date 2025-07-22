# DID-AI

**DID-AI** is an open-source toolkit that empowers researchers with automated Difference-in-Differences (DID) analysis. It combines convenient Python utilities with LLM powered result summaries.

## 🌟 Key Features

- 📊 One-click DID estimation from raw data
- 🧠 Natural language interpretation of regression results
- 📈 Automated parallel trend & placebo tests
- ✍️ Paper-ready methods and results writeup (in Markdown/LaTeX)
- 📁 Easy CSV/Excel data upload interface

## 🔧 Technologies

- Python (pandas, statsmodels)
- Streamlit (UI)
- DeepSeek API / OpenAI API (LLM integration)

## 📦 Getting Started

```bash
pip install -r requirements.txt
python src/main.py sample_data/did_example_data.csv --outcome outcome --treatment treated --time time
```

## Repository Structure

```
DID-AI/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py             # Application entry point
│   ├── did_model.py        # DID estimation utilities
│   ├── placebo_test.py     # Placebo test implementation
│   ├── trend_test.py       # Parallel trend check
│   ├── llm_writer.py       # LLM result summarizer
│   └── utils.py            # Helper functions
├── notebooks/
│   └── example_did_analysis.ipynb
├── prompts/
│   └── result_interpretation_prompt.md
└── sample_data/
    └── did_example_data.csv
```
