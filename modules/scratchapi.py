import os
import json

#updated 'grabber.py'

# Load URLs.
def curl(url):
  os.system("echo "" > loadurl.json")
  os.system(f"sh loadurl.sh \"{url}\" > loadurl.json")
  loadurl = open("loadurl.json", "r").read()
  return loadurl

# List cloud vars. (Dict.)
def cloudvar(pid):
  raw = json.loads(curl(f"https://clouddata.scratch.mit.edu/logs?projectid={pid}&limit=100&offset=0"))
  var = {}
  for x in raw:
    try: var[x["name"]]
    except KeyError: var[x["name"]] = x["value"]
  return var

# Load project code.
def project(pid):
  token = json.loads(curl(f"https://api.scratch.mit.edu/projects/{pid}/"))["project_token"]
  obj = curl(f"curl https://projects.scratch.mit.edu/{pid}?token={token}")
  return obj