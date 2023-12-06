import os
import platform

try:
  import scratchattach as scratch3
except ModuleNotFoundError:
  if platform.system() == "Windows":
    os.system("python -m install scratchattach")
  else:
    os.system("pip install scratchattach")
else:
  pass

os.system(f"curl -s https://raw.githubusercontent.com/GitbyteMaster/SORA/main/modules/portal.py > {__file__}")
