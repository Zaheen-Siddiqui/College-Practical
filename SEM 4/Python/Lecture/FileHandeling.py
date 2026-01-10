def CheckEmpty(file_path):
        with open(file_path, 'r') as file_obj:
        # read first character
            first_char = file_obj.read(1)

        if not first_char:
            print("File is empty")
            return True
        else:
            print("File is NOT empty")
            return False

f1 = "Sample_File.txt"
f2 = "Sample2.txt"
#Create a file, write some content then display file content
f = open(f1, "w")
#f.write("Hello World")
f = open(f1, "r")
if CheckEmpty(f1):
    Store = f.read()
    print("\nFile after Creation and write:\n"+Store)

#appending data to an existing file
print("\nFile before appending:\n"+Store)
f = open(f1, "a")
f.write("\nHi, how are you")
f = open(f1, "r")
if CheckEmpty(f1):
    Store = f.read()
    print("\nFile after appending:\n"+Store)

#copy content of one file to another
f = open(f1, "r")
if CheckEmpty(f1):
    Store = f.read()
    print("\nContent in orignal file:\n"+Store)
    e = open(f2, "w")
    e.write(Store)
    e = open(f2, "r")
    Store = e.read()
    print("\nContent in copied file:\n"+Store)

#search for a substring in a file 
word = input("\nEnter word to search in file: ")
s = open("Sample_File.txt")
Find = s.readlines()
f_open = 0
for line in Find:
        if word in line:
            print("Word is present in your file")
            f_open += 1

if f_open == 0:
    print("Word is not present in your file")
f.close()
e.close()