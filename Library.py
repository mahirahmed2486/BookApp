#todo setup member varaibles and constructors

# todo setup methods for adding books, and then methods for adding and storing notes for those books

# This program will have some similar functionality to some of my productivity apps but will deal with storing notes
# and books the user reads. The user will have a library of books they can add to. And they can choose to make a note
# for a book that they are reading. This will save the player's data into their library which can be read in on the startup
# of this program.
# Want to think on a larger scale and see how we can have users add notes to a category of books ie) if a person was to
# read a self improvement book and make note of it all other users who also read self-improvement books would be able to
# see the posting if they so choose

class Book:
    def __init__(self, title):
        self.title = title
        self.notes = []
    def addNote(self):
        note = input("Enter the note you would like to add for ", self.title, ": ")
        self.notes.append(note)

class User:
    def __init__(self, name):
        self.name = name
        self.library = []
    def addBook(self):
        title = input("Enter the title of the book you'd like to add to your library: ")
        newBook = Book(title)
        self.library.append(newBook)
    def addNote(self):
        book = input("What is the name of the book you'd like to add a note to?")
        # condition for if the book is not in the library
        # if book not in library : are you sure you entered correct/ do you want to add a book of this title
        self.library[book].addNote
        