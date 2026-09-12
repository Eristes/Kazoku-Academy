This is Year 5 of the Kazoku Academy Project

Project on hold due to time constraints -Weekly updates still planned for video Links

## Weekly update workflow

`HTML file generator/run all.py` calculates project weeks from August 10, 2026, which is project week 1. The week advances every seven days.

When the runner starts:

- Choose `correction` to regenerate the current project week.
- Choose `new` to generate the next project week, which is useful when running early.
- Existing files in the selected week folder require explicit overwrite confirmation.
- The five generator scripts are updated to use the selected `weekCur` value before they run.
- When a new-week run completes successfully, the commented section in `Atticus.html` moves to hide the following week. Corrections leave it unchanged.

A redirect page for the current day and week has not been implemented yet.
