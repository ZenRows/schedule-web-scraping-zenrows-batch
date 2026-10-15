import os
import sys
import requests

API = "https://async.api.zenrows.com/v1"
HEADERS = {"X-API-Key": os.environ["ZENROWS_API_KEY"]}
job_id = sys.argv[1]

# Removes the job, its schedule, its runs and its results.
r = requests.delete(f"{API}/jobs/{job_id}", headers=HEADERS, timeout=30)
print(r.status_code)
