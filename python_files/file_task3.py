import os

while True:
    print("\nFile Manager Menu:")
    print("1. Create File")
    print("2. Append to File")
    print("3. Remove File")
    print("4. Read File")
    print("5. Check if File Exists")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        filename = input("Enter file name to create: ")
        with open(filename, "w") as file:
            print(f"File '{filename}' created successfully.")


    elif choice == "2":
        filename = input("Enter file name to append: ")
        if os.path.exists(filename):
            content = input("Enter content to append: ")
            with open(filename, "a") as file:
                file.write(content + "\n")
            print("Content appended successfully.")
        else:
            print("File does not exist.")

    
    elif choice == "3":
        filename = input("Enter file name to remove: ")
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' removed successfully.")
        else:
            print("File does not exist.")

    
    elif choice == "4":
        filename = input("Enter file name to read: ")
        if os.path.exists(filename):
            with open(filename, "r") as file:
                print("File Content:")
                print(file.read())
        else:
            print("File does not exist.")

    
    elif choice == "5":
        filename = input("Enter file name to check: ")
        if os.path.exists(filename):
            print("File exists.")
        else:
            print("File does not exist.")

            
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
