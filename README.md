# Basic-Keylogger
A web app that records keystrokes only with user consent and allows secure download or upload of the logs.


Features

Records keystrokes only after user consent.

Buttons to Start, Stop, Clear, Download, and Upload logs.

Logs saved locally as JSON; optional upload requires admin token.

Ethical demo — do not record others without consent.


Commands to Run

# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment (Windows)
venv\Scripts\activate

# 3. (Optional) Set admin token
set ADMIN_TOKEN=secret-demo-token

# 4. Navigate to project folder
cd C:\Users\SRUSTHI\Desktop\keystroke_demo

# 5. Run the app
python app.py

# 6. Open in browser
http://127.0.0.1:5000



File Structure

keystroke-demo/
├── app.py
├── requirements.txt
└── templates/
    ├── base_home.html
    └── consent_logger.html



This is short, clear, and ready for your README.

If you want, I can combine this with a one-line project description to make the full README.
