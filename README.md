# Basic-Keylogger
A web app that records keystrokes only with user consent and allows secure download or upload of the logs.


## Features

* Records keystrokes only after user consent.

* Provides buttons to Start, Stop, Clear, Download, and Upload logs.

* Logs are saved locally as JSON; optional upload requires admin token.

* Ethical demo — do not record others without consent.


## Commands to Run

* Create virtual environment: python -m venv venv

* Activate virtual environment (Windows): venv\Scripts\activate

* (Optional) Set admin token: set ADMIN_TOKEN=secret-demo-token

* Navigate to project folder: cd path\to\keystroke-demo

* Run the app: python app.py

* Open in browser: http://127.0.0.1:5000



## File Structure

keystroke-demo/
├── app.py
├── requirements.txt
└── templates/
    ├── base_home.html
    └── consent_logger.html



    


---
