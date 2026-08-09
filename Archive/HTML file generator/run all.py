import subprocess

# List of the files to run
scripts = [
    'HTML file generator/A1 generate.py',
    'HTML file generator/A2 generate.py',
	'HTML file generator/A3 generate.py',
    'HTML file generator/A4 generate.py',
    'HTML file generator/A5 generate.py',
    'HTML file generator/J1 generate.py',
	'HTML file generator/J2 generate.py',
    'HTML file generator/J3 generate.py',
	'HTML file generator/J4 generate.py',
	'HTML file generator/J5 generate.py'
    
]

# Run each script one by one
for script in scripts:
    print(f"\n--- Running {script} ---")
    result = subprocess.run(['python', script], capture_output=True, text=True)

    # Print the output
    print("Output:")
    print(result.stdout)

    # Check for errors
    if result.stderr:
        print("Errors:")
        print(result.stderr)