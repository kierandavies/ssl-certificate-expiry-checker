import ssl
import socket
import datetime
from colorama import init, Fore

# Initialize colorama
init()

def get_certificate_expiry(fqdn):
    ssl_context = ssl.create_default_context()
    try:
        with socket.create_connection((fqdn, 443), timeout=3) as sock:
            sock.settimeout(10)  # Set the timeout for the socket
            with ssl_context.wrap_socket(sock, server_hostname=fqdn) as ssl_sock:
                cert = ssl_sock.getpeercert()
                # Extract the expiry date from the certificate
                expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                return expiry_date
    except (socket.gaierror, ConnectionRefusedError, ssl.SSLError, ssl.CertificateError, socket.timeout):
        return None

# Specify the file path containing the FQDNs
file_path = "fqdns.txt"

# Read FQDNs from the file
with open(file_path, "r") as file:
    fqdns = file.read().splitlines()

# Process each FQDN and print the output with color coding
for fqdn in fqdns:
    expiry_date = get_certificate_expiry(fqdn)
    if expiry_date is None:
        # FQDN failed
        print(Fore.RED + f"{fqdn} | FAILED" + Fore.RESET)
    else:
        current_year = datetime.datetime.now().year
        if expiry_date.year == current_year:
            # Expiry within the current year
            print(Fore.YELLOW + f"{fqdn} | {expiry_date.strftime('%Y-%m-%d %H:%M:%S')}" + Fore.RESET)
        elif expiry_date.year > current_year:
            # Expiry in the next year
            print(Fore.GREEN + f"{fqdn} | {expiry_date.strftime('%Y-%m-%d %H:%M:%S')}" + Fore.RESET)
        else:
            # Invalid expiry date
            print(Fore.RED + f"{fqdn} | INVALID EXPIRY DATE" + Fore.RESET)
