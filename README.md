# Cyber Security Internship Project
This repository contains the tasks completed during the first month of the Cyber Security internship at Arch Technologies. The projects focus on network security and understanding system-level vulnerabilities through practical Python implementation.

## Project Overview
### Task 1: Basic Network Sniffer

**Objective:** Build a network sniffer in Python that captures and analyzes network traffic to understand data flow and packet structures.

**Tools Used:** Python, Scapy Library.

**Features:**
* Captures real-time IP packets.
* Extracts Source and Destination IP addresses.
* Identifies Transport Layer protocols (TCP/UDP) and their respective ports.
* Utilizes BPF (Berkeley Packet Filter) to optimize performance.

**Security Note:** This tool requires root/administrative privileges to access raw sockets.

**Running the Scripts**
```
sudo python3 sniffer.py
```

## Task 2: Key Logging

**Objective:** Simulate a basic keylogger in a controlled environment to understand how keystroke logging works and analyze the potential risks.

**Tools Used:** Python, pynput library.

**Features:**

* Monitors and captures user keystrokes locally.
* Logs keystrokes into a local file (key_log.txt) for analysis.
* Handles special keys (Space, Enter, etc.) for readability.

**Risk Analysis:**

* **Credential Theft:** Potential for capturing sensitive data like passwords.
* **Privacy Risks:** Demonstrates how unauthorized scripts can monitor private user activity.
* **Mitigation:** Highlights the importance of using antivirus software and avoiding untrusted scripts.

**Running the Scripts**

```
python3 keylogger.py
```
