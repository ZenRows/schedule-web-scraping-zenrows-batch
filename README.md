# Schedule Web Scraping Without a Cron Server

## Description

This repo is the companion code for the tutorial [Schedule web scraping without a cron server](https://www.zenrows.com/blog/schedule-web-scraping). It uses [Zenrows Batch](https://docs.zenrows.com/batch/introduction) scheduled jobs to run a scraper every day at a set local time, every hour, on chosen weekdays or once, with no server or cron entry of your own. Every run is stored with a status and a result for each URL.

## Features

- A daily job at 9:00 New York time, with the timezone stored as an IANA name so daylight saving is handled for you
- An hourly job that extracts Hacker News titles, links and scores with `css_extractor`
- Listing every run of a job, with its trigger, status and credits
- A "what's new since the last run" diff built from each run's results
- Pausing, replacing and resuming a schedule
- Deleting a job and everything it stored

## Prerequisites

- Python 3.9+
- A Zenrows API key: [create a Zenrows account](https://app.zenrows.com/register)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ZenRows/schedule-web-scraping-zenrows-batch.git
   cd schedule-web-scraping-zenrows-batch
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The scripts read your key from the `ZENROWS_API_KEY` environment variable:

```bash
export ZENROWS_API_KEY=your_api_key   # Windows (PowerShell): $env:ZENROWS_API_KEY="your_api_key"
```

## Usage

```bash
python 01_daily_schedule.py            # creates the daily job, prints its id and next run (UTC)
python 02_hourly_schedule.py           # creates the hourly Hacker News job
python 03_list_runs.py JOB_ID          # lists every run of a job, newest first
python 04_whats_new.py JOB_ID          # downloads the latest run and prints what is new since last time
python 05_manage_schedule.py JOB_ID    # pauses, replaces and resumes a schedule
python 06_delete_job.py JOB_ID         # deletes a job, its runs and its results
```

Run `04_whats_new.py` after each run completes (or from a [completion webhook](https://docs.zenrows.com/academy/batch/webhooks)). It keeps what it has seen in `<JOB_ID>.seen.json`.

## Project structure

```
.
├── 01_daily_schedule.py    # Calendar schedule: every day at 09:00, America/New_York
├── 02_hourly_schedule.py   # Rate schedule: every hour, css_extractor on Hacker News
├── 03_list_runs.py         # GET /jobs/{id}/runs
├── 04_whats_new.py         # Diff the latest run against the previous one
├── 05_manage_schedule.py   # Pause, replace and resume a schedule
├── 06_delete_job.py        # DELETE /jobs/{id}
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Learn more

- [Scheduled jobs in the Batch API reference](https://docs.zenrows.com/batch/developer-guide-restapi#scheduled-jobs)
- [Run a Batch job on a schedule](https://docs.zenrows.com/academy/batch/scheduled-jobs)
- [Price scraping: track prices across retailers](https://www.zenrows.com/blog/price-scraping)
