import os
import requests

API = "https://async.api.zenrows.com/v1"
HEADERS = {"X-API-Key": os.environ["ZENROWS_API_KEY"]}

job = {
    "type": "scheduled",
    "status": "closed",
    "name": "daily-price-check",
    "schedule": {
        "calendar": {"times_of_day": ["09:00"], "cadence": {"daily": {}}},
        "timezone": "America/New_York",
    },
    "zenrows_params": {"mode": "auto"},
    "tasks": [
        {"url": "https://www.scrapingcourse.com/ecommerce/product/abominable-hoodie/", "external_id": "hoodie"},
        {"url": "https://www.scrapingcourse.com/ecommerce/product/adrienne-trek-jacket/", "external_id": "jacket"},
    ],
}

created = requests.post(f"{API}/jobs", headers=HEADERS, json=job, timeout=30).json()
job_id = created["job_id"]

details = requests.get(f"{API}/jobs/{job_id}", headers=HEADERS, timeout=30).json()
print(job_id, details["schedule_state"], details["next_scheduled_run"])
