with open("data.txt","r") as file:
    for line in file:
      if line.strip():
        cleaned_line = line.strip()
        print(cleaned_line.lower())