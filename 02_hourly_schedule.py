import json
import os
import requests

API = "https://async.api.zenrows.com/v1"
HEADERS = {"X-API-Key": os.environ["ZENROWS_API_KEY"]}

selectors = {"titles": ".titleline > a", "links": ".titleline > a @href", "scores": ".score"}
job = {
    "type": "scheduled",
    "status": "closed",
    "name": "hn-front-page-hourly",
    "schedule": {"rate": {"every": 1, "unit": "hour"}},
    "zenrows_params": {"css_extractor": json.dumps(selectors)},
    "tasks": [
        {"url": "https://news.ycombinator.com/", "external_id": "hn-front"},
        {"url": "https://news.ycombinator.com/newest", "external_id": "hn-newest"},
    ],
}

created = requests.post(f"{API}/jobs", headers=HEADERS, json=job, timeout=30).json()
print(created)
