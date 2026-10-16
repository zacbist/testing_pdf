# PDF Extract

A local batch PDF text extractor built on pdfminer.six.

## How it works

1. Reads all PDF files from the `pdfs/` directory
2. Extracts text content from each using pdfminer.six
3. Collects results for further processing

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

## Contents

- `pdfs/` — PDF documents to process
- `main.py` — Extractor script
- `requirements.txt` — Dependencies
