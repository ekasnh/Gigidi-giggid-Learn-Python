import re
import getpass
import math

# List of commonly used weak passwords
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "12345", "1234567",
    "qwerty", "abc123", "password1", "123123", "letmein", "iloveyou"
}

# Function to calculate Shannon entropy
def calculate_entropy(password):
    unique_chars = set(password)
    entropy = len(password) * math.log2(len(unique_chars))
    return entropy

# Function to calculate estimated crack time
def calculate_crack_time(password):
    guesses_per_second = 1e9  # 1 billion guesses per second
    # Determine the size of the character set used
    char_space = 0
    if re.search(r'[a-z]', password):
        char_space += 26  # Lowercase letters
    if re.search(r'[A-Z]', password):
        char_space += 26  # Uppercase letters
    if re.search(r'\d', password):
        char_space += 10  # Digits
    if re.search(r'[!@#$%^&*(),.?":{}|<>~`_+=|/\\]', password):
        char_space += 32  # Common special characters

    total_combinations = char_space ** len(password)
    crack_time_seconds = total_combinations / guesses_per_second

    # Convert seconds to human-readable format
    if crack_time_seconds < 60:
        return f"{crack_time_seconds:.2f} seconds"
    elif crack_time_seconds < 3600:
        return f"{crack_time_seconds / 60:.2f} minutes"
    elif crack_time_seconds < 86400:
        return f"{crack_time_seconds / 3600:.2f} hours"
    elif crack_time_seconds < 31536000:
        return f"{crack_time_seconds / 86400:.2f} days"
    else:
        return f"{crack_time_seconds / 31536000:.2f} years"

def check_password_strength(password):
    # Define stricter criteria
    length_criteria = len(password) >= 16  # Minimum length of 16
    uppercase_criteria = len(re.findall(r'[A-Z]', password)) >= 2  # At least 2 uppercase letters
    lowercase_criteria = len(re.findall(r'[a-z]', password)) >= 2  # At least 2 lowercase letters
    digit_criteria = len(re.findall(r'\d', password)) >= 2  # At least 2 digits
    special_char_criteria = len(re.findall(r'[!@#$%^&*(),.?":{}|<>~`_+=|/\\]', password)) >= 2  # At least 2 special chars
    entropy = calculate_entropy(password)

    # Check against a blacklist of common passwords
    if password.lower() in COMMON_PASSWORDS:
        return "Weak: Your password is too common and easily guessable."

    # Count how many criteria are met
    criteria_met = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    # Determine the password strength based on stricter criteria
    if length_criteria and criteria_met == 5 and entropy > 70:
        crack_time = calculate_crack_time(password)
        return f"Strong: Your password meets all the strict security requirements. Estimated crack time: {crack_time}"
    elif length_criteria and criteria_met >= 4 and entropy > 60:
        crack_time = calculate_crack_time(password)
        return f"Moderate: Your password is fairly secure but could be stronger. Estimated crack time: {crack_time}"
    else:
        crack_time = calculate_crack_time(password)
        return f"Weak: Your password does not meet the required security standards. Estimated crack time: {crack_time}"

# Secure input
if __name__ == "__main__":
    print("Strict Password Strength Checker with Estimated Crack Time")
    password = getpass.getpass("Enter your password (input hidden): ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
