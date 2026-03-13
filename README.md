# Cyber Security Internship Project
This repository contains the tasks completed during the first month of the Cyber Security internship at Arch Technologies. The projects focus on network security and understanding system-level vulnerabilities through practical Python implementation.

## Project Overview
### Task 1: Basic Network Sniffer

**Objective:** 

Build a network sniffer in Python that captures and analyzes network traffic to understand data flow and packet structures.

**Tools Used:** 

Python, Scapy Library.

**Features:**
* Captures real-time IP packets.
* Extracts Source and Destination IP addresses.
* Identifies Transport Layer protocols (TCP/UDP) and their respective ports.
* Utilizes BPF (Berkeley Packet Filter) to optimize performance.

**Security Note:** 

This tool requires root/administrative privileges to access raw sockets.

**Running the Scripts**
```
sudo python3 sniffer.py
```

## Task 2: Key Logging

**Objective:** 

Simulate a basic keylogger in a controlled environment to understand how keystroke logging works and analyze the potential risks.

**Tools Used:** 

Python, pynput library.

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
## Task 3: Advanced Data Recovery & Forensic Retrieval

 **Objective:** 
 
 To recover "permanently" deleted assets and analyze the reliability of signature-based file carving.
 
 **Tools Used:** 
 
 Recuva (Deep Scan Mode), Windows File Systems (NTFS), Hash Verification.

 **Features:** 
 * **Scenario Simulation:** Generated three high-resolution test images.
 * **Forensic File Carving:** Utilized Recuva’s deep scanning algorithms to search for Magic Bytes (file signatures) directly on the disk surface, independent of the Master File Table (MFT).
 * **Data Persistence Analysis:** Demonstrated that "deleted" data remains physically present on the storage medium until the specific clusters are overwritten by new write operations.
 * **Integrity Validation:** Performed post-recovery checks to ensure the binary structure of the images remained intact during the reconstruction process.
 
 **Recovery Steps:**

* **Incident Simulation:** Verified the presence of 3 target images on a Windows partition before performing a permanent deletion.

* **Surface Scanning:** Executed a Deep Scan targeting the specific drive sector. This allowed the tool to identify files based on their headers rather than their (now missing) directory entries.

* **Cross-Drive Restoration:** Restored the identified images to a separate physical drive. Security Note: This is a critical step to prevent "collision" where the recovery process overwrites the very data it is trying to save.

* **Verification:** Successfully reconstructed the 3 images and verified that the file metadata and image quality were preserved 100%.
 
 **Key Finding:** 
 
 Data persistence on NTFS remains high immediately after deletion, provided no new data is written to the drive. 

## Task 4: Credit Card Fraud Detection

**Objective:** 

Build a machine learning model to detect fraudulent transactions within a highly imbalanced dataset using Python.

**Tools Used:** 

Python 3, Scikit-learn, Seaborn, Matplotlib, SMOTE (imlearn).

**Features:**

* **Handling Class Imbalance:** Effectively resampled the training data from an initial distribution of 492 fraud cases against 284,315 legitimate cases to a balanced 227,451 vs. 227,451 ratio using SMOTE.

* **Algorithm Selection:** Implemented a Random Forest Classifier to handle complex non-linear relationships in transaction data.

* **Performance Analysis:** Generated a Confusion Matrix to visualize model accuracy, successfully identifying 84 out of 98 fraud cases in the test set.

* **Advanced Metrics:** Achieved a Weighted Average F1-score of 1.00 and a Fraud-specific (Class 1) Precision of 0.89, demonstrating high reliability in distinguishing suspicious activity from normal behavior.


**Technical Workflow:**

1. **Environment Setup:** Configured a Python virtual environment (venv) to manage dependencies like seaborn and scikit-learn.

2. **Data Resampling:** Applied oversampling to the minority class to ensure the model learned the characteristics of fraudulent patterns.

3. **Model Evaluation:** Generated a comprehensive Classification Report focusing on Recall (0.86) to minimize the "False Negative" rate—ensuring most fraud is caught.

4. **Visualization:** Produced a Confusion Matrix heatmap to confirm the model's predictive power across both classes.


## Model Performance Summary:

**Total Test Samples: 56,962**

**Fraud Detected (True Positives): 84**

**Legitimate (True Negatives): 56,854**

**Accuracy: 100% (Weighted)**

**Fraud Detection Precision: 89%**
