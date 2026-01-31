# 🔐 File Integrity Checker (SHA-256)

A Python-based **File Integrity Monitoring (FIM)** tool designed to detect unauthorized file changes using cryptographic hashing.

This project demonstrates a **security-first mindset** by identifying file tampering, deletions, and unexpected modifications — a core concept in blue-team security, SOC work, and incident response.

---

## 🚀 Features

- Recursive file & folder hashing
- SHA-256 cryptographic integrity checks
- JSON-based hash database
- Tamper detection (modified files)
- Missing file detection
- Clean CLI flags with argparse
- Colored terminal output for clarity

---

## 🛠️ How It Works

1. Files are hashed using **SHA-256**
2. Hashes are stored in `hashes.json`
3. On verification, files are re-hashed
4. Any change is flagged immediately

---

## 📦 Usage

### Monitor a file or folder
```bash
python checker.py <path>
