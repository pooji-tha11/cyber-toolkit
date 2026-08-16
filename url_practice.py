import validators
from urllib.parse import urlparse

test_urls = [
    "https://www.google.com",
    "http://192.168.1.1/login",
    "http://www.paypal.com@malicious-site.com/",
    "not a url at all",
    "https://verify-account.paypal.com.security-check.net/login"
]

for url in test_urls:
    print(f"URL: {url}")
    is_valid = bool(validators.url(url))
    print(f"  Valid structure: {is_valid}")

    if is_valid:
        parsed = urlparse(url)
        print(f"  Scheme: {parsed.scheme}")
        print(f"  Netloc (domain part): {parsed.netloc}")
        print(f"  Path: {parsed.path}")
    print()