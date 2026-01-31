import re
import getpass

COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty",
    "abc123", "password1", "admin", "letmein"
]

def check_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (minimum 8 characters)")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Password is too common")
        score = 0

    return score, feedback


def main():
    password = getpass.getpass("Enter password: ")
    score, feedback = check_strength(password)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print(f"\nStrength: {strength}")

    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"- {tip}")


if __name__ == "__main__":
    main()

