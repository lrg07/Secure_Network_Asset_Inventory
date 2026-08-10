# Secure Network Asset Inventory & System Information Scanner

A lightweight Python-based cybersecurity utility that collects basic system and network information and generates a structured inventory report.

## Project Overview

Organizations need visibility into their connected systems for effective asset management and cybersecurity monitoring. Manual collection of system information can be slow and inaccurate.

This project provides a simple Python utility that automatically collects important host and network information and saves the results to a text report.

## Objectives

- Identify host information
- Retrieve network details
- Display operating system information
- List available network interfaces
- Generate a structured inventory report
- Save collected information to a text file

## Features

- Hostname detection
- Local IP address detection
- MAC address retrieval
- Operating system information
- OS version and architecture information
- Python version detection
- Network interface listing
- Automatic report generation
- Timestamped report output

## Technologies Used

- Python
- Git
- GitHub
- Windows / Linux
- VMware Workstation
- Kali Linux

## Project Structure

```text
Secure_Network_Asset_Inventory/
│
├── Asset_Inventory.py
├── .gitignore
└── reports/
    └── system_inventory_report.txt