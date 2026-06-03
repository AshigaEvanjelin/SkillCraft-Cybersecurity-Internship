# Caesar Cipher Program

history = []

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


while True:
    print("\n===== Caesar Cipher Menu =====")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. View History")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        message = input("Enter the message: ")

        while True:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            print("Please enter a shift value between 1 and 25.")

        encrypted = encrypt(message, shift)

        print("\n----- Result -----")
        print("Original Message :", message)
        print("Encrypted Message:", encrypted)

        print("\n----- Character Count -----")
        print("Total Characters:", len(message))
        print("Letters:", sum(c.isalpha() for c in message))
        print("Spaces :", message.count(" "))

        history.append(
            f"Encrypted | Original: {message} | Result: {encrypted}"
        )

    elif choice == "2":
        message = input("Enter the encrypted message: ")

        while True:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            print("Please enter a shift value between 1 and 25.")

        decrypted = decrypt(message, shift)

        print("\n----- Result -----")
        print("Encrypted Message:", message)
        print("Decrypted Message:", decrypted)

        print("\n----- Character Count -----")
        print("Total Characters:", len(message))
        print("Letters:", sum(c.isalpha() for c in message))
        print("Spaces :", message.count(" "))

        history.append(
            f"Decrypted | Original: {message} | Result: {decrypted}"
        )

    elif choice == "3":
        print("\n===== History =====")

        if len(history) == 0:
            print("No history available.")
        else:
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")

    elif choice == "4":
        print("Thank you for using Caesar Cipher!")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")