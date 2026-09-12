import re
import subprocess
from datetime import date
from pathlib import Path


def update_week_current(script: str, week_current: str):
    with open(script, 'r') as script_file:
        contents = script_file.read()

    updated_contents, replacements = re.subn(
        r'^weekCur\s*=.*$',
        f'weekCur = "{week_current}"',
        contents,
        count=1,
        flags=re.MULTILINE
    )

    if replacements != 1:
        raise RuntimeError(f"Could not update weekCur in {script}")

    with open(script, 'w') as script_file:
        script_file.write(updated_contents)


def move_atticus_comment(next_week: int):
    atticus_file = 'Atticus.html'
    with open(atticus_file, 'r') as html_file:
        lines = html_file.readlines()

    marker_index = next(
        (index for index, line in enumerate(lines)
         if line.startswith('<!--  <div class="dropdown">')),
        None
    )
    button_text = f'>Week {next_week:02d}</button>'
    button_index = next(
        (index for index, line in enumerate(lines) if button_text in line),
        None
    )

    if marker_index is None or button_index is None:
        raise RuntimeError(f"Could not move the Atticus comment before Week {next_week:02d}")

    dropdown_index = next(
        (index for index in range(button_index, -1, -1)
         if '<div class="dropdown">' in lines[index]),
        None
    )

    if dropdown_index is None:
        raise RuntimeError(f"Could not find the Week {next_week:02d} dropdown")

    lines[marker_index] = lines[marker_index].replace('<!--  ', '  ', 1)
    if not lines[dropdown_index].startswith('<!--  '):
        lines[dropdown_index] = '<!--  ' + lines[dropdown_index]

    with open(atticus_file, 'w') as html_file:
        html_file.writelines(lines)

# List of the files to run
scripts = [
    'HTML file generator/A1 generate.py',
    'HTML file generator/A2 generate.py',
	'HTML file generator/A3 generate.py',
    'HTML file generator/A4 generate.py',
    'HTML file generator/A5 generate.py'
    
]

today = date.today()
anchor_date = date(2026, 8, 10)
anchor_week = 1

if today < anchor_date:
    raise RuntimeError("The current date is before the project week anchor date")

week_number = anchor_week + (today - anchor_date).days // 7

run_type = input("Is this a new week or a correction? [new/correction]: ").strip().lower()
if run_type in {"new", "n"}:
    week_number += 1
elif run_type not in {"correction", "c"}:
    print("Aborted. Choose 'new' or 'correction'.")
    raise SystemExit

week_current = f"{week_number:02d}WEEK{today.year}"

target_files = [Path(week_current) / f"AT-D{day}.html" for day in range(1, 6)]
existing_files = [file for file in target_files if file.exists()]

if existing_files:
    print("The following files already exist:")
    for file in existing_files:
        print(f"- {file}")

    overwrite = input("Overwrite these files? [y/N]: ").strip().lower()
    if overwrite not in {"y", "yes"}:
        print("Aborted. No HTML files were overwritten.")
        raise SystemExit

# Update every generator before running any of them.
for script in scripts:
    update_week_current(script, week_current)

# Run each script one by one only after the week update succeeds everywhere.
all_succeeded = True
for script in scripts:
    print(f"\n--- Running {script} ---")
    result = subprocess.run(['python', script], capture_output=True, text=True)

    # Print the output
    print("Output: File Written")
    print(result.stdout)

    # Check for errors
    if result.stderr:
        print("Errors:")
        print(result.stderr)

    if result.returncode != 0:
        all_succeeded = False

if run_type in {"new", "n"} and all_succeeded:
    move_atticus_comment(week_number + 1)
elif run_type in {"new", "n"}:
    print("The Atticus menu was not updated because a generator failed.")