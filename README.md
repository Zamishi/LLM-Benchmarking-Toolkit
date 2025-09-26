# LLM-Benchmarking-Toolkit

**Python | PyQt5 | SymPy | OpenAI API | Gemini API**

---

## Overview

The **LLM Benchmarking Toolkit** is a Python-based research tool designed to **analyze and benchmark multiple large language models (LLMs)** such as OpenAI and Gemini. It supports **mathematical, coding, and textual problem-solving tasks** by integrating OCR and symbolic computation, providing a research-focused platform for **performance evaluation, comparison, and analysis**.

---

## Key Features

- **Dual LLM Comparison:** Evaluate how different LLMs perform on the same input.  
- **OCR Integration:** Extract text from images or screenshots for processing.  
- **Symbolic Computation:** Use SymPy for accurate mathematical problem handling.  
- **Research Interface:** Streamlined overlay interface to monitor and collect results efficiently.  
- **Extensible Framework:** Add new LLMs, datasets, or evaluation metrics as needed.

---

## Installation

1. Clone the repository:  
```bash
git clone https://github.com/yourusername/llm-benchmarking-toolkit.git
cd llm-benchmarking-toolkit
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure **Tesseract OCR** is installed and accessible in your PATH.

* Windows default: `C:\Program Files\Tesseract-OCR\tesseract.exe`
* Mac/Linux: install via your package manager.

4. Set your API keys (optional environment variables):

```bash
export OPENAI_API_KEY="your_openai_api_key"
export GEMINI_API_KEY="your_gemini_api_key"
```

---

## Usage

Run the main interface:

```bash
python main.py --debug
```

Optional flags:

* `--no-openai` : Disable OpenAI LLM
* `--no-gemini` : Disable Gemini LLM
* `--debug` : Save debug images and logs for research analysis

---

## Research Output

* Compare LLM responses on **math, coding, and textual tasks**.
* Export results to CSV/JSON for **accuracy analysis and evaluation**.
* Log performance metrics such as response time and solution correctness.

---

## Contributing

Contributions are welcome for:

* Adding new LLMs
* Improving benchmarking metrics
* Expanding example datasets for evaluation

---

## Intended Use

This toolkit is intended purely for **research, benchmarking, and learning purposes**.  
