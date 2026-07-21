import re


COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "111111", "letmein", "admin", "welcome", 
    "12345678", "Hello@123"
]

def analyze_password(password):
    feedback = []
    score = 0

    if len(password) <= 12:
        score += 2
    elif len(password) <= 8:
        score += 1
    else:
        feedback.append("Password is too short (use at least 8 characters, ideally 12+).")


    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Password should include at least 1 number.")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback = ["This is a commonly used password and is very unsafe, regardless of length or characters."]


    if score <= 2:
        streingth = "Weak"
    elif score <=4:
        strength = "Moderate"
    else:
        strength = "Strong"
    

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }