import json
import os
import sys
import requests

API = "https://async.api.zenrows.com/v1"
HEADERS = {"X-API-Key": os.environ["ZENROWS_API_KEY"]}
job_id = sys.argv[1]

job = requests.get(f"{API}/jobs/{job_id}", headers=HEADERS, timeout=30).json()
run = job["latest_run"]
if run["status"] != "completed":
    sys.exit(f'run {run["run_sequence"]} is {run["status"]}, try again later')

# Results of the job's latest run. Each row links to the extracted JSON.
page = requests.get(f"{API}/jobs/{job_id}/results", headers=HEADERS,
                    params={"status": "successful"}, timeout=30).json()
current = {}
for row in page["results"]:
    data = requests.get(row["result_url"], timeout=60).json()
    current[row["external_id"]] = dict(zip(data["links"], data["titles"]))

seen_file = f"{job_id}.seen.json"
previous = json.load(open(seen_file)) if os.path.exists(seen_file) else {}
print(f'run {run["run_sequence"]} ({run["trigger"]}, {run["created_at"][:16]}Z): {run["stats"]["successful"]}/{run["stats"]["total"]} pages')
for page_id, stories in current.items():
    new = [title for link, title in stories.items() if link not in previous.get(page_id, {})]
    print(f"  {page_id}: {len(new)} new of {len(stories)}")
    for title in new[:3]:
        print(f"    + {title}")
json.dump(current, open(seen_file, "w"))
