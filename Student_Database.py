import sqlite3

# Assigns numbers to options
MIN_CHOICE = 1
MAX_CHOICE = 6
DISPLAY = 1
CREATE = 2
READ = 3
UPDATE = 4
DELETE = 5
EXIT = 6

def main():

    choice = 0
    display_menu()
    while choice != EXIT:
        choice = get_menu_choice()
        if choice == DISPLAY:
            display()
        if choice == CREATE:
            create()
        if choice == READ:
            read()
        if choice == UPDATE:
            update()
        if choice == DELETE:
            delete()

# Displays options
def display_menu():
    print("---Student Database Menu---")
    print("Enter the number of the function you wish to execute:")
    print("1. Display student database\n"
          "2. Create a new student ID\n"
          "3. Read a student ID\n"
          "4. Update a student ID\n"
          "5. Delete a student ID\n"
          "6. Exit")

# Gets user choice
def get_menu_choice():
    choice = int(input("Enter your choice: "))

    if choice < MIN_CHOICE or choice > MAX_CHOICE:
        print("Enter a valid choice.")
        choice = int(input("Enter your choice: "))

    return choice

# Displays all contents of the Student table.
def display():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    print('Contents of student.db/Student table:')
    print('ID-------------First Name-----Last Name------Phone Number---------Email Address--------Credits Completed----Credits In Progress')
    cur.execute('SELECT * FROM Student')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<15}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:<35}{row[5]:<20}{row[6]}')
    conn.commit()

# Creates a new student ID and corresponding information
def create():
    student_id = input("Enter student ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    credits_completed = input("Enter the number of credits completed: ")
    credits_in_progress = input("Enter the number of credits in progress: ")
    conn = None
    try:
        conn = sqlite3.connect('student.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO Student (Student_ID, First_Name, Last_Name, Phone_Number, Email, Credits_Completed, Credits_In_Progress) VALUES (?, ?, ?, ?, ?, ?, ?)", (student_id, first_name, last_name, phone_number, email, credits_completed, credits_in_progress))
        conn.commit()
        print('Successfully updated student database.')
    except sqlite3.Error as err:
        print("Database Error:", err)
    finally:
        if conn is not None:
            conn.close()

# Asks user for student ID and reads corresponding information
def read():
    student_id = input("Enter student id associated with student you are looking for: ")
    conn = None
    try:
        conn = sqlite3.connect('student.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Student WHERE Student_ID = ?", (student_id,))
        results = cur.fetchall()
        for row in results:
            print('ID-------------First Name-----Last Name------Phone Number---------Email Address--------Credits Completed----Credits In Progress')
            print(f'{row[0]:<15}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:<35}{row[5]:<20}{row[6]}')
        print('Successfully read student database.')
    except sqlite3.Error as err:
        print("Database Error:", err)
    finally:
        if conn is not None:
            conn.close()

# Calls read function, then asks user for student ID and gets user input to update information
def update():
    read()
    student_id = input("Enter the student id associated with student information you would like to change: ")
    first_name = input("Enter (new) first name: ")
    last_name = input("Enter (new) last name: ")
    phone_number = input("Enter (new) phone number: ")
    email = input("Enter (new) email: ")
    credits_completed = int(input("Enter the (new) number of credits completed: "))
    credits_in_progress = int(input("Enter the (new) number of credits in progress: "))
    conn = None
    try:
        conn = sqlite3.connect('student.db')
        cur = conn.cursor()
        cur.execute("UPDATE Student SET First_Name = ?, Last_Name = ?, Phone_Number = ?, Email = ?, Credits_Completed = ?, Credits_In_Progress = ? WHERE Student_ID = ?", (first_name, last_name, phone_number, email, credits_completed, credits_in_progress, student_id))
        conn.commit()
        print('Successfully updated student database.')
    except sqlite3.Error as err:
        print("Database Error:", err)
    finally:
        if conn is not None:
            conn.close()

# Calls read function, then asks user for student ID to delete and confirms deletion
def delete():
    read()
    student_id = input("Enter the student id you would like to delete: ")
    sure = input("Are you sure you want to delete this student information? (y/n): ")
    if sure.lower() == "y":
        conn = None
        try:
            conn = sqlite3.connect('student.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM Student WHERE Student_ID = ?", (student_id,))
            conn.commit()
            id_deleted = cur.rowcount
            print("Deleted {} row(s)".format(id_deleted))
        except sqlite3.Error as err:
            print("Database Error:", err)
        finally:
            if conn is not None:
                conn.close()


if __name__ == "__main__":
    main()