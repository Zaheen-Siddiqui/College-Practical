import sqlite3
conn = sqlite3.connect("Employee")
cursor = conn.cursor()
print("Opened Database successfully")
print("\nBefore Update\n")
print("ItemID\tItemName\tcost")
for row in cursor.execute("select ItemID, ItemName, cost from EmpRes"):
	print(row[0],"\t",row[1],"\t",row[2])
cursor.execute("delete from EmpRes where ItemID = 101")
print("\nAfter Update\n")
print("ItemID\tItemName\tcost")
for row in cursor.execute("select ItemID, ItemName, cost from EmpRes"):
	print(row[0],"\t",row[1],"\t",row[2])
cursor.close()
conn.commit()
conn.close()
