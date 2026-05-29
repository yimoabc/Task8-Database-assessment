#import
import sqlite3 #Import sqlite3 module to connect Python with the database.

#function
connec = sqlite3.connect("Student Grade Tracker Database.db")  #connect to the database
helper = connec.cursor()                                       #create a cursor object to execute SQL commands

#name the menu to make the code more readable
MENU_WRITE_1 = "1"
MENU_READ_ALL_2 = "2"
MENU_SEARCH_3 = "3"
MENU_EXIT_4 = "4"

#name the search type to make the code more readable
SEARCH_SINGLE_1 = "1"
SEARCH_DOUBLE_2 = "2"
SEARCH_BACK_3 = "3"

#name the column to make the code more readable
col_student_id = "student_id"
col_student_name = "student_name"
col_year_level = "year_level"
col_subject = "subject"
col_exam_name = "exam_name"
col_status = "status"
col_assignment_type = "assignment_type"
col_score = "score"
col_grade = "grade"

#create a function to sort the data
# name the function "print_grade_sorter" and create a blank placeholder with data_that_userneed=None, "none" tell the system it's completely blank.   
def print_grade_sorter(data_that_userneed=None):
    
    # check if item input in the function is blank
    if data_that_userneed is None:
        #if it's blank, select everythring from grade tracker without any order
        sql_input = "SELECT * FROM Grade_tracker"
    else:
        #if the item in the function is something else, select everything that order by the item in function
        sql_input = f"SELECT * FROM Grade_tracker ORDER BY {data_that_userneed} DESC;"
    
    #make helper to execute the result we get through the process
    helper.execute(sql_input)
    
    # save the result that was collect by helper as a variable 
    results = helper.fetchall()
    print("\n------Read data ordered by column name------\n")
    #check if we need to output normal form or do we need to as extra column
    #(I set up a normal form to make the data more concise and excluding unnecessary information)
    if data_that_userneed == col_exam_name:
    
    # if user want to order the result by our hidden column
    # , make sure the title can be shown
        print("studentid  name  yearlevel     subject          score  grade     exam_name")
    
    elif data_that_userneed == col_status:
        print("studentid  name  yearlevel     subject          score  grade     status")
   
    elif data_that_userneed == col_assignment_type:
        print("studentid  name  yearlevel     subject          score  grade     assignment_type")
    else:
       print("studentid  name  yearlevel     subject           score  grade")
    
    #after the diterminatin, ready to print each data (that in results that we collect)
    for data in results:
       
    #save the normal form as a variable so we can use it after more efficiently.
        normal_form =(f"{data[0]:<10}{data[1]:<10}{data[2]:<4}{data[3]:<25}{data[7]:<6}{data[8]:<4}")
    #show the normal form plus the hidden information that user required
        if data_that_userneed == col_exam_name:
            print(normal_form + f" | Exam: {data[4]}")
        elif data_that_userneed == col_status:
            print(normal_form + f" | Status: {data[5]}")
        elif data_that_userneed == col_assignment_type:
            print(normal_form + f" | Type: {data[6]}")
    #if user didn't required print out the normal form
        else:
            print(normal_form)

# name the function "insert_new_grade" 
# and create few blank placeholder for user's new upload data information 
def insert_new_grade(id, name, year, subject, e_name, status, type, score, grade):  
    
    #save the command to a variable so it can be call it by helper
    # and use ? as the placeholder for datas user input
    upload_to_sql = ("INSERT INTO Grade_Tracker (student_id, student_name, year_level, subject, exam_name, status, assignment_type, score, grade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);")
    
    #Make helper to execute data to databse world
    helper.execute(upload_to_sql, (id, name, year, subject, e_name, status, type, score, grade))
    
    #connect to databse and update the data we get
    connec.commit()

#define a fuction for single column search and add two placeholder
def single_subject_search(column_name, user_input):
    code_select_user_id = f"SELECT * FROM Grade_tracker WHERE {column_name} = ?;"
    results = helper.execute(code_select_user_id, (user_input,)).fetchall()
    #no results
    if not results:
        print(f"\nNo items found with {user_input}")
    else:
        print("\nSearch have complete\n")
        print("------------------------Search-Result-------------------------")
        print("studentid|  name  |yearlevel|     subject           |score | grade")
        for data in results:
            print(f"{data[0]:<10}{data[1]:<10}{data[2]:<10}{data[3]:<25}{data[7]:<6}{data[8]:<4}")
            print(f"Exam name: {data[4]:<10}|Status: {data[5]:<10}|Assignment type: {data[6]:<10}\n")

#define a fuction for double column search and add four placeholder
def double_subject_search(column_name, column_name_2, user_input, user_input_2):
    code_select_to_input = f"SELECT * FROM Grade_tracker WHERE {column_name} = ? AND {column_name_2} = ?"
    results = helper.execute(code_select_to_input, (user_input, user_input_2)).fetchall() 
    if not results:
        print(f"\nNo items found with {user_input, user_input_2}")
    else:
        print("\nSearch have complete\n")
        print("------------------------Search-Result-------------------------")
        print("studentid|  name  |yearlevel|     subject           |score | grade")
        for data in results:
            print(f"{data[0]:<10}{data[1]:<10}{data[2]:<10}{data[3]:<25}{data[7]:<6}{data[8]:<4}")
            print(f"Exam name: {data[4]:<10}|Status: {data[5]:<10}|Assignment type: {data[6]:<10}\n")
         
#main code
while True:
    try:
        # Ask the user what operation they want to perform on the data 
        read_or_write = input("\nDo you like read information or upload data\n1.upload data\n2.View and sort all records\n3.enter to search specific data from specific column\n4.exit\n")
        #Check if user input valid answer(1,2,3,4)
        if read_or_write in [MENU_WRITE_1, MENU_READ_ALL_2, MENU_SEARCH_3, MENU_EXIT_4]:

            if read_or_write == MENU_WRITE_1:
                tem_id = int(input("Please enter the user id ").strip())
                tem_name = input("Please enter the name ").strip()
                tem_year = int(input("Please enter the year level ").strip())
                tem_subject = input("Please enter the subject ").strip()
                tem_e_name = input("Please enter the exam name ").strip()
                tem_status = input("Please enter the status ").strip()
                tem_type = input("Please enter the assignment type ").strip()
                tem_score = int(input("Please enter the score ").strip())
                tem_grade = input("Please enter the grade ").strip()
                
                data_need_upload = (tem_id, tem_name, tem_year, tem_subject, tem_e_name, tem_status, tem_type, tem_score, tem_grade)
                insert_new_grade(*data_need_upload)
                print("Updates have saved")

            if read_or_write == MENU_READ_ALL_2:
                user_want = input("\nWhat data would you like to see?\n1. Sort by [Student ID]\n2. Sort by [Student Name]\n3. Sort by [Year Level]\n4. Sort by [Subject]\n5. Sort by [Exam Name] (Extra Show)\n6. Sort by [Status] (Extra Show)\n7. Sort by [Assignment Type] (Extra Show)\n8. Sort by [Score]\n9. Sort by [Grade]\n10. Go back\n Please enter the answer in number\n")
                if user_want == "1":
                        print_grade_sorter()
                elif user_want == "2":
                        print_grade_sorter(col_student_name)
                elif user_want == "3":
                        print_grade_sorter(col_year_level)
                elif user_want == "4":
                        print_grade_sorter(col_subject)
                elif user_want == "5":
                        print_grade_sorter(col_exam_name)
                elif user_want == "6":
                        print_grade_sorter(col_status)
                elif user_want == "7":
                        print_grade_sorter(col_assignment_type)
                elif user_want == "8":
                        print_grade_sorter(col_score)
                elif user_want == "9":
                        print_grade_sorter(col_grade)
                elif user_want == "10":
                        continue
                else:
                        print("\nPlease enter a valid number") 
            
            if read_or_write == MENU_SEARCH_3:
                Kind_of_search = input("\nWhich kind of search?\n1. single subject search\n2. double subject search\n3. go back\n")

                if Kind_of_search == SEARCH_SINGLE_1:
                    search = input("\nWhich item you like to search\n1. student id\n2. student name\n3. year level\n4. subject\n5. exam name\n6. status\n7. assignment type\n8. score\n9. grade\n10. Go back\n")   
                    
                    if search == "1":
                        user_input = input("Please enter the student id (e.g. 10000) ").strip()
                        single_subject_search(col_student_id, user_input)
                    elif search == "2":
                        user_input = input("Please enter the student name (e.g. Zack) ").strip()
                        single_subject_search(col_student_name, user_input)
                    elif search == "3":
                        user_input = input("Please enter the year level (e.g. 11) ").strip()
                        single_subject_search(col_year_level, user_input)
                    elif search == "4":
                        user_input = input("Please enter the subject (e.g. Digital Technologies) ").strip()
                        single_subject_search(col_subject, user_input)
                    elif search == "5":
                        user_input = input("Please enter the exam name (e.g. AS92004) ").strip()
                        single_subject_search(col_exam_name, user_input)
                    elif search == "6":
                        user_input = input("Please enter the status (e.g. Internal) ").strip()
                        single_subject_search(col_status, user_input)
                    elif search == "7":
                        user_input = input("Please enter the assignment type (e.g. Project) ").strip()
                        single_subject_search(col_assignment_type, user_input)
                    elif search == "8":
                        user_input = input("Please enter the score (e.g. 85) ").strip()
                        single_subject_search(col_score, user_input)
                    elif search == "9":
                        user_input = input("Please enter the grade (e.g. E) ").strip()
                        single_subject_search(col_grade, user_input)
                    elif search == "10":
                        continue
                    else:
                        print("\nPlease enter a valid number")
                #when user input 2 to search two subject
                elif Kind_of_search == SEARCH_DOUBLE_2:
                    #ask user what they want to search for the first subject
                    search1 = input("\nWhich item you like to search\n1. student id\n2. student name\n3. year level\n4. subject\n5. exam name\n6. status\n7. assignment type\n8. score\n9. grade\n10. Go back\n")   
                    #if they input 1 
                    if search1 == "1":
                        #let user to input student id
                        User_search1 = input("Please enter the student id (e.g. 10000) ").strip()
                        column_name_1 = col_student_id
                    elif search1 == "2":
                        User_search1 = input("Please enter the student name (e.g. Zack) ").strip()
                        column_name_1 = col_student_name
                    elif search1 == "3":
                        User_search1 = input("Please enter the year level (e.g. 11) ").strip()
                        column_name_1 = col_year_level
                    elif search1 == "4":
                        User_search1 = input("Please enter the subject (e.g. Digital Technologies) ").strip()
                        column_name_1 = col_subject
                    elif search1 == "5":
                        User_search1 = input("Please enter the exam name (e.g. AS92004) ").strip()
                        column_name_1 = col_exam_name
                    elif search1 == "6":
                        User_search1 = input("Please enter the status (e.g. Internal) ").strip()
                        column_name_1 = col_status
                    elif search1 == "7":
                        User_search1 = input("Please enter the assignment type (e.g. Project) ").strip()
                        column_name_1 = col_assignment_type
                    elif search1 == "8":
                        User_search1 = input("Please enter the score (e.g. 85) ").strip()
                        column_name_1 = col_score
                    elif search1 == "9":
                        User_search1 = input("Please enter the grade (e.g. E) ").strip()
                        column_name_1 = col_grade
                    elif search1 == "10":
                        continue
                    else:
                        print("\nPlease enter a valid number")
                        continue

                    search2 = input("\nWhich item you like to search\n1. student id\n2. student name\n3. year level\n4. subject\n5. exam name\n6. status\n7. assignment type\n8. score\n9. grade\n10. Go back\n")   
                    
                    if search2 == "1":
                        User_search2 = input("Please enter the student id (e.g. 10000) ").strip()
                        column_name_2 = col_student_id
                    elif search2 == "2":
                        User_search2 = input("Please enter the student name (e.g. Zack) ").strip()
                        column_name_2 = col_student_name
                    elif search2 == "3":
                        User_search2 = input("Please enter the year level (e.g. 11) ").strip()
                        column_name_2 = col_year_level
                    elif search2 == "4":
                        User_search2 = input("Please enter the subject (e.g. Digital Technologies) ").strip()
                        column_name_2 = col_subject
                    elif search2 == "5":
                        User_search2 = input("Please enter the exam name (e.g. AS92004) ").strip()
                        column_name_2 = col_exam_name
                    elif search2 == "6":
                        User_search2 = input("Please enter the status (e.g. Internal) ").strip()
                        column_name_2 = col_status
                    elif search2 == "7":
                        User_search2 = input("Please enter the assignment type (e.g. Project) ").strip()
                        column_name_2 = col_assignment_type
                    elif search2 == "8":
                        User_search2 = input("Please enter the score (e.g. 85) ").strip()
                        column_name_2 = col_score
                    elif search2 == "9":
                        User_search2 = input("Please enter the grade (e.g. E) ").strip()
                        column_name_2 = col_grade
                    elif search2 == "10":
                        continue
                    else:
                        print("\nPlease enter a valid number")
                        continue

                    double_subject_search(column_name_1, column_name_2, User_search1, User_search2)
                #back to the choosing when user input3
                elif Kind_of_search == SEARCH_BACK_3:
                    continue
            #stop the code when user input 4 and exit
            if read_or_write == MENU_EXIT_4:
                break
        # if not, tell them to enter valid number and start again
        else:
            print("\nPlease enter a valid number ") 
    #Catch when user input letter to a int() function   
    except ValueError:
        print("Please enter a valid number ")