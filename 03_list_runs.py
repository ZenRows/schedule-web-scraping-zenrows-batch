import os
import sys
import requests

API = "https://async.api.zenrows.com/v1"
HEADERS = {"X-API-Key": os.environ["ZENROWS_API_KEY"]}
job_id = sys.argv[1]

runs = requests.get(f"{API}/jobs/{job_id}/runs", headers=HEADERS, timeout=30).json()["runs"]
for run in runs:
    stats = run["stats"]
    print(run["run_sequence"], run["trigger"], run["created_at"][:19], run["status"],
          f'{stats["successful"]}/{stats["total"]} pages, {stats["spend"]["credits"]} credits')
