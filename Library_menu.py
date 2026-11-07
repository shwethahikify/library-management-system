print("\n===== LIBRARY MANAGEMENT SYSTEM =====")

while True:
    print("\n1. Display Books")
    print("2. Search Books")
    print("3. Display Students")
    print("4. Search Student")
    print("5. View Issued Books")
    print("6. Calculate Fine")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("Display Books selected")

    elif choice == "2":
        print("Search Books selected")

    elif choice == "3":
        print("Display Students selected")

    elif choice == "4":
        print("Search Student selected")

    elif choice == "5":
        print("View Issued Books selected")

    elif choice == "6":
        print("Calculate Fine selected")

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
