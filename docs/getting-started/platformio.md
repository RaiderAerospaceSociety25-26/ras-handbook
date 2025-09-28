# PlatformIO IDE Setup & Usage Guide

## **Introduction**

-   What is PlatformIO IDE?
    -   PlatformIO IDE is an extension that runs within VS Code
    -   It allows you to program embedded systems (microcontrollers)
    -   Similarities to ArduinoIDE with more customization for our projects
-   Why use it?
    -   PIO IDE allows us to set custom environments per project
    -   Supports complex setups and configurations not found in ArduinoIDE
    -   You get to use the same VS Code that you use for any other project
-   Note: PlatformIO Code (Command line interface) is built into the extension

---

## **Installation**

### Prerequisites

-   Ensure Git works from **[terminal](terminal.md)** (`git --version`)
-   Install VS Code from our **[guide](vscode.md)**
-   Locally clone the repository code for `srad-flight-computer`, `tracking-groundstation`, or any other MCU based project

### Installing the Extension

-   Open VS Code → Extensions panel (++cmd+shift+"X"++)
-   Search "**PlatformIO IDE**"
-   Click **install**
-   Reload VS Code if needed

---

## **First-Time Setup & Creating a Project**

-   Click **PlatformIO Home** in status bar or sidebar (alien head icon)
-   To open a project either:
    -   Under `Project Tasks` click `Pick a folder` (folder must include `platform.ini` file)
    -   Open `PIO Home` using the command pallete ( ++cmd+shift+"P"++ ) Click `Open Project` (folder must include `platform.ini` file)
-   `firmware/` Directory structure:
    -   `platform.ini` Project config file
    -   `src/`: Operating code (e.g `.cpp` files)
    -   `include/`: Header files & Config files (e.g `.h` files)
    -   `lib/`: Custom project libraries (e.g `usfsmax/`)
    -   `tools/`: Custom software/visualizations (e.g `.py` but can be anything)

---

## **Project Workflow & Tasks**

### PlatformIO Toolbar & Status Bar Buttons

-   Build: Compiles your code
-   Upload: Uploads your code to the device
-   Clean: Deletes build files
-   Serial Monitor: Read device output

## Debugging & Serial Monitor

Serial Monitor:

-   Open by clicking **monitor** in an active project
-   Set baud-rate in `platform.ini` (e.g `monitor_speed = 115200`)

---

## **Working with Libraries**

### What is Library Management in PlatformIO

-   PlatformIO's Library Manager handles dependencies, versions, and ensures consistency across builds
-   You can pull from the PlatformIO Registry or from version control systems (e.g Git)
-   Projects remain self-contained: libraries are typically installed per project into `.pio/libdeps/`, not globally

### Adding Libraries via PlatformIO IDE (GUI)

1. Open PIO Home → go to Libraries section
2. Search for the library name (e.g, `Adafruit Sensor`, `Wire`)
3. Click "Add to Project"
4. Select the active project and environment
5. The extension then automatically updates your `platform.ini` (the `lib_deps` section) and downloads the library into `.pio/libdeps/` for that project

---

## **PlatformIO CLI**

PlatformIO IDE wraps the PlatformIO Core (CLI). You can also run commands directly in a terminal (inside VS Code’s integrated terminal or your system shell). PlatformIO Core provides a robust CLI for building, uploading, monitoring, and system operations.

**Here are key commands you should know:**

| Command              | Description                                                                           | Example Usage                                                                 |
| -------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `pio run`            | Build the project (all environments by default) :contentReference[oaicite:0]{index=0} | `pio run` <br> `pio run -e uno` <br> `pio run -e uno -t upload`               |
| `pio device list`    | List all connected serial/USB devices                                                 | `pio device list`                                                             |
| `pio device monitor` | Open serial monitor to view output from the device                                    | `pio device monitor --baud 115200`                                            |
| `pio lib list`       | Show libraries currently installed for the project                                    | `pio lib list`                                                                |
| `pio debug`          | Start a debugging session (CLI mode)                                                  | `pio debug --interface=gdb -x .pioinit` :contentReference[oaicite:1]{index=1} |
| `pio update`         | Update PlatformIO libraries, platforms, etc.                                          | `pio update`                                                                  |
| `pio upgrade`        | Upgrade the PlatformIO Core (CLI) tool                                                | `pio upgrade`                                                                 |
| `pio system info`    | Show system and environment information (PlatformIO)                                  | `pio system info`                                                             |
| `pio system prune`   | Clean up unused packages / cache to free space                                        | `pio system prune`                                                            |
