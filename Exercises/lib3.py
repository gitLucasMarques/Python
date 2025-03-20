from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
from datetime import datetime, timedelta
import random

LOAN_PERIOD_DAYS = 14
COOLDOWN_DAYS = 7

class LibraryError(Exception):
    def __init__(self, message: str = "An error occurred in the library system"):
        super().__init__(message)

class NonMemberError(LibraryError):
    def __init__(self, member_name: str):
        message = f"{member_name} is not a registered member."
        super().__init__(message)

class BookNotAvailableError(LibraryError):
    def __init__(self, book_title: str):
        message = f"The book '{book_title}' is not available."
        super().__init__(message)

class CooldownPeriodError(LibraryError):
    def __init__(self, member_name: str, cooldown_end_date: datetime):
        message = f"{member_name} is in a cooldown period until {cooldown_end_date}."
        super().__init__(message)

class Status(Enum):
    AVAILABLE = 1
    LOANED = 2
    LOST = 3

@dataclass
class Book:
    title: str
    authors: List[str]
    edition: int

@dataclass
class BookItem:
    book: Book
    status: Status = Status.AVAILABLE

@dataclass
class Member:
    name: str
    member_id: int
    cooldown_end_date: Optional[datetime] = None
    current_loan: Optional[BookItem] = None

@dataclass
class Loan:
    book_item: BookItem
    member: Member
    date_borrowed: datetime = datetime.now()
    date_returned: Optional[datetime] = None
    due_date: datetime = None

@dataclass
class Library:
    items: List[BookItem] = field(default_factory=list)
    loan_history: List[Loan] = field(default_factory=list)
    members: List[Member] = field(default_factory=list)

    def add_book_item(self, book_item: BookItem):
        self.items.append(book_item)

    def add_member(self, member: Member):
        self.members.append(member)

    def checkout(self, member: Member, book_item: BookItem) -> None:
        if member not in self.members:
            raise NonMemberError(member.name)
        if book_item.status != Status.AVAILABLE:
            raise BookNotAvailableError(book_item.book.title)
        if member.cooldown_end_date and member.cooldown_end_date > datetime.now():
            raise CooldownPeriodError(member.name, member.cooldown_end_date)

        book_item.status = Status.LOANED
        date_borrowed = datetime.now()
        due_date = date_borrowed + timedelta(days=LOAN_PERIOD_DAYS)
        loan = Loan(book_item=book_item, member=member, date_borrowed=date_borrowed, due_date=due_date)
        member.current_loan = book_item
        self.loan_history.append(loan)

    def return_book(self, member: Member) -> None:
        if member not in self.members:
            raise NonMemberError(member.name)
        
        for loan in self.loan_history:
            if loan.member == member and loan.book_item.status == Status.LOANED:

                if loan.due_date < datetime.now():
                    member.cooldown_end_date = datetime.now() + timedelta(days=COOLDOWN_DAYS)
                
                loan.book_item.status = Status.AVAILABLE
                member.current_loan = None
                self.loan_history.remove(loan)
                return
        
        raise LibraryError(f"No active loans found for {member.name}.")

def main():
    books = [
        Book(title='The Great Gatsby', authors=['F. Scott Fitzgerald'], edition=1),
        Book(title='1984', authors=['George Orwell'], edition=1),
        Book(title='O Código Da Vinci', authors=['Dan Brown'], edition=1),
    ]
    
    library = Library()
    
    for book in books:
        library.add_book_item(BookItem(book=book))
        
    library.add_member(Member(name='John Doe', member_id=1))
    library.add_member(Member(name='Paulo', member_id=2))
    library.add_member(Member(name='José', member_id=3))
    
    print('\nINITIAL LIBRARY: ', library) 
    
    for _ in range(10):
        flag = random.randint(1, 2)
        flag_book = random.randint(0, len(library.items) - 1)
        flag_member = random.randint(0, len(library.members) - 1)
        
        member = library.members[flag_member]
        book_item = library.items[flag_book]
        
        if flag == 1:  # Checkout
            try:
                library.checkout(member, book_item)
                print(f'\nStatus de Empréstimo: {member.name} has borrowed {book_item.book.title}.')
            except LibraryError as e:
                print('\n', e)

        else:  # Return
            try:
                library.return_book(member)
                print(f'\nStatus de Devolução: {member.name} has returned {book_item.book.title}.')
            except LibraryError as e:
                print('\n', e)
      
        print('\nLIBRARY: ')
        for item in library.items:
            print(f'{item.book.title} - Status: {item.status.name}')

main()
