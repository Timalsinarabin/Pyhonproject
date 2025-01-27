class Library:
    def __init__(self):
        self.books=[{"name":"A Tale of Two Cities","author":"Charles Dickens"},
                    {"name":"The Little Prince","author":"Antoine de Saint-Exupéry"},
                    {"name": "The hobbit", "author": "	J. R. R. Tolkien"},
                    {"name": "The Alchemist", "author": "Paulo Coelho"},
                    {"name": "Harry Porter", "author": "J. K. Rowling"},
                    {"name": "Dream", "author": "Anton"},
                    ]
    def displayallbooks(self):
        for book in self.books:
            print(f"\nTitle: {book['name']} \nAuthor: {book['author']}")

    def displaysearchedbook(self,title):
        for book in self.books:
            if book["name"].lower()==title.lower():
                print(f"The book '{title}' is available")
                return True
        print(f"The book '{title}' is not available")
        return False

class Person:
    def __init__(self,person_name):
        self.borrowedbook = []
        self.name=person_name

    def borrowbook(self,title):
        c=input("Do you want to return (Y/N): ")
        if c.lower()=='y':
            self.borrowedbook.append(title)
        else:
            print("Book not borrowed.")

    def returnbook(self,title):
        if title in self.borrowedbook:
            c=input("Do you want to return (Y/N): ")
            if c.lower()=='y':
                self.borrowedbook.remove(title)
                print("The book returned sucessfully.")
            else:
                print("Book not returned.")
        else:
            print("No borrowed book.")

    def vborrow(self):
        if self.borrowedbook:
            print(f"Borrowed books:{self.borrowedbook}")
        else:
            print("No borrowed boook.")

Lib = Library()
name=input("Enter your name:")
borrowlimit=2
user = Person(name)
while True:
    print("\n1.Display all book \n2.Search a Book \n3.Borrow a book \n4.Return a book \n5.View borrow books \n6.Exit")
    choice=int(input("Select an option (1-6): "))

    if choice==1:
        Lib.displayallbooks()

    elif choice==2:
        title = input("Enter name of the book you are looking for:")
        Lib.displaysearchedbook(title)

    elif choice==3:
        title = input("Enter name of the book you are looking for:")
        found=Lib.displaysearchedbook(title)
        if found:
            if len(user.borrowedbook) >= borrowlimit:
                print("borrow limit exceeds")
            else:
                user.borrowbook(title)
                print("Book borrowed sucessfully.")
    elif choice==4:
        title = input("Enter name of the book you are looking for:")
        found = Lib.displaysearchedbook(title)
        if found:
            user.returnbook(title)
        else:
            print("No book of the record found")
    elif choice ==5:
        user.vborrow()

    elif choice==6:
        exit()
    else:
        print("Invalid option. Please enter a valid option.")

