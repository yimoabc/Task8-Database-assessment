
#import

import sqlite3







#function











#main code
connec = sqlite3.connect("Student Grade Tracker Database.db")  #connect to the database
helper = connec.cursor()                                       #create a cursor object to execute SQL commands

helper.execute("SELECT * FROM Grade_tracker")                  #execute the commands
data = helper.fetchall()                                       #collect all the data



def print_grade_sorter(data_that_userneed=None):
    if data_that_userneed is None:
        sql_input = "SELECT * FROM Grade_tracker"

    else:
        sql_input = f"SELECT * FROM Grade_tracker ORDER BY {data_that_userneed} DESC;"
    helper.execute(sql_input)
    results = helper.fetchall()

    if data_that_userneed == "exam_name":
        print("student id     name   year level      subject                   score    grade        exam_name")
    elif data_that_userneed == "status":
        print("student id     name   year level      subject                   score    grade      status")
    elif data_that_userneed == "assignment_type":
        print("student id     name   year level      subject                   score    grade       assignment_type")
    else:
       print("student id     name   year level      subject                   score    grade")
    for data in results:

        normal_form =(f"{data[0]:<15}{data[1]:10}{data[2]:<10}{data[3]:<30}{data[7]:<10}{data[8]:<8}")

        if data_that_userneed == "exam_name":
            print(normal_form + f" | Exam: {data[4]}")
        elif data_that_userneed == "status":
            print(normal_form + f" | Status: {data[5]}")
        elif data_that_userneed == "assignment_type":
            print(normal_form + f" | Type: {data[6]}")
        else:
            print(normal_form)
while True:
    try:
        read_or_write = input("\nDo you like read or write\n1.write\n2.read\n3.exit\n")
        
        if read_or_write == "2":

            user_want = (input("\nWhat data would you like to see?\n1. Sort by [Student ID]\n2. Sort by [Student Name]\n3. Sort by [Year Level]\n4. Sort by [Subject]\n5. Sort by [Exam Name] (Extra Show)\n6. Sort by [Status] (Extra Show)\n7. Sort by [Assignment Type] (Extra Show)\n8. Sort by [Score]\n9. Sort by [Grade]\n Please enter the answer in number\n"))
            if user_want == "1":
                    print_grade_sorter()
            elif user_want == "2":
                    print_grade_sorter()
            elif user_want == "3":
                    print_grade_sorter()
            elif user_want == "4":
                    print_grade_sorter()
            else:
                    print("\nPlease enter a valid number") 

        if read_or_write == "3":
            break

        else:
                    print("\nPlease enter a valid number") 
        
    except ValueError:
           print("Please enter a valid number") 