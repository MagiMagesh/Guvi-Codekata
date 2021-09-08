import mysql.connector


while True:
    print('Menu')
    print('1. Add Student in Classroom')
    print('2. Get a Student Details')
    print('3. Get all Student in Classroom')
    print('4. Update or modify a student details in Classroom')
    print('5. Delete a Student detial')
    print('6. Exit')

    input_user = int(input('Enter your Options from above: '))
    if input_user == 1:
        print("The sutdent_id is based on priority")
        student_name = input('Enter Student Name: ')
        student_class = input('Enter Class of Student: ')
        m1 = int(input("Enter the mark of m1"))
        m2 = int(input("Enter the mark of m2"))
        m3 = int(input("Enter the mark of m3"))
        m4 = int(input("Enter the mark of m4"))
        m5 = int(input("Enter the mark of m5"))
        total_marks = m1+m2+m3+m4+m5
        average = int(total_marks)/5
        conc = mysql.connector.connect(host="localhost", user='root', passwd="", database='student')
        cur = conc.cursor()
        cur.execute("INSERT INTO classroom (`student_name`, `student_class`, `m1`, `m2`, `m3`, `m4`, `m5`)")





import mysql.connector

conc = mysql.connector.connect(host="localhost", user='root', passwd="", database='student')
cur = conc.cursor()
cur.execute("INSERT INTO classroom (`student_name`, `student_class`, `m1`, `m2`, `m3`, `m4`, `m5`) VALUES (`student_name`, `student_class`, 85,85,96,774,5)")
cur.execute("SELECT * FROM classroom")

result = cur.fetchall()

for i in result:
    print(i)


#INSERT INTO classroom (`student_name`, `student_class`, `m1`, `m2`, `m3`, `m4`, `m5`) VALUES (`student_name`, `student_class`, 85,85,96,774,5)













import mysql.connector


while True:
    print('Menu')
    print('1. Add Student in Classroom')
    print('2. Get a Student Details')
    print('3. Get all Student in Classroom')
    print('4. Update or modify a student details in Classroom')
    print('5. Delete a Student detial')
    print('6. Exit')

    input_user = int(input('Enter your Options from above: '))
    if input_user == 1:
        print("The sutdent_id is based on priority")
        student_id = int(input('Enter Student_id: '))
        student_name = input('Enter Student Name: ')
        student_class = input('Enter Class of Student: ')
        m1 = int(input("Enter the mark of m1: "))
        m2 = int(input("Enter the mark of m2: "))
        m3 = int(input("Enter the mark of m3: "))
        m4 = int(input("Enter the mark of m4: "))
        m5 = int(input("Enter the mark of m5: "))

        total_marks = m1+m2+m3+m4+m5
        average = int(total_marks)/5
        conc = mysql.connector.connect(host="localhost", user='root', passwd="", database='student')
        cur = conc.cursor()
        #`student_id`, `student_name`, `student_class`, 85, 85, 96, 774, 5, 858
        query = "INSERT INTO classroom VALUES ({},'{}','{}',{},{},{},{},{},{},{})".format(student_id,student_name,student_class,m1,m2,m3,m4,m5,total_marks,average)
        cur.execute(query)
        con.commit

