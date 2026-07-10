# NovoHours — a tiny HH:MM adding machine

*Last updated: 2026-07-10*

A minimal PySide6 desktop app that keeps a running total of time. Type an
`HH` and `MM` value and hit `+` (or press Enter in the minutes box) to add it
to the total; prefix the hours with `-` to subtract. `Reset` clears the tally.
The result is shown as `±HH:MM`.

## Run from source

```powershell
python -m venv venv-win          # one time only
.\venv-win\Scripts\Activate.ps1
pip install -r requirements.txt  # or requirements-lock.txt for an exact set
python novohours.py
```

## Build the Windows executable

Ready-built binaries are attached to each [GitHub release](../../releases).
To build `novohours.exe` yourself (inside the activated venv):

```powershell
pyinstaller --clean --distpath . --specpath build --onefile novohours.py
Remove-Item -Recurse -Force build
```

## License

[MIT](LICENSE)
