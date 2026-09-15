# creating of file and writing few lines of text in it. and then reading the file and printing the content. 
# then adding (appending) few more lines to the same file and then reading the file afain and printing the content. 


with open("file_name.txt", "w") as file:  
    file.write("this is a line of text")
    file.write("\nthis is another line of text")
    file.write("\nthis is yet another line of text")

with open("file_name.txt", "r") as file:
    content = file.read()
    print(content)

print("\n")

with open("file_name.txt", "a") as file:
    file.write("\nthis is an appended line of text")

with open("file_name.txt", "r") as file:
    content = file.read()
    print(content)



with open("journal.txt", "w") as file_assignment:
    file_assignment.write("Day 1: Started learning Python\n")
    file_assignment.write("Day 2: Went for a run\n")
    file_assignment.write("Day 3: Built my first Python script\n")

print("\n")

with open("journal.txt", "a") as file_assignment:
    file_assignment.write("Day 4: Had coffee with a friend\n")
    file_assignment.write("Day 5: Completed a Python project\n")
    file_assignment.write("Day 6: Read a book\n")

with open("journal.txt", "r") as file_assignment:
    reading_file_content = file_assignment.read()
    print(reading_file_content)

### Problem 3

# You want to look back at your Python-related entries. Using context managers (`with` statements), read `journal.txt` and create a new file called `python_entries.txt` containing only the entries that mention `"Python"`. Then read the new file back and print its contents.
print("\n")

with open("journal.txt", "r") as file_assignment, open("python_entries.txt", "w") as python_file:
    for line in file_assignment:
        if "Python" in line:
            python_file.write(line)

with open("python_entries.txt", "r") as python_word_file:
    print(python_word_file.read())