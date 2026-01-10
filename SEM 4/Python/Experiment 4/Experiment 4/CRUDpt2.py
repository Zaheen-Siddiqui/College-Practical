import sqlite3
conn = sqlite3.connect("Employee")
cursor = conn.cursor()
print("Opened Database successfully")
print("\nBefore Update\n")
print("ItemID\tItemName\tcost")
for row in cursor.execute("select ItemID, ItemName, cost from EmpRes"):
	print(row[0],"\t",row[1],"\t",row[2])
cursor.execute("update EmpRes set cost  = 15000 where ItemID = 101")
print("\nAfter Update\n")
print("ItemID\tItemName\tcost")
for row in cursor.execute("select ItemID, ItemName, cost from EmpRes"):
	print(row[0],"\t",row[1],"\t",row[2])
cursor.close()
conn.commit()
conn.close()
