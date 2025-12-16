with open("notes.txt", "r", encoding="utf8") as file:
    content = file.read()
    print(content)
    file.close()
    
with open("notes.txt", "w", encoding="utf8") as file:
    while True:
        print("Press 1 to add a note, press 2 to delete a note, press 3 to exit")

        operation = int(input("Select the operation: "))
        print()

        if operation == 1:
            text = input("Enter your note: ")
            file.write(text + "\n")

        if operation == 2:
            text = input("Enter the number of the note you want to delete: ")
            for line in file:
                if str(text + "\n") or str(text) in line
                

        if operation == 3:
            print("\n", "Operation finished")
            break

        file.close()

with open("notes.txt", "r", encoding="utf8") as file:
    content = file.read()
    print(content)
    file.close()
