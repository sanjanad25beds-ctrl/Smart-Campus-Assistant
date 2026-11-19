rom department import department_info
from classroom import search_classroom
from campus_services import find_facility, campus_contacts


def main():

    while True:
        print("\n===== SMART CAMPUS ASSISTANT =====")
        print("1. Classroom Information")
        print("2. Department Information")
        print("3. Campus Facilities")
        print("4. Campus Contacts")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            search_classroom()

        elif choice == "2":
            department_info()

        elif choice == "3":
            find_facility()

        elif choice == "4":
            campus_contacts()

        elif choice == "5":
            print("\nThank you for using Smart Campus Assistant!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()


