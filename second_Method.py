import pandas as pd
import os

FILE = "students.xlsx"

# Create file if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["ID", "Name", "Age", "Course"])
    df.to_excel(FILE, index=False)


# ---------------- FUNCTIONS ----------------

def load_data():
    df = pd.read_excel(FILE)

    # Fix ID type issue (Excel sometimes makes it float)
    if not df.empty:
        df["ID"] = df["ID"].astype(int)

    return df


def save_data(df):
    df.to_excel(FILE, index=False)


def add_student():
    df = load_data()

    name = input("Enter Name: ")

    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("❌ Invalid age\n")
        return

    course = input("Enter Course: ")

    new_id = 1 if df.empty else df["ID"].max() + 1

    new_row = pd.DataFrame([[new_id, name, age, course]],
                           columns=["ID", "Name", "Age", "Course"])

    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)

    print("✅ Student Added\n")


def view_students():
    df = load_data()

    print("\n--- Students ---")

    if df.empty:
        print("No records found\n")
    else:
        print(df.to_string(index=False))
        print()


def update_student():
    df = load_data()

    try:
        student_id = int(input("Enter ID to update: "))
    except ValueError:
        print("❌ Invalid ID\n")
        return

    if student_id in df["ID"].values:
        name = input("Enter New Name: ")

        try:
            age = int(input("Enter New Age: "))
        except ValueError:
            print("❌ Invalid age\n")
            return

        course = input("Enter New Course: ")

        df.loc[df["ID"] == student_id, ["Name", "Age", "Course"]] = [name, age, course]
        save_data(df)

        print("✅ Updated\n")
    else:
        print("❌ ID not found\n")


def delete_student():
    df = load_data()

    try:
        student_id = int(input("Enter ID to delete: "))
    except ValueError:
        print("❌ Invalid ID\n")
        return

    if student_id in df["ID"].values:
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() != 'y':
            return

        df = df[df["ID"] != student_id]
        save_data(df)

        print("✅ Deleted\n")
    else:
        print("❌ ID not found\n")


def search_student():
    df = load_data()

    name = input("Enter name to search: ")

    result = df[df["Name"].str.contains(name, case=False, na=False)]

    print("\n--- Results ---")

    if result.empty:
        print("❌ No records found\n")
    else:
        print(result.to_string(index=False))
        print()


# ---------------- MENU ----------------

def menu():
    while True:
        print("===== Student Management System (Excel) =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice\n")


# Run program
menu()