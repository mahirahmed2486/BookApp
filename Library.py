

import pickle
# This program will have some similar functionality to some of my productivity apps but will deal with storing notes
# and books the user reads. The user will have a library of books they can add to. And they can choose to make a note
# for a book that they are reading. This will save the player's data into their library which can be read
# in on the startup of this program.
# Want to think on a larger scale and see how we can have users add notes to a category of books ie) if a person was to
# read a self improvement book and make note of it all other users who also read self-improvement books would be able to
# see the posting if they so choose


class Book:
    def __init__(self, title):
        self.title = title
        self.notes = []
    def printTitle(self):

        print(self.title)
    def addaNote(self):
        note = input("Enter the note you would like to add for this book: ")
        self.notes.append(note)
        print("Added note...")

    def show_Notes(self):
        '''
        shows all the notes of a book starting from the very first note added
        :return: NONE
        '''
        index = 0
        for note in self.notes:
            print(index, ":", note)
            index += 1
class User:
    def __init__(self, name):
        self.name = name
        self.library = {}

    def addBook(self):
        title = input("Enter the title of the book you'd like to add to your library: ")
        # search list of books to make sure it's not already in there
        newBook = Book(title)
        self.library[title] = newBook

    def addNote(self):
        book = input("What is the title of the book you'd like to add a note to? ")
        # condition for if the book is not in the library
        # if book not in library : are you sure you entered correct/ do you want to add a book of this title
        self.library[book].addaNote()

    def printNotes(self):
        '''
        prints out all the notes for the requested book, checks to make sure the book is valid as well
        :return: None
        '''
        book = input("What is the name of the book you'd like to print notes from? ")
        self.library[book].show_Notes()

    def printLibrary(self):
        index = 0
        for books in self.library:
            print(index, ":", books.title())
            index += 1


try:
    file = open('save_data.txt', 'rb')
    Person = pickle.load(file)
    print("Welcome back, " + Person.name)
except EOFError:
    # first time running the program
    name = input("What is your name?")
    Person = User(name)
user_input = 0
while user_input != 4:
    print("[0] : Add a new Book...")
    print("[1] : Add a note to a Book...")
    print("[2] : Shows all notes of a Book...")
    print("[3] : Print a list of books in your Library...")
    print("[4] : Quit...")
    user_input = int(input("What would you like to do? "))
    if user_input == 0:
        Person.addBook()
    elif user_input == 1:
        Person.addNote()
    elif user_input == 2:
        Person.printNotes()
    elif user_input == 3:
        Person.printLibrary()
    elif user_input == 4:
        break
    else:
        print("Please enter the number of one of the following items below")

# save data
file = open('save_data.txt', 'wb')
pickle.dump(Person, file)
file.close()
