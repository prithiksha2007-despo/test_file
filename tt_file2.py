def check_password_strength(password):
    length_ok = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    
    print(f"\nChecking password: '{password}'")
    
    if length_ok and has_number and has_upper:
        print("Strength: Strong! 💪")
    else:
        print("Strength: Weak ⚠️")
        print("Tips to improve:")
        if not length_ok:
            print("- Make it at least 8 characters long.")
        if not has_number:
            print("- Add at least one number.")
        if not has_upper:
            print("- Add at least one uppercase letter.")

# Test the function with a couple of examples
check_password_strength("weak")
check_password_strength("Python123")