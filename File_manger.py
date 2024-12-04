import os
print("================================")

print("Welcome to the File Manager!")

print("================================")

print("1. Create a new file")

print("2. Read an existing file")

print("3. Delete a file")

print("4. List all files")

print("5. Exit")
choice =0
while choice !=5:
    choice = int(input("Enter your choice: "))
    if choice == 1:
       filename=input("Enter name of the file:")
       file=open(filename,"w")
       print("File created successfully!")
       s=input("  :")
       file.write(s)
       file.close()

    elif choice == 2:
        filename=input("Enter name of the file to open:")
        try:
            file=open(filename,"r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("File not found!")

    elif choice == 3: 
        filename=input("Enter filename to delete:")
        os.remove(filename)
   
    elif choice == 4:
        directorypath = r"d:\programming\Python"
        for filename in os.listdir(directorypath):
            print(f"File : '{filename}' ")