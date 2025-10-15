import datetime

def create_new_account():
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    try:
        with open("user_details.txt", "a") as file:
            file.write(f"Username: {username}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")
            file.write(f"Created At: {datetime.datetime.now()}\n")
            file.write("-" * 50 + "\n")
        print("✅ Account created successfully!")
    except FileNotFoundError:
        print("❌ File not found!")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open("user_details.txt", "r") as file:
            content = file.read()

            # Check both username and password exist together
            if f"Username: {username}" in content and f"Password: {password}" in content:
                print("✅ Login Successful!")
                return True
            else:
                print("❌ User not found or incorrect password.")
                return False
    except FileNotFoundError:
        print("❌ No users found. Please create an account first.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

    return False


def todo():
    while True:
        print("\n📝 Create a new Todo task\n")
        title = input("Enter the title of the Todo: ").strip()
        while not title:
            print("⚠️ Title is mandatory.")
            title = input("Enter the title of the Todo: ").strip()

        description = input("Enter the description of the Todo: ").strip()
        while not description:
            print("⚠️ Description is mandatory.")
            description = input("Enter the description of the Todo: ").strip()

        level = input("Select the level of the Todo (Low / Medium / High): ").strip().lower()
        while level not in ["low", "medium", "high"]:
            print("⚠️ Please select a valid level.")
            level = input("Select the level of the Todo (Low / Medium / High): ").strip().lower()

        with open("todo.txt", "a") as file:
            file.write(f"Title: {title}\n")
            file.write(f"Description: {description}\n")
            file.write(f"Level: {level}\n")
            file.write(f"Created At: {datetime.datetime.now()}\n")
            file.write("-" * 50 + "\n")
        print("✅ Todo added successfully!\n")
        


def home():
    print("\n🏠 Welcome to the System\n")
    print("1. Create an Account")
    print("2. Login to Account")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
    except ValueError:
        print("⚠️ Invalid input! Please enter a number (1 or 2).")
        return

    if choice == 1:
        create_new_account()
    elif choice == 2:
        if login():
            todo()
    else:
        print("⚠️ Invalid choice, please select 1 or 2.")


# Run the program
home()
