import os
import platform
import getpass
import json

path = ""
if platform.system() == "Windows":
    path = r"C:\Users\%USERNAME%\SORA\modules\obj.json"
else:
    path = "~/SORA/modules/obj.json"

def curl(url):
    os.system(f"curl {url} > {path}")
    return open(f"/Users/{getpass.getuser()}/SORA/modules/obj.json", "r").read()
    
def project(pid):
    obj = curl(f"https://api.scratch.mit.edu/projects/{pid}/")
    src = json.loads(obj)
    token = src["project_token"]
    obj = curl(f"curl https://projects.scratch.mit.edu/{pid}?token={token}")
    os.remove(f"/Users/{getpass.getuser()}/SORA/modules/obj.json")
    return obj
