import os
import platform
import getpass
import json

path = ""
if platform.system() == "Windows":
    path = r"C:\Users\%USERNAME%\SORA\modules\obj.json"
else:
    path = "~/SORA/modules/obj.json"

def project(pid):
    os.system(f"curl https://api.scratch.mit.edu/projects/{pid}/ > {path}")
    obj = open(f"/Users/{getpass.getuser()}/SORA/modules/obj.json", "r").read()
    src = json.loads(obj)
    token = src["project_token"]
    os.system(f"curl https://projects.scratch.mit.edu/{pid}?token={token} > {path}")
    obj = open(f"/Users/{getpass.getuser()}/SORA/modules/obj.json", "r").read()
    os.remove(f"/Users/{getpass.getuser()}/SORA/modules/obj.json")
    return obj
