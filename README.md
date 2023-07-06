# Certificate Expiry Checker
## ssl-certificate-expiry-checker

This script allows you to check the expiry date of SSL certificates for a list of Fully Qualified Domain Names (FQDNs) stored in a text file. It uses the `ssl`, `socket`, `datetime`, and `colorama` libraries in Python.

## Prerequisites
- Python 3.x
- The `colorama` library, which can be installed using `pip install colorama`

## Usage
1. Clone the repository or download the script file to your local machine.
2. Create a text file (`fqdns.txt`) and populate it with the FQDNs for which you want to check the certificate expiry. Each FQDN should be on a separate line.
3. Ensure that you have the `colorama` library installed. You can install it by running `pip install colorama` in your terminal.
4. Open a terminal or command prompt and navigate to the directory where the script is located.
5. Run the script using the command `python certificate_expiry_checker.py`.
