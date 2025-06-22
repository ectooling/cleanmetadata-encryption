# CleanMetadata Encryption Module

This repository publishes the standalone encryption module used by [CleanMetadata.com](https://www.cleanmetadata.com) to secure uploaded files before metadata removal. We provide this code to demonstrate transparency and compliance with our stated privacy practices.

## 🔐 What This Repo Contains

- `encryption.py`: A self-contained AES-GCM encryption module (256-bit key).
- `test_encrypt.py`: Simple test script to demonstrate encryption/decryption flow.
- No metadata removal logic is included — this is strictly for encryption.

## 🎯 Purpose

We believe in privacy by design. This repo exists to:
- Show how files are encrypted *before* any processing.
- Demonstrate that we do **not inspect**, **store**, or **log** unencrypted file contents.
- Comply with legal and ethical standards for transparency and user protection.

## ✅ Key Features

- AES-256 encryption in Galois/Counter Mode (GCM) for confidentiality and integrity.
- Randomly generated IV (nonce) per file.
- Keys are generated per session and never stored.
- Suitable for pre-processing encryption in local or client-side workflows.

## ⚠️ What This Is Not

- Not a production-ready key management system.
- Does not include any metadata removal logic or CleanMetadata service code.
- Not intended for long-term encrypted storage or secure messaging.

## 🚀 Usage

Clone this repo and run the test script:

```bash
python test_encrypt.py
```

You can also import `encrypt_file()` and `decrypt_file()` into your own workflows.

## 🧾 Compliance Notice

This software and associated service comply with U.S. export control laws.

Use is prohibited by any person or entity located in or controlled from a country subject to comprehensive U.S. trade sanctions, including but not limited to: Cuba, Iran, North Korea, Syria, and the Crimea, Donetsk, and Luhansk regions of Ukraine.

We actively block usage from sanctioned regions to comply with U.S. law and to fulfill Technology and Software under U.S. Export Administration Regulations (TSU) obligations.

## 📜 License

MIT License — see [LICENSE](LICENSE). Use freely with attribution. No warranty.

## 📣 About CleanMetadata

[CleanMetadata](https://www.cleanmetadata.com) is a free, privacy-respecting metadata removal tool. Files are encrypted, cleaned instantly, and auto-deleted. We do not log, track, or profile users.

> This repository is part of our effort to provide a transparent and secure user experience.
