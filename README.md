# json2pdf

A universal, open-source tool that converts any JSON file into a beautiful, readable PDF — with automatic table detection and clean typography.

## 🚀 Features
- Converts any JSON (nested or flat) into a structured PDF.
- Automatically detects and formats lists of objects as tables.
- Clean, readable layout.
- Works both as a **CLI** and a **Python library**.

## 📦 Installation
```bash
pip install -r requirements.txt
```

## 🧰 Usage

### Command Line
```bash
python -m json2pdf input.json output.pdf --title "My Report"
```
or after packaging:
```bash
json2pdf input.json output.pdf --title "My Report"
```

### As a Library
```python
from json2pdf import json_to_pdf

data = {"project": "Demo", "results": [{"metric": "accuracy", "value": 0.98}]}
json_to_pdf(data, "report.pdf", title="Example Report")
```

## 🧾 Requirements
- Python 3.7+
- reportlab >= 3.6

## 📝 License
MIT License — free for all uses.
