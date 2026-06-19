normalqueue = []
urgentqueue = []
priorityqueue = []

doctorlogin = {
    "username": "admin@hospital.com",
    "password": "123"
}

while True:
    print("\n" + "=" * 20)
    print(" APPOINTMENT QUEUE!")
    print("=" * 20)
    print("N = Normal | U = Urgent | P = Priority | M = Medical Area")

    option = input("\nChoose an option: ").upper()

    if option in ["N", "U", "P"]:
        name = input("Enter the patient's name: ")
        try:
            age = int(input("Enter the age: "))
            data = f"{name} ({age} years old)"

            if option == "N":
                normalqueue.append(data)
            elif option == "U":
                urgentqueue.append(data)
            elif option == "P":
                priorityqueue.append(data)

            print(f"Patient {name} added successfully!")
        except ValueError:
            print("ERROR: Age must be an integer!")

    elif option == "M":
        doctorusername = input("Email: ")
        doctorpassword = input("Password: ")

        if doctorusername == doctorlogin["username"] and doctorpassword == doctorlogin["password"]:
            while True:
                print("\n--- MEDICAL PANEL ---")
                print("1 - Normal Queue\n2 - Urgent Queue\n3 - Priority Queue\n4 - Exit")
                medicaloption = input("Select: ")

                if medicaloption == "1":
                    print(f"Normal Queue: {normalqueue}")
                elif medicaloption == "2":
                    print(f"Urgent Queue: {urgentqueue}")
                elif medicaloption == "3":
                    print(f"Priority Queue: {priorityqueue}")
                elif medicaloption == "4":
                    break
                else:
                    print("Invalid option.")
        else:
            print("Incorrect username or password.")

    else:
        print("Invalid option.")
