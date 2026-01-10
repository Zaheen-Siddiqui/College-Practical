import sqlite3
conn = sqlite3.connect("Employee")
cursor = conn.cursor()
print("Opened Database successfully")
cursor.execute("create table EmpRes (ItemID int primary key, ItemName char(50), cost int)")
data = []
row = []
flag = True
while (flag)
	print("1.Insert\n2.Delete\n3.Update
