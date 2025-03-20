from dataclasses import dataclass, field
from typing import List
from enum import Enum
from datetime import datetime
import random

class Status(Enum):
    Available = 1
    Loaned = 2
    Lost = 3

@dataclass
class Book:
    title: str
    authors: List[str]
    edition: int

@dataclass
class BookItem:
    book: Book
    status: Status = Status.Available
    date_borrowed: datetime = None

    def checkout(self) -> bool:
        if self.status == Status.Available:
            self.status = Status.Loaned
            self.date_borrowed = datetime.now()
            return True
        return False
    
    def return_book(self) -> bool:
        if self.status == Status.Loaned:
            self.status = Status.Available
            self.date_borrowed = None
            return True
        return False

@dataclass
class Member:
    name: str
    member_id: int
    borrowed_books: List[BookItem] = field(default_factory=list)

    def borrow_book(self, book_item: BookItem):
        if book_item.status == Status.Available and book_item.checkout():
            self.borrowed_books.append(book_item)
            return True
        return False

    def return_book(self, book_item: BookItem):
        if book_item.status == Status.Loaned and book_item.return_book():
            self.borrowed_books.remove(book_item)
            return True
        return False
    
@dataclass
class Library:
    items: List[BookItem] = field(default_factory=list)
    members: List[Member] = field(default_factory=list)

    def add_book_item(self, book_item: BookItem):
        self.items.append(book_item)

    def add_member(self, member: Member):
        self.members.append(member)

def main():
    
    book = []
    
    book.append(Book(title='The Great Gatsby', authors=['F. Scott Fitzgerald'], edition=1))
    book.append(Book(title='1984', authors=['George Orwell'], edition=1))
    book.append(Book(title='O Código Da Vinci',  authors=['Dan Brown'], edition=1))
    
    library = Library()
    
    while len(book) != 0:
        books = BookItem(book.pop())
        library.items.append(books)
        
    library.members.append(Member(name='John Doe', member_id=1))
    library.members.append(Member(name='Paulo', member_id=2))
    library.members.append(Member(name='José', member_id=3))
    
    print('\nBiblioteca inicial: ', library) 
    
    nMember = 2
    nBooks = 2
    
    for i in range(1,11):
        flag = random.randint(1,2)
        flag_book = random.randint(-1,nBooks)
        flag_member = random.randint(-1,nMember)
        
        if flag == 1:
            success = library.members[flag_member].borrow_book(library.items[flag_book])
            if success == True:
                print('\nStatus do empréstimo de ', library.members[flag_member].name, ': ',
                       success, library.members[flag_member].borrowed_books)
                nBooks = nBooks - 1
            else:
                print('\nNão foi possível emprestar este livro!', library.items[flag_book])
        
        else:
            if library.members[flag_member].borrowed_books.count(library.items[flag_book]) != 0:
                success = library.members[flag_member].return_book(library.items[flag_book])
                if  success == True:
                    print('\nStatus da devolução de ', library.members[flag_member].name, ': ',
                           success, library.members[flag_member].borrowed_books)
                    nBooks = nBooks + 1
            else:
                print('\nEste livro não está com este usuário!', library.members[flag_member].name,library.items[flag_book])
        
        
        print('\nBIBLIOTECA: ')
        for i in library.items:
            if i.status == Status.Available:
                print(i)

 
resultado = main()    
