import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5000: "Flask dev server / AirPlay Receiver",
    8080: "HTTP (alternate)"
}

ALLOWED_TARGETS = ["127.0.0.1", "localhost"]
MAX_PORTS = 1024


def scan_ports(target, start_port, end_port):
    # Safety check 1: only allow-listed targets
    if target not in ALLOWED_TARGETS:
        return {
            "error": "For safety, this version only scans localhost (127.0.0.1). "
                     "Only scan systems you own or have written permission to test.",
            "target": target,
            "open_ports": [],
            "scanned": 0
        }

    # Safety check 2: valid port numbers
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        return {"error": "Ports must be between 1 and 65535.",
                "target": target, "open_ports": [], "scanned": 0}

    if start_port > end_port:
        return {"error": "Start port must be less than or equal to end port.",
                "target": target, "open_ports": [], "scanned": 0}

    # Safety check 3: limit how much we scan in one request
    if (end_port - start_port + 1) > MAX_PORTS:
        return {"error": f"Please scan at most {MAX_PORTS} ports at a time.",
                "target": target, "open_ports": [], "scanned": 0}

    open_ports = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex(("127.0.0.1", port))
            if result == 0:
                open_ports.append({
                    "port": port,
                    "service": COMMON_PORTS.get(port, "Unknown")
                })

    return {
        "error": None,
        "target": target,
        "open_ports": open_ports,
        "scanned": end_port - start_port + 1
    }