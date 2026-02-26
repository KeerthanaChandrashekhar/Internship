try: 
    file = open("missing_file.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("The file you are trying to read does not exist.")
    
except PermissionError:
    print("You do not have permission to read this file.")
    
except Exception as e:
    print("An unexpected error occurred:", e)