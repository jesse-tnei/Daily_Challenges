available_books = {
            1: "The Great Gatsby",
            2: "To Kill a Mockingbird",
            3: "1984",
            4: "Pride and Prejudice"
        }

available_books_2 = {
            10: "The Great Gatsby",
            21: "To Kill a Mockingbird",
            31: "1984",
            14: "Pride and Prejudice"
        }
print(type(available_books))
print(available_books.keys())
for i in available_books.keys():
    print(i, available_books[i])


print(len(available_books))

print(1 in available_books.keys() or 1 in available_books_2.keys())
