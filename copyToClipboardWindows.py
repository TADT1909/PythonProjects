#Work only on Windows OS
# https://stackoverflow.com/questions/41029997/copy-string-to-clipboard-natively-python-3
import subprocess
txt = "Save to clipboard!"
subprocess.run(['clip.exe'], input=txt.strip().encode('utf-16'), check=True)