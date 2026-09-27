# CodeAlpha_NetworkSniffer

## Overview
This is a Python-based network sniffer built for **Task 1** of the CodeAlpha Cybersecurity Internship. The program captures live network traffic, analyzes packet structures, and saves structured logs.

## Features
- Captures live TCP / HTTPS network packets using Scapy.
- Parses packet details and protocol metadata.
- Automatically logs captured session data into a JSON file.

## Tech Stack
- Python 3.12
- Scapy

## Project Structure
```text
CodeAlpha_NetworkSniffer/
│
├── main.py                # Main application entry point
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
├── src/
│   ├── __init__.py        # Package initialization
│   ├── sniffer.py         # Packet capture logic
│   ├── parser.py          # Packet parsing logic
│   └── logger.py          # JSON logging utility
│
└── logs/
    └── capture_log.json   # Saved output logs

How to Run
1.Open your terminal or PowerShell as Administrator.
2.Install dependencies:
    pip install -r requirements.txt
3.Run the program:
    python main.py

---

### How to save it to GitHub in 3 simple commands:
Once you paste that into your `README.md` and save the file in VS Code, just run these three lines in your terminal:
```cmd
git add README.md
git commit -m "Add final clean README for Task 1"
git push origin main