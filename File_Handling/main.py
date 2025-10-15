def user_details():
    
    while True:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        if not age.isdigit():
            print("Please enter a valid age.")
            continue
        address = input("Enter your address: ")
        email = input("Enter your email: ")
        phone: int = input("Enter your phone number: ")
        with open("user_details.txt", "a") as file:
            file.write(f"Name: {name}\nAge: {age}\nAddress: {address}\nEmail: {email}\nPhone: {phone}\n{'-'*40}\n")
        more = input("Do you want to add another user? (yes/no): ").strip().lower()
        if more != 'yes':
            break

user_details()