# CodeAlpha Basic Network Sniffer

## Cyber Security Internship Task 1

### Project Title

Basic Network Sniffer

### Author

PRINCE HALPARA

### Internship

CodeAlpha Cyber Security Internship

---

## Project Description

The Basic Network Sniffer is a Python-based cybersecurity tool that captures and analyzes network packets traveling through a network interface. The project helps in understanding how data is transmitted over a network and provides insight into different network protocols.

The program captures live network traffic and displays important information such as source IP address, destination IP address, protocol type, source port, destination port, and packet summary.

This project was developed as part of the CodeAlpha Cyber Security Internship Program to gain practical knowledge of packet analysis and network monitoring.

---

## Objectives

* Understand network packet flow.
* Learn packet capturing techniques.
* Analyze network protocols.
* Display useful packet information.
* Gain hands-on experience in cybersecurity.

---

## Technologies Used

* Python 3
* Scapy Library
* Npcap (Windows)
* Visual Studio Code
* Windows Operating System

---

## Features

* Captures live network packets.
* Displays Source IP Address.
* Displays Destination IP Address.
* Identifies TCP Protocol.
* Identifies UDP Protocol.
* Identifies ICMP Protocol.
* Shows Source and Destination Ports.
* Displays Packet Summary.
* Detects ARP and other Non-IP Packets.

---

## Installation

### Step 1: Install Python

Download and install Python from:

https://www.python.org

### Step 2: Install Scapy

Open Command Prompt and run:

```bash
pip install scapy
```

### Step 3: Install Npcap

Download and install Npcap from:

https://npcap.com

While installing, enable:

* Install Npcap in WinPcap API-compatible Mode

---

## How to Run the Project

1. Open Command Prompt as Administrator.
2. Navigate to the project folder.

```bash
cd CodeAlpha_BasicNetworkSniffer
```

3. Run the program.

```bash
python sniffer.py
```

4. Generate some network activity by opening websites or browsing the internet.
5. The program will capture packets and display their information.

---

## Sample Output

```text
Source IP      : 10.14.123.127
Destination IP : 172.64.155.209
Protocol       : TCP
Source Port    : 26991
Destination Port : 443
Packet Summary : Ether / IP / TCP
```

---

## Learning Outcomes

Through this project, I learned:

* Basics of packet sniffing.
* Working of TCP/IP networking.
* Packet structure and headers.
* Network monitoring techniques.
* Use of Scapy for packet analysis.
* Ethical use of cybersecurity tools.

---

## Ethical Statement

This project is created strictly for educational and learning purposes. It should only be used on networks where proper authorization and permission have been granted.

---

## Conclusion

The Basic Network Sniffer successfully captures and analyzes network packets. The project provides practical exposure to network traffic analysis and helps in understanding the fundamentals of cybersecurity and network communication.

---

## GitHub Repository Name

CodeAlpha_BasicNetworkSniffer
