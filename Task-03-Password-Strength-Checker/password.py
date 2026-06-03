import string

while True:
    print("\n===== PASSWORD STRENGTH CHECKER =====")
    print("1. Check Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        password = input("Enter Password: ")

        score = 0

        if len(password) >= 8:
            score += 1

        if any(char.isupper() for char in password):
            score += 1

        if any(char.islower() for char in password):
            score += 1

        if any(char.isdigit() for char in password):
            score += 1

        if any(char in string.punctuation for char in password):
            score += 1

        print("\n===== RESULT =====")

        if score <= 2:
            print("🔴 Password Strength: WEAK")
        elif score <= 4:
            print("🟡 Password Strength: MEDIUM")
        else:
            print("🟢 Password Strength: STRONG")

    elif choice == "2":
        print("Thank you for using Password Strength Checker!")
        break

    else:
        print("Invalid choice!")