import os
import platform
import getpass
import json
import shutil
import requests

path = ""
if platform.system() == "Windows":
    path = r"C:\Users\%USERNAME%\soraobj.json"
else:
    path = "~/soraobj.json"

def curl(url):
    os.system(f"curl {url} > {path}")
    return open(f"/Users/{getpass.getuser()}/soraobj.json", "r").read()
    
def project(pid):
    obj = curl(f"https://api.scratch.mit.edu/projects/{pid}/")
    src = json.loads(obj)
    token = src["project_token"]
    obj = curl(f"curl https://projects.scratch.mit.edu/{pid}?token={token}")
    return obj

def loadimage(url, as_file):
    # https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
    response = requests.get(url, stream=True)
    open(as_file, "a")
    with open(as_file, 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    del response

