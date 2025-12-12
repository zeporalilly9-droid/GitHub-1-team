import sqlite3


def main():
    # Connect to the database (creates student.db if it doesn't exist)
    conn = sqlite3.connect('student.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Add the Student table.
    add_student_table(cur)

    # Add rows to the Student table.
    add_student(cur)

    # Commit the changes.
    conn.commit()

    # Display the Student table.
    display_student(cur)

    # Close the connection.
    conn.close()


# The add_student_table adds the Student table to the database.
def add_student_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Student')

    # Create the table.
    cur.execute('''CREATE TABLE Student (Student_ID TEXT PRIMARY KEY NOT NULL,
                                        First_Name TEXT,
                                        Last_Name TEXT,
                                        Phone_Number TEXT,
                                        Email TEXT,
                                        Credits_Completed INTEGER,
                                        Credits_In_Progress INTEGER)''')


# The add_student function adds rows to the Student table.
def add_student(cur):
    students = [
        ('12345', 'Matthew', 'Johnson', '1963260712', 'matthew.johnson@gmail.com', 31, 16),
        ('67890', 'Mark', 'Thill', '0634891275', 'mark.thill@hotmail.com', 14, 15),
        ('54321', 'Luke', 'Tyler', '7934720571', 'luketyler@gmail.com', 30, 15),
        ('87594', 'John', 'Sullivan', '4907325814', 'johnsullivan@outlook.com', 48, 17)
]

    for row in student_id:
        cur.execute('''INSERT INTO Student VALUES (?, ?, ?, ?, ?, ?, ?)''', row)


# The display_student function displays the contents of
# the Student table.
def display_student(cur):
    print('Contents of student.db/Student table:')
    print('ID-------------First Name-----Last Name------Phone Number---------Email Address--------Credits Completed----Credits In Progress')
    cur.execute('SELECT * FROM Student')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<15}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:<35}{row[5]:<20}{row[6]}')



# Execute the main function.
if __name__ == '__main__':
    main()
