from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    items = relationship("BookItem", back_populates="book")
    UniqueConstraint('title', 'author', name='uix_1')

class BookItem(Base):
    __tablename__ = "book_items"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    is_available = Column(Boolean, default=True)
    book = relationship("Book", back_populates="items")

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        return False

engine = create_engine('mysql+mysqlconnector://sql10748734:FCsdTT6skA@sql5.freemysqlhosting.net/sql10748734')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_book_to_library(session, title, author):
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    return book

def add_book_item_to_library(session, book_id):
    book = session.query(Book).get(book_id)
    if not book:
        return None
    item = BookItem(book=book)
    session.add(item)
    session.commit()
    return item

def list_all_books(session):
    return session.query(Book).all()

def borrow_book_by_id(session, item_id):
    item = session.query(BookItem).get(item_id)
    if item and item.borrow():
        session.commit()
        return item
    return None

def return_book_by_id(session, item_id):
    item = session.query(BookItem).get(item_id)
    if item and item.return_book():
        session.commit()
        return item
    return None

def add_book_ui(session):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    book = add_book_to_library(session, title, author)
    print(f"Book '{book.title}' by {book.author} added to the library.")

def add_book_item_ui(session):
    book_id = int(input("Enter the ID of the book to add a copy for: "))
    item = add_book_item_to_library(session, book_id)
    if item:
        print(f"Book item with ID {item.id} added for '{item.book.title}'.")
    else:
        print("Book not found.")

def list_books_ui(session):
    books = list_all_books(session)
    if not books:
        print("No books in the library.")
    else:
        for book in books:
            print(f"{book.id}: {book.title} by {book.author}")
            for item in book.items:
                status = "Available" if item.is_available else "Borrowed"
                print(f"    Item {item.id}: {status}")

def borrow_book_ui(session):
    item_id = int(input("Enter the ID of the book item to borrow: "))
    item = borrow_book_by_id(session, item_id)
    if item:
        print(f"You have borrowed item {item.id} of '{item.book.title}'.")
    else:
        print("Book item not found or already borrowed.")

def return_book_ui(session):
    item_id = int(input("Enter the ID of the book item to return: "))
    item = return_book_by_id(session, item_id)
    if item:
        print(f"You have returned item {item.id} of '{item.book.title}'.")
    else:
        print("Book item not found or was not borrowed.")

def main():
    session = Session()
    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Add Book Item (Copy)")
        print("3. List Books")
        print("4. Borrow Book Item")
        print("5. Return Book Item")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book_ui(session)
        elif choice == 2:
            add_book_item_ui(session)
        elif choice == 3:
            list_books_ui(session)
        elif choice == 4:
            borrow_book_ui(session)
        elif choice == 5:
            return_book_ui(session)
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
