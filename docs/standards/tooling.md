# Tooling Standards

> **Why this page?** Ensure every member has the same toolchain, formatting, and CI checks so contributions are consistent and reproducible.

## Goals

-   Single‑command builds and uploads
-   Auto‑format + lint before code ever hits a PR
-   Editor settings that match CI
-   Clear minimum versions and where to get them
-   Define commands/setups for needed tools

---

## Required Tools (minimum versions)

-   **Git** ≥ 2.39
-   **VS Code** (latest) with recommended extensions below
-   **PlatformIO Core** (installed by VS Code extension) for ESP32 projects
-   **Python** ≥ 3.10 (PlatformIO manages venvs automatically)
-   **clang-format** ≥ 16 (C/C++ formatting)
-   **pre-commit** ≥ 3 (git hook runner)
-   _(optional)_ **Make** or **Just** for task shortcuts

> Install `clang-format` via your OS package manager (e.g., `brew install llvm` on macOS, `choco install llvm` on Windows, `apt install clang-format` on Ubuntu).

---

## Repo Conventions
