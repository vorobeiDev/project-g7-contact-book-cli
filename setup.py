from cx_Freeze import setup, Executable


executable = Executable(script="app.py", target_name="g7cli.exe")

build_exe_options={
      "build_exe": "app"
}

setup(name="G7",
      version="0.1",
      description="Project G7 CLI Contact Book & Notes Bot",
      executables=[executable],
      options={"build_exe": build_exe_options})
