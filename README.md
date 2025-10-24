# json2pdf

A universal, open-source tool that converts any JSON file into a beautiful, readable PDF — with automatic table detection and clean typography.

---

## 🚀 Features
- Converts any JSON (nested or flat) into a structured PDF.
- Automatically detects and formats lists of objects as tables.
- Clean, readable layout with professional typography.
- Works both as a **command-line tool (CLI)** and a **Python library**.
- Fully cross-platform (Windows, macOS, and Linux).

---

## 🧩 Setting Up Your Environment

Before installing dependencies, it’s a good practice to create a **virtual environment** to keep your project isolated and avoid conflicts.

### 🪟 **Windows Setup**

Open **PowerShell** or **Command Prompt**, then run:

```bash
# 1. Navigate to the project folder
cd path\to\json2pdf_package

# 2. Create a virtual environment named 'venv'
python -m venv venv

# 3. Activate the environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
When activated, your prompt should start with (venv) — that means you’re inside the virtual environment.

To deactivate it later:

bash
Copy code
deactivate
🍎 macOS / Linux Setup
Open your terminal and run:

bash
Copy code
# 1. Navigate to the project folder
cd path/to/json2pdf_package

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate the environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
Deactivate the environment anytime with:

bash
Copy code
deactivate
📦 Installation (Alternative)
If you prefer to install dependencies globally (not recommended), simply run:

bash
Copy code
pip install -r requirements.txt
🧰 Usage
🔹 Command Line
Convert JSON files directly from your terminal:

bash
Copy code
python -m json2pdf input.json output.pdf --title "My Report"
Or, if you installed it as a package:

bash
Copy code
json2pdf input.json output.pdf --title "My Report"
🔹 As a Python Library
Import and use it inside your own scripts:

python
Copy code
from json2pdf import json_to_pdf

data = {
    "project": "Demo",
    "results": [
        {"metric": "accuracy", "value": 0.98},
        {"metric": "precision", "value": 0.94}
    ]
}

json_to_pdf(data, "report.pdf", title="Example Report")
🧾 Requirements
Python ≥ 3.7

ReportLab ≥ 3.6

💡 Example
Input (data.json):

json
Copy code
{
  "Project": "AI Pricing Analysis",
  "Version": "1.2",
  "Costs": [
    {"Model": "GPT-4o", "Cost/1K Tokens ($)": 0.01},
    {"Model": "GPT-4o-mini", "Cost/1K Tokens ($)": 0.002}
  ]
}
Command:

bash
Copy code
python -m json2pdf data.json output.pdf --title "AI Pricing Report"
Output:
A clean, human-readable PDF with neatly formatted tables and sections.

🛠️ Troubleshooting
🧱 1. python or pip not recognized
Cause: Python is not added to your system PATH.
Fix:

Reinstall Python from python.org/downloads.

Make sure to check “Add Python to PATH” during installation.

Then reopen your terminal and try again:

bash
Copy code
python --version
pip --version
🧩 2. venv not found
Cause: The virtual environment module might not be installed.
Fix:

bash
Copy code
python -m ensurepip --upgrade
python -m pip install virtualenv
Then recreate your environment:

bash
Copy code
python -m venv venv
🧰 3. Permission denied or source: not found (macOS/Linux)
Fix:
Ensure the script is executable:

bash
Copy code
chmod +x venv/bin/activate
source venv/bin/activate
If using zsh or fish shell, adjust the command accordingly:

bash
Copy code
source venv/bin/activate.fish
🔒 4. pip install errors (SSL / connection issues)
Try upgrading pip and setuptools:

bash
Copy code
python -m pip install --upgrade pip setuptools
If still blocked, use:

bash
Copy code
pip install --trusted-host pypi.org --trusted-host pypi.python.org -r requirements.txt
🪶 5. PDF not generating or empty
Ensure the input JSON file is valid (use an online JSON validator).

Make sure the file path you pass exists.

Use absolute paths if your script runs from another directory.

Example:

bash
Copy code
python -m json2pdf "C:\Users\Admin\Desktop\data.json" "C:\Users\Admin\Desktop\report.pdf"
📝 License
MIT License — free for personal, academic, and commercial use.
Feel free to fork, modify, and share this tool.

👨‍💻 Author
Developed by Faisal Shouman
Open-source contribution and improvements are welcome!