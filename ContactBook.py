import os
import sys

__author__ = "Nicolas de Moura"
__version__ = 1.0
__date__ = "29/03/2022"

class Database:
    def __init__(self):
        os.system("date /t")
        if os.system("dir /b database.txt"):
            print("Creating database.txt...")
            os.system('echo > database.txt')
            self.file = open("database.txt", "w")
            self.file.write("Name  Age  PhoneNumber  Email\n")
            self.file.close()
            print("File created")
        else:
            print("Database.txt was find.")
            self.file = open("database.txt")
            print("File loaded")
            self.file.close()
    def newEntry(self):
        self.file = open("database.txt", "a")
        name = str(input("Name: "))
        age = str(input("Age: "))
        phone_number = str(input("Phone number: "))
        email = str(input("Email: "))
        self.file.write(f"{name}  {age}  {phone_number}  {email}\n")
        self.file.close()
    def readEntry(self):
        command = int(input("Type 1 to simple read or 2 to notepad read: "))
        self.file = open("database.txt", "r")
        if command == 1:
            print(self.file.read())
            self.file.close()
        elif command == 2:
            os.system("notepad database.txt")
            self.file.close()
    def removeEntry(self):
        try:
            self.file = open("database.txt", "r")
            lines = self.file.readlines()
            self.file.close()
            to_delete = int(input("Which line do you want to delete?: "))
            try:
                if to_delete == 0:
                    print("Is not possible to delete the header row")  
                elif to_delete != 0:
                    del lines[to_delete]
                    new_file = open("database.txt", "w")
                    for line in lines:
                        new_file.write(line)
                    new_file.close()
            except IndexError:
                print(f"There are no line with the index {to_delete}")
                print("Please keep in mind that the index beggins with 0")
        except:
            print("Something occured and was not possible to conclude the process")
    def stats(self):
        print("The file stats are:")
        os.system("dir ./database.txt")
if __name__ == "__main__":
    db = Database()
    while True:
        command = str(input('''\n\t\tType new to new entry
        \tType read to read entry
        \tType remove to remove entry
        \tType show to show stats from your database
        \tType e to exit\n>>>''')).lower()
        if command == "new":
            db.newEntry()
        elif command == "read":
            db.readEntry()
        elif command == "show":
            db.stats()
        elif command == "remove":
            db.removeEntry()
        elif command == "e":
            sys.exit()
        else:
            print(f"{command} is not recognized as a command")
