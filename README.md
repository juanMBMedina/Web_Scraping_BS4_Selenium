# Web_Scraping_BS4_Selenium

![python](https://img.shields.io/badge/python-3.8%2B-blue)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

Elegant, minimal web-scraping pipeline using Selenium + BeautifulSoup to
extract product and instalment data (example target: Mercado Libre).

**Repository**: `https://github.com/juanMBMedina/Web_Scraping_BS4_Selenium`

---

## **Quick Start**
- **Clone** the repo and create a virtual environment, then install deps:

```bash
git clone https://github.com/juanMBMedina/Web_Scraping_BS4_Selenium.git
cd Web_Scraping_BS4_Selenium
# Windows PowerShell
py -m venv venv; .\venv\Scripts\Activate.ps1
# Linux / macOS
# py -m venv venv
# source venv/bin/activate
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

---

#**Run the extraction (example)**

```bash
py -m runners.runner
```

CSV outputs are stored in the `output_data/` folder and logs are written to
`logs/`.

---

##**Features**
- **Selenium navigation** with a small browser helper in `navigation/browser.py`.
- **BeautifulSoup parsers** in `extract/` for page parsing and model mapping.
- **Transform & load** steps produce cleaned CSVs under `output_data/`.

---

##**Installation Notes (Windows & Linux)**
- Windows PowerShell: activate virtualenv with `.\venv\Scripts\Activate.ps1`.
- Windows cmd: `venv\Scripts\activate`.
- Linux/macOS or Git Bash: `source venv/bin/activate`.
- If you plan to run the notebook: `py -m pip install jupyter`.

---

##**Environment Configuration (environment variables)**

The project uses `python-dotenv` (loaded in `navigation/browser.py`). Create a
`.env` file in the project root to override runtime behavior. Example:

```ini
# .env (example - do NOT commit secrets)
HEADLESS=True
USER_AGENT=
WINDOW_SIZE=1920,1080
```

- `HEADLESS`: `True` or `False` (string, case-sensitive). Default: `True`.
- `USER_AGENT`: optional user agent string used when headless. Leave empty to
  fall back to the browser default (recommended for testing).
- `WINDOW_SIZE`: `WIDTH,HEIGHT` (used in headless mode). Default: `1920,1080`.

Behavior notes:
- `HEADLESS` is evaluated as `os.getenv("HEADLESS", "True") == "True"`.
- When `HEADLESS=False`, the driver starts with `--start-maximized`.
- If `USER_AGENT` is empty, the code currently still builds the
  `--user-agent=` argument; setting `USER_AGENT` to an empty string avoids
  passing `None`.

Useful: copy a real agent from [What is my User Agent](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)

---

##**Project Layout**
- `extract/` — extractors and helpers
  - `extract/meli/` — Mercado Libre specific extractor and models
- `pages/` — page models used by Selenium navigation
- `navigation/` — browser launcher and navigation helpers (see `browser.py`)
- `transform/` — cleaning/normalization and schemas
- `load/` — CSV loader (`load/csv_loader.py`)
- `runners/` — orchestration scripts (`runners/runner.py`)
- `output_data/` — CSV outputs
- `logs/` — runtime log files
- `web_scraping_meli.ipynb` — interactive notebook

---

##**Troubleshooting & Tips**
- If Selenium fails to start, ensure a compatible browser (Chrome) is
  installed and `webdriver-manager` can download the matching driver.
- If PowerShell blocks script activation, run as administrator and execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- Consider setting `HEADLESS=False` during development to see the browser.

---

##**Contributing**
- PRs and issues welcome. Keep changes focused and add tests where possible.

---
##**License**

This project is released under the MIT License — see the `LICENSE` file
included in the repository for full terms.

---

If you'd like, I can also:
- run `py -m runners.runner` locally to verify the Quick Start steps; or
- update `navigation/browser.py` to avoid adding the `--user-agent=` option
  when `USER_AGENT` is empty (safer default).

Tell me which follow-up you'd like.
