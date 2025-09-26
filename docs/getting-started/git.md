# Git Basics

!!! info "Goal"
Be able to clone, branch, commit, merge, and open a pull request.

## Install

- Install Git: https://git-scm.com/downloads
- Set identity:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```

## Daily Flow

```bash
# 1) Create a feature branch
git checkout -b feat/<short-task-name>

# 2) Work and commit
git add -A
git commit -m "feat: short, imperative summary"

# 3) Sync with main
git fetch origin
git rebase origin/main  # or merge if preferred

# 4) Push and open PR
git push -u origin HEAD
```

## Fix common issues

- Undo last commit (keep changes): `git reset --soft HEAD~1`
- Drop local changes: `git reset --hard`
- Resolve merge conflicts: edit files → `git add` → `git rebase --continue`
