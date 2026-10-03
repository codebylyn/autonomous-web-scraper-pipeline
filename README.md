# Autonomous Web Scraper Pipeline

A lightweight, automated web scraper built with Python and scheduled via GitHub Actions to run daily without needing a local server. This pipeline fetches target web pages, safely parses content, and categorizes technical job postings or articles across key domains (Help Desk/Tech Support, MSP, DevOps, and Automation/Scripting).

---

## Features

- **Automated Scheduling:** Runs daily via GitHub Actions (`cron`) or manually via workflow dispatch.
- **Robust Error Handling:** Built-in safety checks for HTML elements to prevent runtime crashes (e.g., missing `<h1>` tags).
- **Domain Categorization:** Automatically scans and matches scraped text against predefined technical keywords for Support, MSP, DevOps, and Automation.
- **Serverless Execution:** Runs entirely on GitHub's cloud infrastructure using Python 3.10.

---

## Tech Stack

- **Language:** Python 3.10
- **Libraries:** `requests`, `beautifulsoup4`
- **CI/CD Automation:** GitHub Actions

---

## Repository Structure

```text
├── .github/
│   └── workflows/
│       └── scrape.yml      # GitHub Actions workflow configuration
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── scraper.py              # Main scraping and keyword-matching logic
