class Library :
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict ={}

    def displayBook(self):
        print(f"WE have following books in our library")
        for book in self.booklist:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book databasehas been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("book has been addedto the book list")
