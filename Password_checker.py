import re

def check_password_strength(password):
    """Check the strength of a given password."""
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Evaluate
    if strength == 5:
        return "✅ Strong password!", []
    elif 3 <= strength < 5:
        return "⚠️ Medium password.", feedback
    else:
        return "❌ Weak password!", feedback


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result, tips = check_password_strength(pwd)
    print(result)
    if tips:
        print("\nSuggestions:")
        for t in tips:
            print(f"- {t}")
