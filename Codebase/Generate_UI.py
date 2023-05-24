import os
import subprocess
from pathlib import Path

print("Generating Python Files from Designer Files...")

# Useful Paths:
python_path =  'D:/Facultate An 4/Licenta/PiCubeSolver/venv'
pyuic5 = f'"{python_path}/Scripts/pyuic5.exe"'
pyrcc5 = f'"{python_path}/Scripts/pyrcc5.exe"'
pyinstaller = f"{python_path}/Scripts/pyinstaller.exe"

command = f"{pyrcc5} GUI/Design/pixels.qrc -o GUI/GeneratedDesign/pixels_rc.py"

for file in os.listdir(Path(os.getcwd() + "/GUI/Design")):
    if file.endswith("ui"):
        filename = file.split(".")[0]
        print(f"Found file: {file}")
        command = command + f" && {pyuic5} GUI/Design/{filename}.ui -o GUI/GeneratedDesign/{filename}.py"
print(command)
try:
    print("Trying to Generate GUI Python Files:")
    result = subprocess.call(command, shell=True)
    if result == 0:
        print("DONE!!!")
except Exception as e:
    print(f"Exception: {e}")