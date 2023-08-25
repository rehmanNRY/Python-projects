# Library management system
class Library:
    def __init__(self,books_list):
        self.books_list = books_list
    def list_of_books(self):
        print("\nList of avalible Books")
        for book in self.books_list:
            print("* ", book)
        print("")
    def borrow_a_book(self):
        book_to_borrow = input("==> Need book? Enter title: ")
        if book_to_borrow in self.books_list:
            print(f"\nBorrowed {book_to_borrow}, care, return early!\n")
            self.books_list.remove(book_to_borrow)
        else:
            print("\nTaken or absent, sorry\n")
    def return_a_book(self):
        book_to_add = input("==> Input book name to return/add: ")
        if book_to_add in self.books_list:
            print(f"\nBook {book_to_add} already in. Thanks\n")
        else:
            self.books_list.append(book_to_add)
            print(f"\nGot the book {book_to_add}. Many thanks.\n")
print("============ Welcome to my library ============")
books_avalible = ["C","C++","Python","HTML","CSS"]
while(True):
    print('''************ Please choose a option ************
==> 1. List of all books
==> 2. Borrow a book
==> 3. Add/Return a book
==> 4. Exit form Library ''')
    option_selected = input("==> Enter your choice: ")
    try:
        option_selected = int(option_selected)
    except ValueError:
        pass
    library = Library(books_avalible)
    if option_selected==1:
        library.list_of_books()
        library.borrow_a_book()
    elif option_selected==2:
        library.borrow_a_book()
    elif option_selected==3:
        library.return_a_book()
    elif option_selected==4:
        print("\nGood Bye! Visit again shortly\n")
        exit()
    else:
        print("\nInvalid selection, choose again.\n")