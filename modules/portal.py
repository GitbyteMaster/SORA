import os
import platform

try:
  import scratchattach as scratch3
except ModuleNotFoundError:
  if platform.system() == "Windows":
    os.system("python -m install scratchattah")
  else:
    os.system("pip install scratchattach")
else:
  pass
