import socket
import platform
import uuid
from datetime import datetime
from pathlib import Path


def get_hostname():
    """Return the system hostname."""
    return socket.gethostname()


def get_ip_address():
    """Return the local IPv4 address."""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except socket.error:
        return "Unable to determine IP address"


def get_mac_address():
    """Return the system MAC address."""
    mac = uuid.getnode()
    mac_address = ":".join(
        f"{(mac >> i) & 0xff:02x}"
        for i in range(40, -1, -8)
    )
    return mac_address


def get_os_information():
    """Return operating system information."""
    return {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Python Version": platform.python_version()
    }


def get_network_interfaces():
    """Return available network interfaces."""
    try:
        interfaces = socket.if_nameindex()
        return [name for _, name in interfaces]
    except AttributeError:
        return ["Network interface detection not supported"]


def generate_report():
    """Collect system information and generate a text report."""

    hostname = get_hostname()
    ip_address = get_ip_address()
    mac_address = get_mac_address()
    os_info = get_os_information()
    interfaces = get_network_interfaces()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
============================================================
       SECURE NETWORK ASSET INVENTORY
       SYSTEM INFORMATION SCANNER
============================================================

Report Generated : {timestamp}

SYSTEM INFORMATION
------------------------------------------------------------
Hostname          : {hostname}
IP Address        : {ip_address}
MAC Address       : {mac_address}
Operating System  : {os_info["Operating System"]}
OS Version        : {os_info["OS Version"]}
Architecture      : {os_info["Architecture"]}
Python Version    : {os_info["Python Version"]}

NETWORK INTERFACES
------------------------------------------------------------
"""

    for interface in interfaces:
        report += f"  - {interface}\n"

    report += """
============================================================
                 END OF REPORT
============================================================
"""

    print(report)

    # Create reports directory if it doesn't exist
    reports_directory = Path("reports")
    reports_directory.mkdir(exist_ok=True)

    filename = reports_directory / "system_inventory_report.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"Report saved to: {filename}")


if __name__ == "__main__":
    generate_report()