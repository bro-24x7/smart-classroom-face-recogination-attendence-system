import os
import subprocess

folder = "data"
if os.path.exists(folder):
    if os.name == "nt":
        os.startfile(folder)
    else:
        subprocess.Popen(["open", folder])
else:
    print("Data folder not found.")
