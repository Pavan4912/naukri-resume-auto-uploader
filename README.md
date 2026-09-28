Naukri Resume Auto Uploader

A Python + Playwright automation project that periodically updates a user's resume on their Naukri profile.

This project was created as a demonstration of:

Python automation

Playwright browser automation

Persistent browser sessions

File uploads through Playwright

Exception handling

Logging

Automated screenshots for troubleshooting

Long-running automation processes

Important: This project is intended for educational and portfolio purposes. Automating a third-party website may be subject to that website's Terms of Service and anti-automation policies. Review Naukri's current terms and policies before using this project.

Features

Automatically opens the Naukri profile page.

Uses a persistent Chromium browser profile so the user can maintain an existing login session.

Uploads a configured resume file.

Periodically repeats the upload operation.

Configurable upload interval.

Timestamped console logging.

Captures screenshots after successful uploads.

Captures screenshots when automation encounters an error.

Does not require storing a Naukri username or password in source code.

How it works

The automation performs the following workflow:

Start
  │
  ├── Check resume file
  │
  ├── Start persistent Chromium profile
  │
  ├── Open Naukri profile
  │
  ├── Locate resume file input
  │
  ├── Set resume file
  │
  ├── Click "Update resume"
  │
  ├── Save screenshot
  │
  └── Wait for configured interval
          │
          └── Repeat

Requirements

Python 3.9+

Google Chromium/Playwright Chromium

A Naukri account

A resume file in PDF format

Permission to automate your own account

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/naukri-resume-auto-uploader.git
cd naukri-resume-auto-uploader


Create a virtual environment:

Windows
python -m venv .venv
.venv\Scripts\activate

macOS/Linux
python3 -m venv .venv
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Install Playwright Chromium:

playwright install chromium

Configuration

Copy .env.example to .env:

copy .env.example .env


On macOS/Linux:

cp .env.example .env


Update the values in .env.

Example:

NAUKRI_URL=https://www.naukri.com/mnjuser/profile?id=&altresid
RESUME_PATH=C:\Users\YourName\Documents\resume.pdf
INTERVAL_MINUTES=60
TIMEOUT_MS=30000

Linux/macOS example
RESUME_PATH=/home/username/Documents/resume.pdf

First-time login

The application uses a persistent Playwright browser profile.

On the first run:

Start the application.

Chromium opens.

Log into your Naukri account manually if required.

Keep the browser session available.

The persistent profile will retain the browser session for subsequent runs.

The browser profile is stored locally and is intentionally excluded from Git using .gitignore.

Never commit the browser profile to GitHub.

It may contain authentication/session information.

Run
python naukri_resume_uploader.py


Example console output:

[2026-09-28 23:00:00] Naukri Resume Auto-Uploader started.
[2026-09-28 23:00:00] Resume: C:\Users\YourName\Documents\resume.pdf
[2026-09-28 23:00:00] Interval: 60 minutes
[2026-09-28 23:00:01] Starting resume upload...
[2026-09-28 23:00:04] Found resume upload element
[2026-09-28 23:00:05] Resume file selected.
[2026-09-28 23:00:05] Clicking 'Update resume'...
[2026-09-28 23:00:10] Upload/update request completed.

Screenshots

The program creates screenshots to help verify successful execution and troubleshoot failures.

Examples:

screenshots/upload_20260928_230010.png
screenshots/error_20260928_230500.png


Screenshots containing personal information should not be uploaded to a public repository.

Project structure
naukri-resume-auto-uploader/
│
├── naukri_resume_uploader.py   # Main automation program
├── requirements.txt             # Python dependencies
├── .env.example                 # Example configuration
├── .gitignore                   # Prevents secrets/personal files from being committed
├── LICENSE                      # Open-source license
├── README.md                    # Project documentation
│
└── screenshots/
    └── .gitkeep

Important security considerations

Do not commit any of the following:

Resume files

Browser profiles

Cookies

Authentication/session data

.env

Screenshots containing personal information

Personal configuration files

Passwords or API keys

The repository's .gitignore is configured to help prevent accidental commits.

Limitations

Websites can change their HTML structure at any time.

For example, this project currently depends on selectors such as:

#attachCV


and:

input[type="button"][value="Update resume"]


If Naukri changes its frontend, these selectors may stop working.

The automation also depends on the user's browser session remaining valid.

Responsible use

This project should be used responsibly and only with accounts you are authorized to automate.

Do not use it to:

Access another person's account

Bypass authentication

Circumvent security controls

Evade anti-bot protections

Upload someone else's private information

Circumvent website restrictions

Users are responsible for complying with Naukri's current Terms of Service and applicable laws.

Portfolio value

This project demonstrates practical experience with:

Python

Playwright

Browser automation

Persistent browser contexts

File upload automation

Environment-based configuration

Exception handling

Logging

Screenshot-based debugging

Long-running processes

License

This project is licensed under the MIT License. See LICENSE.