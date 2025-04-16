# NSE Data Scraper

This script fetches equity stock indices data from the NSE website using Selenium to acquire session cookies, then uses `requests` to retrieve the data from the public API.

## Files
- `scraper.py`: Main Python script for scraping.
- `cookies.json`: Output file containing session cookies.
- `requirements.txt`: Python package dependencies.

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/nse-data-scraper.git
cd data_scraper
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download Chromedriver
Make sure you download the correct version of [Chromedriver](https://chromedriver.chromium.org/downloads) and place it in the root directory.

### 4. Run the script
```bash
python scraper.py
```
