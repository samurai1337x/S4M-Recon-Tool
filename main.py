import tkinter as tk
from tkinter import scrolledtext, messagebox, PhotoImage
import socket
import whois
import threading
import os
import base64


# DNS Lookup Function
def dns_lookup(domain, output_area):
    try:
        ip_address = socket.gethostbyname(domain)
        output_area.insert(tk.END, f"DNS Lookup for {domain}: {ip_address}\n")
    except Exception as e:
        output_area.insert(tk.END, f"Error in DNS Lookup: {e}\n")

# Whois Lookup Function
def whois_lookup(domain, output_area):
    try:
        w = whois.whois(domain)
        output_area.insert(tk.END, f"Whois Lookup for {domain}:\n{w}\n")
    except Exception as e:
        output_area.insert(tk.END, f"Error in Whois Lookup: {e}\n")

# Port Scanning Function
def port_scan(host, ports, output_area):
    try:
        ports = [int(p.strip()) for p in ports.split(",") if p.strip().isdigit()]
        if not ports:
            output_area.insert(tk.END, "Invalid port list. Please provide valid port numbers.\n")
            return
        
        output_area.insert(tk.END, f"Scanning {host} for ports: {ports}\n")
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                status = "Open" if result == 0 else "Closed"
                output_area.insert(tk.END, f"Port {port}: {status}\n")
    except Exception as e:
        output_area.insert(tk.END, f"Error in Port Scan: {e}\n")

# Common Ports Scanning
def common_ports_scan(host, output_area):
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP"
    }
    try:
        output_area.insert(tk.END, f"Scanning {host} for commonly known ports:\n")
        for port, service in common_ports.items():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                status = "Open" if result == 0 else "Closed"
                output_area.insert(tk.END, f"Port {port} ({service}): {status}\n")
    except Exception as e:
        output_area.insert(tk.END, f"Error in Common Ports Scan: {e}\n")

# Reverse DNS Lookup Function
def reverse_dns_lookup(ip_address, output_area):
    try:
        host = socket.gethostbyaddr(ip_address)
        output_area.insert(tk.END, f"Reverse DNS Lookup for {ip_address}: {host[0]}\n")
    except Exception as e:
        output_area.insert(tk.END, f"Error in Reverse DNS Lookup: {e}\n")

# Clear Output Function
def clear_output(output_area):
    output_area.delete(1.0, tk.END)

# Wrapper for threading
def run_in_thread(func, *args):
    thread = threading.Thread(target=func, args=args)
    thread.start()

# Apply dark theme
def apply_dark_theme(widget):
    widget.configure(bg="#1e1e1e", fg="#d4d4d4", insertbackground="#d4d4d4")

# Main GUI
def main():
    # Create main window
    root = tk.Tk()
    root.title("S4M Recon Tool")
    icon_base64 = "{{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}}"
    
    # Convert base64 string to a photo image
    icon_data = base64.b64decode(icon_base64)
    icon = PhotoImage(data=icon_data)    
    root.iconphoto(True, icon)

    # Dark theme
    root.configure(bg="#1e1e1e")

    # Input frame
    input_frame = tk.Frame(root, bg="#1e1e1e")
    input_frame.pack(padx=10, pady=10, fill=tk.X)

    tk.Label(input_frame, text="Domain / Host:", bg="#1e1e1e", fg="#d4d4d4").grid(row=0, column=0, sticky=tk.W)
    domain_entry = tk.Entry(input_frame, width=50, bg="#2d2d2d", fg="#d4d4d4", insertbackground="#d4d4d4")
    domain_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Ports (comma-separated):", bg="#1e1e1e", fg="#d4d4d4").grid(row=1, column=0, sticky=tk.W)
    ports_entry = tk.Entry(input_frame, width=50, bg="#2d2d2d", fg="#d4d4d4", insertbackground="#d4d4d4")
    ports_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="IP Address (for Reverse DNS):", bg="#1e1e1e", fg="#d4d4d4").grid(row=2, column=0, sticky=tk.W)
    ip_entry = tk.Entry(input_frame, width=50, bg="#2d2d2d", fg="#d4d4d4", insertbackground="#d4d4d4")
    ip_entry.grid(row=2, column=1, padx=5, pady=5)

    # Button frame
    button_frame = tk.Frame(root, bg="#1e1e1e")
    button_frame.pack(padx=10, pady=10)

    tk.Button(button_frame, text="DNS Lookup", width=15, bg="#007acc", fg="white", command=lambda: run_in_thread(dns_lookup, domain_entry.get(), output_area)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Whois Lookup", width=15, bg="#007acc", fg="white", command=lambda: run_in_thread(whois_lookup, domain_entry.get(), output_area)).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(button_frame, text="Port Scan", width=15, bg="#007acc", fg="white", command=lambda: run_in_thread(port_scan, domain_entry.get(), ports_entry.get(), output_area)).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(button_frame, text="Common Ports Scan", width=15, bg="#007acc", fg="white", command=lambda: run_in_thread(common_ports_scan, domain_entry.get(), output_area)).grid(row=0, column=3, padx=5, pady=5)
    tk.Button(button_frame, text="Reverse DNS Lookup", width=15, bg="#007acc", fg="white", command=lambda: run_in_thread(reverse_dns_lookup, ip_entry.get(), output_area)).grid(row=0, column=4, padx=5, pady=5)
    tk.Button(button_frame, text="Clear Output", width=15, bg="#e51400", fg="white", command=lambda: clear_output(output_area)).grid(row=0, column=5, padx=5, pady=5)

    # Output area
    output_frame = tk.Frame(root, bg="#1e1e1e")
    output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    output_area = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, height=20, bg="#2d2d2d", fg="#d4d4d4", insertbackground="#d4d4d4")
    output_area.pack(fill=tk.BOTH, expand=True)

    # Start GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
