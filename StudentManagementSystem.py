import mysql.connector

# making database connnection
dbConn = mysql.connector.connect(
					host="localhost", 
					port="3306",
					user="arshad",
					password="password", 
					database="sms")

# Function to Add_Student
def Add_Student():

	studentId = input("Enter Student's Id : ")
	
	# Checking if Student with given Id already exist or not
	if(check_student(studentId) == True):
		print("Student already exists\nTry Again\n\n")
		menu()		
	else:
		studentName = input("Enter Student Name : ")
		english = int (input("Enter English Mark : "))
		maths = int (input("Enter Maths Mark : "))
		physics = int (input("Enter Physics Mark : "))
		chemistry = int (input("Enter Chemistry Mark : "))
		computer = int (input("Enter Computer Mark : "))
		total = english + maths + physics + chemistry + computer		
		average = total / 5
		print ("Total = ",total)
		print ("Average = ",average)
		data = (studentId, studentName, english, maths, physics, chemistry, computer, total, average)
	
		# Inserting Student details into Student table
		sql = 'insert into sms_student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		c = dbConn.cursor()
		
		# Executing the SQL Query
		c.execute(sql, data)
		
		# commit() method to make changes in the table
		dbConn.commit()
		print("Student is added successfully.\n\n")
		menu()

# Function to Update Student
def Update_Student():
	studentId = int(input("Enter Student's Id : "))
	
	# Checking if Student with given Id exist or not
	if(check_student(studentId) == False):
		print("Student does not exists. Try Again\n\n")
		menu()
	else:
		studentName = input("Enter Student Name : ")
		english = int (input("Enter English Mark : "))
		maths = int (input("Enter Maths Mark : "))
		physics = int (input("Enter Physics Mark : "))
		chemistry = int (input("Enter Chemistry Mark : "))
		computer = int (input("Enter Computer Mark : "))
		total = english + maths + physics + chemistry + computer		
		average = total / 5
		print ("Total = ",total)
		print ("Average = ",average)

		cursor = dbConn.cursor()
		
		# Query to Update Record of Student with given Id
		sql = 'update sms_student set student_name=%s,english=%s,maths=%s,physics=%s,chemistry=%s,computer=%s,total=%s, average=%s where student_id=%s'
		data = (studentName, english, maths, physics, chemistry, computer, total, average, studentId)
		
		# Executing the SQL Query
		cursor.execute(sql, data)
		
		# commit() method to make changes in the table
		dbConn.commit()
		print("Student is updated successfully.\n\n")
		menu()

# Function to Remove Student with given Id
def Remove_Student():
	Id = input("Enter Student's Id : ")
	
	# Checking if Student with given Id exist or not
	if(check_student(Id) == False):
		print("Student does not exists.Try Again\n\n")
		menu()
	else:		
		# Query to Delete Student from table
		sql = 'delete from sms_student where student_id=%s'
		data = (Id,)
		c = dbConn.cursor()
		
		# Executing the SQL Query
		c.execute(sql, data)
		
		# commit() method to make changes in the table
		dbConn.commit()
		print("Student is removed successfully.\n\n")
		menu()


# Function To Check if Student with given Id already exist or not
def check_student(student_id):
	
	# Query to select all rows from student Table
	sql = 'select * from sms_student where student_id = %s'
	
	# making cursor buffered to make rowcount method work properly
	cursor = dbConn.cursor(buffered=True)
	data = (student_id,)
	
	# Executing the SQL Query
	cursor.execute(sql, data)
		
	# rowcount method to find number of rows with given values
	rowCount = cursor.rowcount
	if rowCount == 1:
		return True
	else:
		return False

# Function to Display All Students from Student Table
def Display_Students():
	
	# query to select all rows from Student Table
	sql = 'select * from sms_student'
	cursor = dbConn.cursor(buffered=True)
	
	# Executing the SQL Query
	cursor.execute(sql)
	
	count = cursor.rowcount
	if count < 1:
		print ("No students found ...\n\n")

	# Fetching all details of all the Students
	r = cursor.fetchall()
	for i in r:
		print("Student Id : ", i[0])
		print("Student Name : ", i[1])
		print("English : ", i[2])
		print("Maths : ", i[3])
		print("Physics : ", i[4])
		print("Chemistry : ", i[5])
		print("Computer : ", i[6])
		print("Total : ", i[6])
		print("Average : ", i[6])
		print("--------------------------------------\n")
				
	menu()

# menu function to display menu
def menu():
	print("Welcome to Student Management System. Please select the option below (1 - 5):")	
	print("1 - Add Student")
	print("2 - Remove Student ")
	print("3 - Update Student")
	print("4 - Display Students")
	print("5 - Exit")

	choice = int(input("Enter your Choice : "))
	if choice == 1:
		Add_Student()
	elif choice == 2:
		Remove_Student()
	elif choice == 3:
		Update_Student()
	elif choice == 4:
		Display_Students()
	elif choice == 5:
		exit(0)
	else:
		print("Invalid Choice.\n\n")
		menu()

# Calling the menu function
menu()