import sqlite3
conn = sqlite3.connect("Employee")
cursor = conn.cursor()
print("Opened Database successfully")
cursor.execute("create table Emp (EmpID int primary key, Name char(50), Salary int)")
data = [(1, 'Zaheen', 1000000) , (2, 'Parth', 1000000) , (3, 'Vinay', 1000000)]
cursor.executemany("insert into Emp values (?,?,?)",data)
print("EmpID\tName\tSalary")
for row in cursor.execute("select EmpID, Name, Salary from Emp"):
	print(row[0],"\t",row[1],"\t",row[2])
cursor.close()
conn.commit()
conn.close()
