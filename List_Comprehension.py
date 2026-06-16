# list comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
list_1 = [1,2,3,4,5]

squared_list = []
for i in list_1:
    square = i ** 2
    squared_list.append(square)
print(squared_list)

squared_list = [i ** 2 for i in list_1]
print(squared_list)

with open("python_entries.txt", "a") as python_file:
    python_file.write(str(squared_list)+"\n")


tv_shows = ["breaking bad", "game of Thrones", "stranger Things", "The Crown", "The Mandalorian", "The office"]


captalised_tv_shows = [i.title() for i in tv_shows if len(i) >=10]
print(captalised_tv_shows)
    
with open("python_entries.txt", "a") as python_file:
    python_file.write(str(captalised_tv_shows))
