from cx_Freeze import setup, Executable

base = None    

executables = [Executable("cv.py", base=base)]

packages = ["idna","sys","tkinter","PIL","datetime"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "cvmakerr",
    options = options,
    version = "0.1",
    description = 'cretes pdf of cv',
    executables = executables
)
