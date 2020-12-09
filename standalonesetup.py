import cx_Freeze

executables = [cx_Freeze.Executable("pyfighter.py", base = "Win32GUI", icon="graphics/logo/logo.ico")]

# Run python standalonesetup.py bdist_msi

cx_Freeze.setup(
        name="PyFighter",
        version="1.0.0",
        description="Pyfighter is an 8-bit side scrolling, infinite level platform game, produced in python using PyGame as part on an MSc by R. Soane, R. Danevicius, and S. Mistry.  Inspired by super street fighter, super smash bros and Mario, they created a customisable and addictive game that gets progressively harder.",
        author="R. Soane, R. Danevicius, S. Mistry",
        options={
            "build_exe": {"packages":["pygame"],
            "include_files":["audio", "json", "other_data","graphics"]
        }},
        executables = executables
        )