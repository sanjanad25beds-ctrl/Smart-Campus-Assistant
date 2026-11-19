
def department_info():
    departments = {
        "CSE": "Computer Science and Engineering",
        "ECE": "Electronics and Communication Engineering",
        "ISE": "Information Science and Engineering",
        "AIML": "Artificial Intelligence and Machine Learning",
        "ME": "Mechanical Engineering",
        "CV": "Civil Engineering"
    }

    print("\n--- Smart Campus Department Information ---")
    print("Available departments:", ", ".join(departments.keys()))

    code = input("Enter department code: ").strip().upper()

    if code in departments:
        print("Department name:", departments[code])
    else:
        print("Department not found.")


if __name__ == "__main__":
    department_info()
