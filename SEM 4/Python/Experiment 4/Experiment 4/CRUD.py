import sqlite3
conn = sqlite3.connect("Employee")
cursor = conn.cursor()
print("Opened Database successfully")
cursor.execute("create table EmpRes (ItemID int primary key, ItemName char(50), cost int)")
cursor.execute("insert into EmpRes (ItemID, ItemName, cost) values (101, 'Monitor', 10000)")
cursor.execute("insert into EmpRes (ItemID, ItemName, cost) values (102, 'Keyboard', 5000)")
cursor.execute("insert into EmpRes (ItemID, ItemName, cost) values (103, 'Mouse   ', 2500)")
print("ItemID\tItemName\tcost")
for row in cursor.execute("select ItemID, ItemName, cost from EmpRes"):
	print(row[0],"\t",row[1],"\t",row[2])
cursor.close()
conn.commit()
conn.close()
