# A global library variable
library = []

# Function to ask a book from user and add it to library
def add_book():
    print("\nAdd a Book")
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    
    # Ensure year is an integer
    while True:
        try:
            year = int(input("Enter the publication year: "))
            break
        except ValueError:
            print("Please enter a valid year (e.g., 1999).")
    
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_input == 'yes' else False

    # Create the book dictionary
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    # Add it to the library
    library.append(book)
    print("Book added successfully!")


# Function to ask a book from user and remove it from the library
def remove_book():
    print("\nRemove a Book")
    title = input("Enter the title of the book to remove: ").strip().lower()
    found = False
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book removed successfully!")
            found = True
            break
    if not found:
        print("Book not found.")

# Function to Search a book
def search_book():
    print("\nSearch for a Book")
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")

    if choice == "1":
        keyword = input("Enter the title: ").strip().lower()
        results = [book for book in library if keyword in book["title"].lower()]
    elif choice == "2":
        keyword = input("Enter the author: ").strip().lower()
        results = [book for book in library if keyword in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if results:
        print("\nMatching Books:")
        for i, book in enumerate(results, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

# To display a book
def display_books():
    print("\nYour Library:")
    if not library:
        print("Your library is empty.")
    else:
        for i, book in enumerate(library, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# To show total number of the books and reading percentage
def display_stats():
    print("\nLibrary Statistics:")
    total = len(library)
    read_count = sum(1 for book in library if book["read"])
    percentage = (read_count / total * 100) if total > 0 else 0
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

# To save the library before exiting
def exit_program():
    print("\nGoodbye!")

## MENU ##
def menu():
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display the statistics")
        print("6. Exit the Library")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            display_stats()
        elif choice == '6':
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")

# Start Program 
if __name__ == "__main__":
    menu()