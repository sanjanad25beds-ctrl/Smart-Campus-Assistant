def search_classroom():

    classrooms = {
        "CSE": "Block A, Room 201",
        "ECE": "Block B, Room 105",
        "ISE": "Block A, Room 301",
        "MECHANICAL": "Block C, Room 102"
    }

    department = input("Enter department name: ").upper()

    if department in classrooms:
        print("Classroom Location:", classrooms[department])
    else:
        print("Classroom not found!")