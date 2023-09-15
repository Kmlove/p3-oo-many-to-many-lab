class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"<Author: {self.name}>"
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalty):
        return Contract(self, book, date, royalty)
    
    def total_royalties(self):
       list_of_royalties = [contract.royalties for contract in self.contracts()]
       return sum(list_of_royalties)



class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)
    def __repr__(self):
        return f"<Book: {self.title}>"
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    def __repr__(self):
        return f'''
                <
                    Author: {self.author},
                    Book: {self.book},
                    Date: {self.date}
                >
            '''

    @classmethod
    def contracts_by_date(cls):
        def sort_func(e):
            return e.date
        cls.all.sort(key=sort_func)
        return cls.all

    def get_author(self):
        return self._author
    def set_author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Please use a valid Author")
    author = property(get_author, set_author)
    
    def get_book(self):
        return self._book
    def set_book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Please use a valid book")
    book = property(get_book, set_book)

    def get_date(self):
        return self._date
    def set_date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Please enter a valid date")
    date = property(get_date, set_date)

    def get_royalties(self):
        return self._royalties
    def set_royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("Please enter a valid royalty")
    royalties = property(get_royalties, set_royalties)

# Contract.all = []
# author = Author("Name")
# book1 = Book("Title 1")
# book2 = Book("Title 2")
# book3 = Book("Title 3")
# contract1 = Contract(author, book1, "02/01/2001", 10)
# contract2 = Contract(author, book2, "01/01/2001", 20)
# contract3 = Contract(author, book3, "03/01/2001", 30)

# import ipdb; ipdb.set_trace()