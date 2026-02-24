filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
        
except FileNotFoundError:
    print("The file you are trying to read does not exist.")
    
except PermissionError:
    print("You do not have permission to read this file.")
    
except Exception as e:
    print("An unexpected error occurred:", e)
