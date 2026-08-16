import validators
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = ["verify", "secure", "account", "update", "login", "confirm", "banking"]
SUSPICIOUS_TLDS = [".xyz", ".top", ".click", ".tk", ".loan", ".work"]

def analyze_url(url):
    feedback = []
    critical_flags = []
    score = 0  # higher score = safer, but critical flags override this

    if not validators.url(url):
        return {
            "risk_level": "Invalid",
            "score": 0,
            "feedback": ["This does not appear to be a structurally valid URL."]
        }

    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    # HTTPS check - now a minor signal, not a strong trust indicator
    if parsed.scheme == "https":
        score += 1
    else:
        feedback.append("URL does not use HTTPS — connection is not encrypted.")

    # '@' symbol trick - CRITICAL
    if "@" in parsed.netloc:
        critical_flags.append(f"URL contains '@' — the real destination is '{hostname}', not the text before '@'.")
    else:
        score += 1

    # IP address instead of domain - CRITICAL
    is_ip = hostname.replace(".", "").isdigit()
    if is_ip:
        critical_flags.append("URL uses a raw IP address instead of a domain name.")
    else:
        score += 1

    # Excessive subdomains
    excessive_subdomains = hostname.count(".") > 3
    if excessive_subdomains:
        feedback.append("URL has an unusually high number of subdomains, a common disguise tactic.")
    else:
        score += 1

    # Suspicious keywords
    found_keywords = [word for word in SUSPICIOUS_KEYWORDS if word in url.lower()]
    if found_keywords:
        feedback.append(f"URL contains suspicious keyword(s): {', '.join(found_keywords)}.")
    else:
        score += 1

    # CRITICAL combo: suspicious keyword + excessive subdomains = classic brand impersonation
    if found_keywords and excessive_subdomains:
        critical_flags.append("URL combines a trusted-sounding keyword with excessive subdomains — a common brand impersonation pattern.")

    # Suspicious TLD
    if any(hostname.endswith(tld) for tld in SUSPICIOUS_TLDS):
        feedback.append("URL uses a top-level domain commonly associated with spam/phishing.")
    else:
        score += 1

    # Length
    if len(url) > 100:
        feedback.append("URL is unusually long, which can be used to hide the real destination.")
    else:
        score += 1

    # Determine risk level - critical flags force High Risk regardless of score
    all_feedback = critical_flags + feedback
    if critical_flags:
        risk_level = "High Risk"
    elif score <= 3:
        risk_level = "High Risk"
    elif score <= 5:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    if not all_feedback:
        all_feedback.append("No obvious red flags detected.")

    return {
        "risk_level": risk_level,
        "score": score,
        "feedback": all_feedback
    }