def read_user_details():
    try:
        with open("user_details.txt", "r") as file:
            # Option 1: Read once and use content as needed
            content = file.read()
            print("\nUser Details:\n")
            print(content)
            
        # Option 2: Reopen or reset the file pointer to read again
        with open("user_details.txt", "r") as file:
            content2 = file.readlines()
            print("\nUser Details Line by Line:\n")
            print(content2)
            
    except FileNotFoundError:
        print("No user details found. Please add some users first.")

read_user_details()
