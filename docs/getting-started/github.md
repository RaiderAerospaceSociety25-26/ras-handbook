# GitHub Setup

1. Create a GitHub account and enable **2FA**.
2. Configure SSH (preferred) or a PAT.
   - SSH quickstart:
     ```bash
     ssh-keygen -t ed25519 -C "you@example.com"
     eval "$(ssh-agent -s)"
     ssh-add ~/.ssh/id_ed25519
     cat ~/.ssh/id_ed25519.pub  # add to GitHub → Settings → SSH keys
     ```
3. Join the org/team and accept repo invites.
4. Install **GitHub Desktop** or use CLI only.
5. Turn on **code owners / required reviews** in repos (maintainers only).
