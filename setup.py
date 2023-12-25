import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable_options = {
    "script": "app.py",
}

if sys.platform == "win32":
    executable_options["target_name"] = "g7cli.exe"
else:
    executable_options["target_name"] = "g7cli"

executable = Executable(**executable_options)

build_exe_options = {
    "build_exe": "app",
}

setup(
    name="G7",
    version="0.1",
    description="Project G7 CLI Contact Book & Notes Bot",
    executables=[executable],
    options={"build_exe": build_exe_options}
)