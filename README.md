# S4M Recon Tool

## Overview

S4M Recon Tool is a network reconnaissance utility built with Python and Tkinter, providing multiple network investigation features in a user-friendly graphical interface.

## Features

- DNS Lookup
- Whois Lookup
- Port Scanning
  - Custom Port Scan
  - Common Ports Scan
- Reverse DNS Lookup

## Prerequisites

- Python 3.x
- Required libraries:
  - tkinter
  - python-whois

## Installation

1. Clone the repository:

```bash
git clone https://github.com/samurai1337x/S4M-Recon-Tool.git
cd S4M-Recon-Tool
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the tool:

```bash
python main.py
```

### Interface Guide

- **Domain/Host**: Enter the target domain or IP address
- **Ports**: For port scanning, enter comma-separated port numbers
- **IP Address**: For reverse DNS lookup

### Buttons

- **DNS Lookup**: Resolve domain to IP address
- **Whois Lookup**: Retrieve domain registration information
- **Port Scan**: Scan specific ports
- **Common Ports Scan**: Scan predefined common ports
- **Reverse DNS Lookup**: Find hostname for a given IP
- **Clear Output**: Reset the output window

## Disclaimer

This tool is for educational and authorized testing purposes only. Ensure you have proper authorization before scanning networks or systems you do not own.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
