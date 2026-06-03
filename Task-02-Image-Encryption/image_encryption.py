from PIL import Image
from tkinter import Tk, filedialog

ENCRYPTED_FILE = "encrypted_image.png"


def select_image():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")
        ]
    )

    return file_path


def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(ENCRYPTED_FILE)

    print("\n✅ Image encrypted successfully!")
    print(f"Saved as: {ENCRYPTED_FILE}")


def decrypt_image(key):
    try:
        img = Image.open(ENCRYPTED_FILE)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                pixels[x, y] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256
                )

        img.save("decrypted_image.png")

        print("\n✅ Image decrypted successfully!")
        print("Saved as: decrypted_image.png")

    except FileNotFoundError:
        print("\n❌ No encrypted image found.")
        print("Please encrypt an image first.")


while True:

    print("\n========== IMAGE ENCRYPTION TOOL ==========")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":

        image_path = select_image()

        if not image_path:
            print("No image selected.")
            continue

        while True:
            try:
                key = int(input("Enter encryption key (1-255): "))

                if 1 <= key <= 255:
                    break

                print("Key must be between 1 and 255.")

            except ValueError:
                print("Please enter a valid number.")

        encrypt_image(image_path, key)

    elif choice == "2":

        while True:
            try:
                key = int(input("Enter decryption key: "))

                if 1 <= key <= 255:
                    break

                print("Key must be between 1 and 255.")

            except ValueError:
                print("Please enter a valid number.")

        decrypt_image(key)

    elif choice == "3":

        print("\nThank you for using the Image Encryption Tool!")
        break

    else:
        print("\n❌ Invalid choice. Please enter 1, 2, or 3.")