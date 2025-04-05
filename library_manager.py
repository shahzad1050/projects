import json
import os

data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
          return json.load(file)
    return []


def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter the  title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input(" Enter the genre of the book: ")
    read = input("have you read thre book? (yes/no):").lower()== "yes"

    new_book = {
        "title": title,
        "author": author,
        "year" : year,
        "genre": genre,
        "read": read
        
      }

    library.append(new_book)
    save_library(library)
    print(f"book {title} added succesfully")


def remove_book(library):
    title = input("Enter the title book to remove from the library")
    initial_length = len(library)
    library = [book for book in library if book ["title"].lower() != title]

    if len(library) < initial_length:
        save_library(library)
        print(f"book {title} removed succesfullly ")
    else:
        print(f"book {title} not found in library")

def search_library(library):
   search_by = input("search by title of author").lower()
   search_term = input(f"Enter the {search_by}").lower()

   result = [book for book in library if search_term in book [search_by].lower()]

   if result:
        for book in result:
           status = "read" if book ["read"] else "unread"
           print(f"{book["title"]} by {book["author"]} - {book["year"]} - {book["genre"]} - {status}")
   else:
           print(f"no books found matching {search_term} in the {search_by} field ")

def display_all_books(library):
    if library:
        for book in library:
            status = "read" if book ["read"] else "unread"
            print(f"{book["title"]} by {book ["author"]} - {book["year"]} - {book["genre"]} - {status}")
    else:
        print("The library is empty.")

def display_statistics(library):
        total_books = len(library)
        read_books = len([book for book in library if book ["read"]])
        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

        print(f"total_books:{total_books}")
        print(f"percentage_read : {percentage_read:.2f}%")

def main():
        library = load_library()
        while True:
          print("Menu")
          print("1. Add a book")
          print("2. remove a book")
          print("3. search the library")
          print("4. display all books")
          print("5. display statistics")
          print("6. Exits")

          choice  = input("Enter th choice")
          if choice == "1":
               add_book(library)
          elif choice == "2":
               remove_book(library)
          elif choice == "3":
               search_library(library)
          elif choice == "4":
               display_all_books(library)
          elif choice == "5":
               display_statistics(library)
          elif choice == "6":
               print("good bye")
               break
          else: 
              print("invalid choice . please try again")


if __name__ == "__main__":

  main()