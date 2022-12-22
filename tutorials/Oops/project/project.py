# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

#libarary Names:
Oxford_Library_books = ["In Search of Lost Time by Marcel Proust", "Ulysses by James Joyce", "Don Quixote by Miguel de Cervantes", "One Hundred Years of Solitude by Gabriel Garcia Marquez", "The Great Gatsby by F", "Moby Dick by Herman Melville", "War and Peace by Leo Tolstoy"]

Library_no_2 = ["A Monster Calls by Patrick Ness","Skulduggery Pleasant by Derek Landy", "Refugee Boy by Benjamin Zephaniah","How I Live Now by Meg Rosoff", "The Handmaid's Tale by Margaret Atwood", "New Town Soul by Dermot Bolger", "The One and Only Ivan by Katherine Applegate", "The Walking Dead by Robert Kirkman"]


dict_for_book_user = { "Fuck u": "ErMapsh"}
class Library:
    def __init__(self, listofbooks, library_name, Name_of_user):
        self.listofbooks = listofbooks
        self.library_name = library_name
        self.Name_of_user = Name_of_user
 
    @property
    def display_book(self):
        print("Books in Librabry:")
        index = 1
        for index, item in enumerate(self.listofbooks):
             print(f"{index}.{item}")

    @property
    def lend_book(self):
        book_ans = input("Enter the book Name:")
        if book_ans in Oxford_Library_books:
            Oxford_Library_books.remove(book_ans.strip())#remove book form list
            dict_for_book_user.update({book_ans : self.Name_of_user})#add to dictionary 
            # print(dict_for_book_user)
            print("u own book successfully")
        else:
            print("may be book not available")


    def return_book(self, return_book_nm):
        if return_book_nm in dict_for_book_user:
            dict_for_book_user.pop(return_book_nm)
            Oxford_Library_books.append(return_book_nm)
            print(f"Book return successfully by {self.Name_of_user}...")
        else:
            print("may be wrong inforamtion of book has given..")

    def WhoOwnBooks(self):
        for keys, values in dict_for_book_user.items():
            print(f"The owner of '{keys}' is {values} ")


    def add_book_by_someone_in_library(self, new_book_name):
        Oxford_Library_books.append(new_book_name)
        self.display_book
        print("new book add successfully........")



class User(Library):
    def __init__(self, listofbooks, library_name, Name_of_user):
        self.listofbooks = listofbooks
        self.library_name = library_name
        self.Name_of_user = Name_of_user
        # super().__init__(Oxford_Library_books , "Oxford", "ErMapsh")

    @property   
    def info(self):
        return f"Name of user is {self.Name_of_user}"



if __name__ == "__main__":
    while 1:
        ErMapsh = User(Oxford_Library_books , "Oxford", "ErMapsh")
        print("What u want?\n1.Display books\n2.Lend Book\n3.Return Book\n4.Add New Book\n5.Owner Of books\n6.Exit")
        ans = int(input("Enter your choice:"))
        print()
        if ans == 1:
            ErMapsh.display_book
            print()

        elif ans == 2:
            ErMapsh.lend_book
            print()

        elif ans == 3:
            return_book_name = input("Enter the name of book that u wana returned:")
            ErMapsh.return_book(return_book_name)
            print()

        elif ans == 4:
            new_book = input("Enter book name:")
            ErMapsh.add_book_by_someone_in_library(new_book)
            print()

        elif ans == 5: 
            ErMapsh.WhoOwnBooks()

        elif ans == 6:
            exit()

