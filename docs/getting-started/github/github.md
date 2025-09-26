# GitHub Website Guide (Org → Project → Repo)

## Big Picture

```
RaiderAerospaceSociety25-26  (Organization)
├─ Projects (planning boards that aggregate issues/PRs)
│   ├─ SRAD Flight Computer
│   └─ Tracking Groundstation
└─ Repositories (actual code/docs/CAD per codebase)
    ├─ srad-flight-computer
    ├─ tracking-groundstation
    └─ ras-handbook (this site)
```

-   **Organization** = Shared owner for everything (teams, members, permissions, policies).
-   **Project** = Planning board (kanban) spanning one or multiple repos.
-   **Repository (repo)** = A single codebase with **code, issues, pull requests (PRs), CI**.

---

## When to Use GitHub (Website) vs Git (CLI)

-   **Use GitHub website** to: create issues, review PRs, comment, view CI status, browse files, manage Projects, read docs.
-   **Use Git (CLI)** to: clone, branch, commit, push, rebase/merge, resolve conflicts locally.

> Think: **Git = engine** (under the hood), **GitHub = garage** (where we coordinate).

---

## Common Tasks on GitHub

### 1) Create an Issue

1. Go to the repo → **Issues** → **New issue**.
2. Choose the template (bug/feature/docs).
3. Fill **what/why/how to test**, add labels, assign yourself, and submit.

**Pro tip:** Add “_Closes #123_” in your PR description to auto-close the issue on merge.

---

### 2) Start a Project (Leads)

-   Org page → **Projects** → **New project** (or use an existing board like **SRAD Flight Computer**).
-   Add views: **Board**, **Table**, **Roadmap**.
-   Add fields: Priority, Status, Owner, Due date.
-   Add issues/PRs from across repos to track the work in one place.

---

### 3) Open a Pull Request (PR)

1. Push your branch (from CLI or GitHub Desktop).
2. Repo → **Pull requests** → **New pull request** → pick your branch vs `main`.
3. Fill description (link the issue, motivation, how to test, screenshots/logs/renders).
4. Mark **Draft** if it’s not ready.
5. Request reviewers (your team leads/Code Owners).

**Checks:** CI (Actions) will run; PR shows ✅/❌ status at the top.

---

### 4) Review a PR

-   Open the PR → **Files changed**.
-   Use **Add a comment** or **Start a review** for multiple comments.
-   Use **Approve** / **Request changes** when done reviewing.
-   Conversations must be **Resolved** before merge.

**Firmware/Critical:** Some PRs require **2 approvals** (see repo rules).

---

### 5) Merge a PR

-   When CI is green and approvals complete, click **Merge** → choose **Squash** (preferred).
-   Enable **Auto-merge** to merge when checks finish.
-   Branch is deleted automatically after merge.

---

### 6) Find CI Logs / Artifacts

-   PR page → **Checks** tab → pick the failing job → view logs.
-   If artifacts are uploaded (renders, build outputs), you’ll see **Artifacts** to download.

---

### 7) Browse Code, History, and Blame

-   Use the **Code** tab to browse files.
-   Open a file → **History** to see who changed what and when.
-   **Blame** highlights per-line authorship.

---

## Permissions & Teams

-   You’ll be added to org teams (**SR-Avionics**, **SR-Airbrakes**) and project teams with appropriate repo access.
-   **Branch protection** on `main` prevents force-push and requires CI + reviews.
-   **Code Owners** auto-requested on relevant paths (e.g., `firmware/`, `docs/`).

---

## Where Things Live (Quick Map)

-   **Issues** → tasks/bugs per repo.
-   **Pull Requests** → code/doc changes for review.
-   **Projects** → cross-repo planning boards.
-   **Actions** → CI pipelines per repo.
-   **Wiki/Discussions** → optional; we use **repos + this handbook** instead.
-   **Pages** → published docs sites (e.g., this handbook).

---

## FAQ

**Q: I don’t see the repo.**  
A: You likely aren’t in the org/team. Ask a lead to invite you.

**Q: CI fails—what do I check?**  
A: PR → **Checks** tab. Read logs, fix locally, push again.

**Q: What’s a draft PR?**  
A: Safe place to get early feedback; won’t merge until **Ready for review**.

---

## Next Steps

-   Create your first **Issue** for a small task.
-   Follow the [Git CLI & Workflow](../git.md) guide to make a branch and open a PR.
