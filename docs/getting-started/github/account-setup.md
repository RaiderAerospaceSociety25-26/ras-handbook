# GitHub Account Setup

## 1. Create a GitHub Account

1. Go to [https://github.com/join](https://github.com/join).
2. Sign up with your **TTU or personal email**.
   - Use your TTU email if you want free access to the [GitHub Student Developer Pack](https://education.github.com/pack).
3. Pick a username you’re comfortable using for school + projects (e.g first-last).

---

## 2. Enable Two-Factor Authentication (2FA)

Security is required for all RAS/SpaceRaiders repos.

1. Go to **Settings → Password and authentication**.
2. Enable **2FA** using:
   - Authenticator app (recommended, e.g., Authy, Microsoft Authenticator), or
   - Hardware key (YubiKey, etc.).
3. Save your recovery codes somewhere safe.

---

## 3. Configure Authentication (SSH Recommended)

### Generate a new SSH key

```bash
# Generate a modern SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### Add your key to GitHub

1. Copy your public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. Go to **GitHub → Settings → SSH and GPG keys → New SSH key**.
3. Give it a name → Paste the key → Save.

### Test the connection

```bash
ssh -T git@github.com
```

You should see:  
`Hi <username>! You've successfully authenticated.`

---

## 5. Join the Organization

1. If you filled out the onboarding MS forms, you should have recieved an email/webapp invite.
2. Accept your invite to **RaiderAerospaceSociety25-26** on GitHub.
3. Confirm you see the **srad-flight-computer** and **tracking-groundstation** repos.
4. If you don’t see the invite, ask your team lead.

---

## 6. Next Steps

- Configure Git identity:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```
- Learn to navigate the [GitHub website](github.md)
- Follow the [Git Basics](../git.md) page for branching, commi
