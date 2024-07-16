# SECURE_E_PERSON_HEALTH_CARE_SYSTEM_USING_AES_ALGORITHM 🔒💉

## Overview 📋

A secure EHR system using AES encryption to protect patient data from unauthorized access while allowing swift access for authorized users.

## Keywords 📝

- **Electronic Medical Records**
- **E-Health Care Systems**
- **Information Hiding**
- **Security**
- **Symmetric Encryption**
- **AES**

## Motivation 🌟

Increase in data breaches in medical systems necessitates a secure solution for protecting patient data.

## Problem Statement ❗

Manual data management in healthcare leads to errors and potential data exposure. A secure and efficient system for electronic health records is needed.

## Solution 💡

Implement a secure EHR system using AES encryption for confidentiality and Fernet encryption for additional security features like message authentication.

## Literature Survey 📚

| **Paper Title** | **Authors & Year** | **Methodology** | **Merits** | **Limitations** |
|:---------------:|:------------------:|:---------------:|:----------:|:---------------:|
| Assessment of Encryption and Decryption Schemes for Secure Data Transmission in Healthcare Systems | Kazeem B. Adedeji et al. (2019) | ECC, RC4, DES, AES | Strong security protocols | AES algebraic structure simplicity |
| Smart Secure System For Human Health Monitoring | Nikhil Nair R, Kiran K A (2017) | AES in PHP, Raspberry Pi | Low power, high throughput | Performance limitations |
| An Efficient Data Security in Medical Report using Blockchain Technology | Mary Subaja Christo et al. (2019) | Quantum Cryptography, Blockchain | High security, trustworthy | Patient data modification |
| Complexity of Cyber Security Architecture for IoT Healthcare Industry | Aysha K. Alharam et al. (2017) | AES Encryption, S-Box | Efficient, strong algorithm | Synchronization issues |
| Cloud-Based E-Health Systems: Security and Privacy Challenges | Mohanad Dawoud et al. (2017) | Cloud Computing, WBAN | Good security and privacy | High maintenance cost |
| An Efficient Lightweight Cryptographic Technique For IoT based E-health care System | Ravi Raushan Kumar Chaudhary et al. (2020) | Lightweight Ciphers | Secure data transmission | Accuracy issues |
| Towards Secure and Smart Healthcare in Smart Cities Using Blockchain | Jinglin Qiu et al. (2018) | Blockchain | Patient privacy | Usability in clinical settings |
| A Privacy Preserving Optimization of Clinical Pathway Query for E-Healthcare Systems | Mingwu Zhang et al. (2020) | Cloud Servers | Better treatment, privacy protection | Encryption not used |
| A Hybrid Data Access Control Using AES and RSA For Ensuring Privacy In Electronic Healthcare Records | S. Kanaga Suba Raja et al. (2020) | AES and RSA Algorithms | Effective data access control | RSA slow for large data |
| Ensuring Privacy and Security in Health | Jayneel Vora et al. (2018) | AT&T Scheme | Low-cost access control | Weak communication protocol |

## Proposed Model 📐

**AES Algorithm:**
- **Phases:** Initial Round, Main Rounds, Final Round
- **Key Sizes:** 128, 192, 256 bits
- **Rounds:** 10, 12, 14 based on key size

**Encryption Process:**
1. Initial Round: Add Round Key
2. Main Rounds: Sub Bytes, Shift Rows, Mix Columns, Add Round Key
3. Final Round: Sub Bytes, Shift Rows, Add Round Key

**Decryption Process:**
- Reverses encryption steps.

## Functional Architecture 🏢

- **Doctor Module:** Access and update patient records.
- **Dean Module:** Manage access controls.
- **Patient Module:** Access health records.

## Tools & Platform 🛠️

- **Language:** Python
- **Platform:** IDLE Python
