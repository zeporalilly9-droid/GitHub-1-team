main() 
Start program 
Display menu options 
While user does not choose Exit: 
    Get user choice 
    If choice is Display → call display() 
    If choice is Create → call create() 
    If choice is Read → call read() 
    If choice is Update → call update() 
    If choice is Delete → call delete() 
End program 

display_menu() 
Print menu header 
Print numbered options for Display, Create, Read, Update, Delete, Exit 
get_menu_choice() 
Prompt user to enter a number 
If number is outside valid range: 
    Prompt again 
Return valid choice 

display() 
Connect to student.db 
Query all rows from Student table 
Print formatted table of student data 
Close connection 

create() 
Prompt user for student details 
Connect to student.db 
Insert new student record into Student table 
Confirm success or show error 
Close connection 

 read() 
Prompt user for student ID 
Connect to student.db 
Query Student table for matching ID 
Display student info 
Confirm success or show error 
Close connection 

update() 
Call read() to show current info 
Prompt user for updated student details 
Connect to student.db 
Update record with new info 
Confirm success or show error 
Close connection 

delete() 
Call read() to show current info 
Prompt user for student ID to delete 
Ask for confirmation 
If confirmed: 
    Connect to student.db 
    Delete record 
    Confirm deletion or show error 

Close connection 

 
