import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": [], "include_files": ["database"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "BSPR",
        version = "0.9",
        description = "Badanie stałych paliw rakietowych.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("BSPR.py", base=base)])