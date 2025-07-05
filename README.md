# LinkWise-Linux
LinkWise is a lightweight web-based tool that helps users detect and analyze suspicious or phishing URLs in real-time. It aims to enhance everyday cybersecurity awareness and protect users from malicious links often spread through emails, messages, and social media for Linux.
# 🔗 LinkWise – Linux Edition 🐧  
A powerful and lightweight terminal-based phishing URL detector.




## 🚀 About the Project

Originally built as a web-based tool, **LinkWise** now comes to the **Linux terminal** for all command-line lovers and cybersecurity enthusiasts.

This Python-based tool analyzes URLs and flags potentially malicious ones using common phishing detection heuristics.

---

## 🛡️ Features

- ✅ Detects non-HTTPS links
- 🧠 Warns about suspicious keywords (e.g., login, verify, bank)
- 🚩 Flags IP-based URLs
- 🔍 Highlights unusual characters (@, %, etc.)
- 📏 Warns if the URL is unusually long
- 🎨 Color-coded terminal output for clarity

---

📦 Installation
git clone https://github.com/yourusername/linkwise-linux.git
cd linkwise-linux
python3 linkwise.py

## 📷 Preview

```bash
$ python3 linkwise.py
🔗 Enter a URL: http://example-login.com/verify
⚠️ Suspicious URL Detected!

Reasons:
• Does not use HTTPS
• Contains suspicious keyword: "login"
• Contains suspicious keyword: "verify"


