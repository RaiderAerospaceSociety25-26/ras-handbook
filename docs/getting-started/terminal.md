# Terminal Basics

## Opening the Terminal

- **macOS**: Press `⌘ + Space`, type `Terminal`, hit Enter.
- **Windows**: Press `Win + R`, type `Terminal` (or search for **PowerShell/Command Prompt**), hit Enter.

_(Tip: On Windows, we recommend the Windows Terminal app for a better experience.)_

---

## Navigation Commands

Think of the terminal as a file explorer without the mouse.

- **Where am I?**
  ```bash
  pwd      # print working directory
  ```
- **List files/folders**
  ```bash
  ls       # macOS/Linux/Sometimes Windows
  dir      # Windows
  ```
- **Move into a folder**
  ```bash
  cd Documents
  ```
- **Go up/back one folder**
  ```bash
  cd ..
  ```

---

## Creating & Managing Folders

- **Make a new folder**
  ```bash
  mkdir projects
  ```
- **Delete a file**
  ```bash
  rm file.txt      # macOS/Linux/Sometimes Windows
  del file.txt     # Windows
  ```
- **Delete a folder**
  ```bash
  rm -rf folder/   # macOS/Linux
  rmdir /S folder  # Windows
  ```

---

## Git Basics in Terminal

You’ll use Git inside your repos (Avionics, Airbrakes, etc.).

_Repo link can be found on the repo page using the top right `<> Code` green button and navigating to the `SSH` link_

- **Clone a repo**
  ```bash
  git clone git@github.com:RaiderAerospaceSociety25-26/srad-flight-computer.git    # SFC Repo
  git clone git@github.com:RaiderAerospaceSociety25-26/tracking-groundstation.git  # TGS Repo
  ```
- **Check current branch**
  ```bash
  git status # Displays modified local files
  ```
- **Create a new branch**
  ```bash
  git switch -c feat/my-task # Switches to & Creates a branch <feat/my-task>
  ```
- **Stage and commit changes**
  ```bash
  git add .                              # Stages all current modified files
  git commit -m "feat: add servo driver" # Commits staged changes to local history (tree)
  ```
- **Push to GitHub**
  ```bash
  git push -u origin HEAD # Initial push to publish a new branch
  git push                # Subsequent pushes
  ```

---

## Running Project Commands

### Run Python Tools

Inside the `firmware/tools/` **sfc** folder there are helper Python scripts (for testing, telemetry parsing, logging, etc.).

1. First, install Python dependencies (one-time):

   ```bash
   cd firmware
   pip install -r requirements.txt
   ```

2. Run a tool:

   ```bash
   # Example: run the sensor test tool
   python3 tools/sensor_test.py

   # Example: parse log files
   python3 tools/log_parser.py logs/latest.log
   ```

_(On Windows, use `python` instead of `python3` if `python3` is not recognized.)_

---

## Tips & Shortcuts

- **Tab completion**: type part of a file name and press `Tab` to auto-complete.
- **Arrow keys**: scroll through your previous commands.
- **Ctrl + C**: cancel a running command.
- **Clear screen**
  ```bash
  clear   # macOS/Linux
  cls     # Windows
  ```
- **List files cleanly**:

```bash
ls -la    # list files vertically with extra info
```

- **Display File Structure:**

```bash
tree -L <depth> # depth of 2-3 is recommended to keep output readable
```

---

## Checklist ✅

- [ ] Can open terminal on your system
- [ ] Can navigate to your `Documents` folder
- [ ] Can create and delete a test folder
- [ ] Successfully cloned the Avionics or Airbrakes repo
- [ ] Ran `make build` without errors

---

## FAQ

**Q: I get `command not found`.**  
→ Means the program isn’t installed (e.g., Git). Go back to the [Git Setup](git.md) page.

**Q: My terminal looks different from screenshots.**  
→ That’s okay—macOS/Linux use `bash/zsh`, Windows uses `cmd` or `PowerShell`. Commands here cover both.
