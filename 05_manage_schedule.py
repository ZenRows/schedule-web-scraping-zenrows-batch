import os
import sys
import requests

API = "https://async.api.zenrows.com/v1"
HEADERS = {"X-API-Key": os.environ["ZENROWS_API_KEY"]}
job_id = sys.argv[1]


def show(label):
    job = requests.get(f"{API}/jobs/{job_id}", headers=HEADERS, timeout=30).json()
    print(f'{label:<10} schedule={job["schedule"]} state={job["schedule_state"]}')


show("start")

# Pause or resume the schedule: no new runs fire while paused.
requests.post(f"{API}/jobs/{job_id}/schedule/state", headers=HEADERS,
              json={"schedule_state": "paused"}, timeout=30)
show("paused")

# Replace the schedule.
requests.put(f"{API}/jobs/{job_id}/schedule", headers=HEADERS,
             json={"rate": {"every": 2, "unit": "hour"}}, timeout=30)
show("replaced")

requests.post(f"{API}/jobs/{job_id}/schedule/state", headers=HEADERS,
              json={"schedule_state": "active"}, timeout=30)
show("resumed")
