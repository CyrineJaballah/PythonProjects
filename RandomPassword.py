import random
import string

# Function to generate a secure password
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to check the security level of a password
def check_password_security(password):
    security_level = 0
    
    # Check password length
    if len(password) >= 8:
        security_level += 1
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        security_level += 1
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        security_level += 1
    

    if any(char.isdigit() for char in password):
        security_level += 1
    
    # Check for special characters
    if any(char in string.punctuation for char in password):
        security_level += 1
    
    return security_level

# Generate a secure password
password = generate_password()
print("Generated Password:", password)

# Check the security level of the generated password
security_level = check_password_security(password)
print("Security Level:", security_level)
