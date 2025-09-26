# Git CLI & Workflow

> **Goal:** Perform the day-to-day Git tasks from your terminal: clone, branch, commit, push, rebase, and open a PR.  
> This mirrors our [Contributing Guide] but in command form.

---

## 0) One-Line Mental Model

**Pull → Branch → Commit (small chunks!) → Push → PR → Review → Merge → Update**

---

## 1) First-Time Setup

### Install Git

- macOS: `brew install git`
- Windows: Install **Git for Windows** (includes Git Bash)
- Linux: `sudo apt install git` (or your distro’s package manager)

### Identify Yourself

```bash
git config --global user.name "Your Name"
git config --global user.email "you@ttu.edu"
```

### Use SSH (recommended)

Make sure you followed **[GitHub Account Setup](github/account-setup.md)** to add your SSH key; then:

```bash
ssh -T git@github.com
# Expect: "Hi <username>! You've successfully authenticated…"
```

---

## 2) Clone a Repo

```bash
# Avionics (example)
git clone git@github.com:RaiderAerospaceSociety25-26/srad-flight-computer.git
cd srad-flight-computer
```

---

## 3) Start From Main & Create a Branch

```bash
git switch main                 # go to main
git pull origin main            # sync with remote
git switch -c feat/short-name   # create & switch to a topic branch
git push -u origin HEAD         # publish branch (sets upstream)
```

**Branch naming:** `feat/...`, `fix/...`, `docs/...`, `chore/...`

---

## 4) Make Changes & Commit in Small Chunks

```bash
git status                          # see changed files
git add firmware/ src/ docs/        # stage changes (be specific when possible)
git commit -m "feat: add servo boot sequence"
```

**Conventional Commits:** `feat`, `fix`, `docs`, `chore`, `refactor`, `test`  
Rule of thumb: One logical change per commit; keep the repo buildable.

---

## 5) Keep Up-To-Date While You Work

```bash
git fetch origin
git rebase origin/main              # preferred for a clean history
# fix conflicts if needed, then:
git push --force-with-lease         # update your PR branch safely
```

> **Why rebase?** Your changes replay on top of the latest `main` = linear history, easier reviews.  
> Use `--force-with-lease` (not plain `--force`) to avoid clobbering teammates’ updates.

---

## 6) Open a Pull Request (PR)

```bash
git push                            # push any new commits
# Using GitHub CLI (optional, recommended):
gh pr create --draft --fill         # draft PR
# or
gh pr create --fill                 # ready for review
```

In the PR description:

- Link the issue: **Closes #123**
- Explain **what changed** and **how to test**
- Add screenshots/logs/renders if applicable (firmware, dashboards, CAD/PCB)

---

## 7) CI, Reviews, Merge

- CI runs automatically (Actions). Fix failures locally, then push.
- Address reviewer comments; push new commits.
- When green/approved, **Squash merge** (keeps `main` tidy).
- Branch auto-deletes on merge.

---

## 8) After Merge: Update Local

```bash
git switch main
git pull origin main
```

Start your next task from the fresh `main`.

---

## 9) Binary Assets (CAD/PCB/Images)

- Large binaries don’t diff like code. Commit sparingly with clear messages.
- If you must add big files regularly, talk to leads about **Git LFS** and repo policies.

---

## 10) Undo & Rescue (Cheatsheet)

```bash
git restore <file>                 # discard unstaged changes to <file>
git restore --staged <file>        # unstage a file (keep edits)

git reset --soft HEAD~1            # undo last commit, keep changes staged
git reset --mixed HEAD~1           # undo last commit, keep changes unstaged
git reset --hard HEAD~1            # undo last commit and throw away changes (danger)

git stash                          # stash current changes
git stash pop                      # restore stashed changes

git rebase --abort                 # back out of a rebase
git merge --abort                  # back out of a merge
```

---

## 11) Conflict Resolution (Quick)

1. Run rebase/merge and see conflicts.
2. Open the files; search for conflict markers:
   ```
   <<<<<<< HEAD
   your version
   =======
   incoming version
   >>>>>>> origin/main
   ```
3. Edit to the correct final version; save.
4. `git add <fixed-files>`
5. `git rebase --continue` (or `git commit` if you were merging)

---

## 12) Quick Reference

```bash
git pull                             # get updates
git switch -c feat/<name>            # new branch
git add <files> && git commit -m "type(scope): summary"
git push -u origin HEAD              # publish branch (first time)
git push                             # subsequent pushes
gh pr create --draft --fill          # draft PR
gh pr create --fill                  # ready PR
git fetch origin && git rebase origin/main   # stay current
```

---

## FAQs

**Q: Do I have to use the GitHub CLI (`gh`)?**  
A: No—create PRs through the website if you prefer.

**Q: My branch is behind `main`.**  
A: `git fetch origin && git rebase origin/main` (resolve conflicts if any, then push).

**Q: CI fails but builds locally.**  
A: Ensure tool versions match; run format/lint hooks; check Actions logs in the PR **Checks** tab.

---

## Next Steps

- If you haven’t already, read the **Contributing Guide** (bigger-picture process).
- Then pick an issue, branch, and make your first PR 🚀
