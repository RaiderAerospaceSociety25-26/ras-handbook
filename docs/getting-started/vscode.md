# VS Code Setup

## 1. Install VSCode from their

-   Download from the official **[VS Code website](https://code.visualstudio.com/download)**
-   Choose your OS (Windows, macOS, Linux)
-   Run the installer with default options
-   On windows, check the box to "Add to path" so the `code` works in the terminal

![VS Code marketplace (light)](../assets/images/vscode-download-light.png#only-light)
![VS Code marketplace (dark)](../assets/images/vscode-download-dark.png#only-dark)

---

## 2. Install the following extensions through the marketplace

Search for these in the Extensions Marketplace ( Mac: ++cmd+shift+"X"++ **OR** Win: ++ctrl+shift+"X"++ **OR** sidebar box icon):

-   PlatformIO IDE
-   Python
-   C/C++ Extension Pack
-   GitLens -- Git supercharged
-   indent-rainbow
-   Material Icon Theme

---

## 3. Recommended Settings

Add these in `settings.json` or via the GUI ( Mac: ++cmd+comma++ **OR** Win: ++ctrl+comma++ **OR** sidebar gear icon )

Enable format on save

```json
"editor.formatOnSave": true
```

Turn on **word wrap** (optional)

```json
"editor.wordWrap": "on"
```

## 4. Quick Usage Guide

#### Open a project

-   Open terminal → navigate to repo folder
-   Run:

```bash
code .
```

-   Or use File → Open Folder

#### Terminal in VS Code

-   Open with ( Mac: ++ctrl+shift+single-quote++ **OR** Win: ++ctrl+single-quote++ **OR** bottom left gear icon )
