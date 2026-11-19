def find_facility():
    facilities = {
        "library": "Library - Main Academic Block",
        "canteen": "Canteen - Near College Entrance",
        "lab": "Computer Laboratory - CSE Block",
        "sports": "Sports Ground - Behind Main Building"
    }

    print("\n--- CAMPUS FACILITIES ---")
    print("Available: Library, Canteen, Lab, Sports")

    facility = input("Enter facility name: ").lower()

    if facility in facilities:
        print("Facility Location:", facilities[facility])
    else:
        print("Facility not found.")


def campus_contacts():
    contacts = {
        "office": "College Office - 080-2372XXXX",
        "library": "Library Department - 080-2372XXXX",
        "placement": "Placement Cell - 080-2372XXXX",
        "admission": "Admission Office - 080-2372XXXX"
    }

    print("\n--- CAMPUS CONTACT INFORMATION ---")
    for department, contact in contacts.items():
        print(department.title(), ":", contact)


if __name__ == "__main__":
    while True:
        print("\n===== SMART CAMPUS SERVICES =====")
        print("1. Find Campus Facility")
        print("2. Campus Contact Information")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            find_facility()
        elif choice == "2":
            campus_contacts()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")