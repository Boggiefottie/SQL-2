#pip install mysql-connector-python

import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database=''
)
cursor = conn.cursor()

# Create a student table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        roll INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        marks INT
    )''')

def insert():
    name1 = input("Enter name: ")
    marks1 = int(input("Enter marks: "))
    cursor.execute("INSERT INTO student (name, marks) VALUES (%s, %s)", (name1, marks1))
    conn.commit()
    print("Record inserted successfully")

def remove():
    roll = int(input("Enter roll no to delete: "))
    cursor.execute("DELETE FROM student WHERE roll = %s", (roll,))
    if cursor.rowcount == 0:
        print("Record does not exist")
    else:
        print("Record deleted successfully")
    conn.commit()

def update():
    roll = int(input("Enter roll no to update: "))
    marks = int(input("Enter new marks: "))
    cursor.execute("UPDATE student SET marks = %s WHERE roll = %s", (marks, roll))
    if cursor.rowcount == 0:
        print("Record does not exist")
    else:
        print("Record updated successfully")
    conn.commit()

def display_all():
    cursor.execute("SELECT * FROM student")
    records = cursor.fetchall()
    if not records:
        print("No records found")
    else:
        print("All Records:")
        for record in records:
            print(record)

def search_records():
    roll = int(input("Enter roll no to search: "))
    cursor.execute("SELECT * FROM student WHERE roll = %s", (roll,))
    records = cursor.fetchall()
    if not records:
        print("No matching records found")
    else:
        print("Matching Records:")
        for record in records:
            print(record)

def main():
    while True:
        print("-----------------------------------------------------")
        print("\t1.Insert")
        print("\t2.Update")
        print("\t3.Delete")
        print("\t4.Display All Records")
        print("\t5.Search Records")
        print("\t6.Exit")
        ch = int(input("Enter your choice here: "))
        if ch == 1:
            insert()
        elif ch == 2:
            update()
        elif ch == 3:
            remove()
        elif ch == 4:
            display_all()
        elif ch == 5:
            search_records()
        else:
            conn.close()
            break

main()
