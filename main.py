from pathlib import Path  #This is the library through which i can read the path.
import os

def readfileandfolder():
 path = Path('') #this empty space will give you the current exisiting file directory path
 items = list(path.rglob('*')) #Recursively finds all entries matching path.rglob('*'), the star * means “match anything” — any filename or folder name.
 for i , items in enumerate(items):
    print(f"{i+1} : {items}")

def createfile():
   try:
        readfileandfolder()

        name = input("Please tell you file Name:-  ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs: # (with) block khatam hone par file automatically close ho jaati hai.
                data = input("What you want to write in this file:-  ")
                fs.write(data)
                print("File created sucessfully.. ")
                readfileandfolder()
        else:
                       print("The file already Exists")
   except Exception as err:
        print(f"An error as been as name of {err}")
   
def readfile():
     try:
        readfileandfolder()
        name = input("Please enter your file name:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)

                print("readed sucessfully")

        else:
            print("No such file exists")
     except Exception as err:
          print(f"An error has been occured of name {err}")

def updatefile():
     try:
        readfileandfolder()
        name = input("Which file you want to update - ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file - ")
            print("Press 2 overwriting the data of your file")
            print("press 3 for appending content in your file")
            res = int(input("Tell your response - "))
            if res == 1:
                name2 = input("Tell your New file name")
                p2 = Path(name2)
                p.rename(p2)
            if res ==2:
                with open(p, 'w') as fs:
                        data = input("This overwrting place ,write you want to overwrite")
                        fs.write(data)  

            if res ==3:
                with open(p, 'a') as fs:
                                    data = input("Tell what you want to append")
                                    fs.write(data) 
     except Exception as err:
          print(f"The error has been occured of name {err}")
                        

def deletefile():
     try:
        readfileandfolder()
        name = input("Which file u want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
            print("Removed sucessfully ")
            
        else:
            print("No such fle exists ")
     except Exception as err:
          print(f"A error as been found as name of {err}")
                
                                 

print("Press 1 for Creation of file ")
print("Press 2 for Reading of file")
print("Press 3 for updating a file")
print("Press 4 for Deletion of a file")

check = int(input("Please tell your response - "))

if check ==1:
    createfile()

if check==2:
     readfile()

if check==3:
     updatefile()

if check == 4:
     deletefile()