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
pyinstaller --clean --distpath . --onefile --windowed --icon "gui/novohours.ico" --add-data "gui;gui" novohours.py
Remove-Item -Recurse -Force build, novohours.spec
```

`--add-data "gui;gui"` bundles the `gui/` folder (the `.ui` file and
`novohours.ico`) into the exe, and `--icon "gui/novohours.ico"` embeds the icon
into the executable itself, so the result is a single self-contained
`novohours.exe` — with the right icon in Explorer — that you can run from anywhere.

> **Tip:** if `pyinstaller` fails with *"Unable to create process using ..."*,
> the venv's launcher scripts point at a stale Python path (this happens when a
> `venv-win` folder is copied between projects rather than freshly created).
> Recreate the venv, or just call PyInstaller through the interpreter, which
> sidesteps the launcher entirely:
>
> ```powershell
> python -m PyInstaller --clean --distpath . --onefile --windowed --icon "gui/novohours.ico" --add-data "gui;gui" novohours.py
> ```

## License

[MIT](LICENSE)
