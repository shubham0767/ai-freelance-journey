books = []

def add_book():
    book = input("Enter Book Name: ")
    books.append(book)
    print("Book Added!")

def issue_book():
    book = input("Enter Book to Issue: ")

    if book in books:
        books.remove(book)
        print("Book Issued.")
    else:
        print("Book Not Available.")

def return_book():
    book = input("Enter Book to Return: ")
    books.append(book)
    print("Book Returned.")

def view_books():
    if len(books) == 0:
        print("Library Empty.")
    else:
        print("\nBooks:")
        for book in books:
            print(book)

while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View Books")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        view_books()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")