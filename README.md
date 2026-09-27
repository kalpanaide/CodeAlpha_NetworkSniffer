# 🛡️ CodeAlpha_NetworkSniffer (JA4-Probe)

A research-driven TLS handshake analyzer and basic network sniffer built for the **CodeAlpha Cybersecurity Internship (Task 1)**. 

---

## 🚀 Overview
This tool captures live TCP port 443 (HTTPS) traffic using Python and Scapy, parses incoming TLS `ClientHello` handshake records, extracts version and payload metadata, and automatically logs structured audit trails into a JSON format.

---

## 🛠️ Tech Stack & Requirements
* **Language:** Python 3.12
* **Packet Capture Engine:** Scapy / Npcap (Windows)
* **Libraries:** `scapy>=2.5.0`

---

## 📂 Project Directory Structure
```text
CodeAlpha_NetworkSniffer/
│
├── main.py                # Main application entry point & CLI banner
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
├── src/
│   ├── __init__.py        # Package initializer
│   ├── sniffer.py         # Core packet capture loop and callback handler
│   ├── parser.py          # TLS ClientHello record disassembler
│   └── logger.py          # JSON structured logging utility
│
├── logs/
│   └── capture_log.json   # Output audit logs of captured TLS handshakes
│
└── tests/                 # Unit test directory