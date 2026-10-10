# Naukri Resume Auto Uploader

A Python + Playwright automation project that periodically updates a user's resume on their Naukri profile.

This project demonstrates practical experience with:

- Python automation
- Playwright browser automation
- Persistent browser sessions
- File upload automation
- Exception handling
- Logging
- Screenshot-based debugging
- Long-running automation processes

> **Important:** This project is intended for educational and portfolio purposes. Automating a third-party website may be subject to that website's Terms of Service and anti-automation policies. Review Naukri's current terms and policies before using this project.

## Features

- Automatically opens the Naukri profile page.
- Uses a persistent Chromium browser profile to maintain an existing login session.
- Uploads a configured resume file.
- Periodically repeats the upload operation.
- Configurable upload interval.
- Timestamped console logging.
- Captures screenshots after upload attempts.
- Captures screenshots when automation encounters an error.
- Does not require storing a Naukri username or password in source code.

## How It Works

The automation performs the following workflow:

```text
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
```

## Requirements

- Python 3.9+
- Playwright
- Chromium
- A Naukri account
- A resume file
- Permission to automate your own account

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pavan4912/naukri-resume-auto-uploader.git
cd naukri-resume-auto-uploader
```

### 2. Create a virtual environment

#### Windows

```cmd
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Chromium

```bash
playwright install chromium
```

## Configuration

Copy `.env.example.md` to `.env`.

### Windows

```cmd
copy .env.example.md .env
```

### macOS/Linux

```bash
cp .env.example.md .env
```

Update the values in `.env`.

Example:

```env
NAUKRI_URL=https://www.naukri.com/mnjuser/profile?id=&altresid
RESUME_PATH=C:\Users\YourName\Documents\resume.pdf
INTERVAL_MINUTES=60
TIMEOUT_MS=30000
BROWSER_PROFILE=./naukri_browser_profile
```

### Linux/macOS example

```env
RESUME_PATH=/home/username/Documents/resume.pdf
```

> **Security:** Never commit your `.env` file to GitHub. It is intentionally excluded through `.gitignore`.

## First-Time Login

The application uses a persistent Playwright browser profile.

On the first run:

1. Start the application.
2. Chromium opens.
3. Log into your Naukri account manually if required.
4. Complete any required verification manually.
5. The persistent browser profile stores the browser session locally.
6. Subsequent runs can reuse the stored session while it remains valid.
7. User need to restart the application **only for first time** after performing the above steps.

The browser profile is intentionally excluded from Git using `.gitignore`.

> **Never commit the browser profile to GitHub.** It may contain authentication and session information.

## Running the Application

Run:

```bash
python naukri_resume_uploader.py
```

Example console output:

```text
[2026-09-28 23:00:00] Naukri Resume Auto-Uploader started.
[2026-09-28 23:00:00] Resume: C:\Users\YourName\Documents\resume.pdf
[2026-09-28 23:00:00] Interval: 60 minutes
[2026-09-28 23:00:01] Starting resume upload...
[2026-09-28 23:00:04] Found resume upload element.
[2026-09-28 23:00:05] Resume file selected.
[2026-09-28 23:00:05] Clicking 'Update resume'...
[2026-09-28 23:00:10] Upload/update request completed.
```

## Screenshots

The application can create screenshots for verification and troubleshooting.

Example files:

```text
screenshots/upload_20260928_230010.png
screenshots/error_20260928_230500.png
```

Screenshots are excluded from the public repository by `.gitignore` because they may contain personal information.

If you want to showcase screenshots on GitHub, use screenshots that have been reviewed and anonymized.

## Project Structure

```text
naukri-resume-auto-uploader/
│
├── naukri_resume_uploader.py   # Main automation program
├── requirements.txt             # Python dependencies
├── .env.example                 # Example configuration
├── .gitignore                   # Prevents personal/sensitive files from being committed
├── LICENSE.txt                  # Project license
├── README.md                    # Project documentation
│
└── screenshots/
    └── .gitkeep
```

## Important Security Considerations

Do not commit any of the following:

- Resume files
- Browser profiles
- Cookies
- Authentication/session data
- `.env`
- Screenshots containing personal information
- Personal configuration files
- Passwords
- API keys
- Access tokens

The repository's `.gitignore` is configured to help prevent accidental commits of these files.

Before pushing changes, always check:

```bash
git status
```

and:

```bash
git diff --cached
```

## Limitations

Websites can change their HTML structure at any time.

For example, this project currently depends on selectors such as:

```css
#attachCV
```

and:

```css
input[type="button"][value="Update resume"]
```

If Naukri changes its frontend, these selectors may stop working.

The automation also depends on the user's browser session remaining valid.

## Responsible Use

This project should be used responsibly and only with accounts you are authorized to automate.

Do not use it to:

- Access another person's account
- Bypass authentication
- Circumvent security controls
- Evade anti-bot protections
- Upload someone else's private information
- Circumvent website restrictions

Users are responsible for complying with Naukri's current Terms of Service and applicable laws.

## Portfolio Value

This project demonstrates practical experience with:

- Python
- Playwright
- Browser automation
- Persistent browser contexts
- File upload automation
- Environment-based configuration
- Exception handling
- Logging
- Screenshot-based debugging
- Long-running processes

## License

This project is licensed under the MIT License. See [LICENSE.txt](LICENSE.txt).
