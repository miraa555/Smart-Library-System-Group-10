from operation import add_book, view_books, update_book, delete_book
from operation import add_member, view_members, delete_member
from operation import borrow_book, return_book
from mock_data import GENRES

def main_menu():
    """Text-based menu for interaction with the Mini Library System."""
    while True:
        print("""
======== Mira Mini Library System ========
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Add Member
6. View Members
7. Delete Member
8. Borrow Book
9. Return Book
0. Exit
=====================================
""")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            genre = input(f"Genre {GENRES}: ")
            total = input("Total Copies: ")
            try:
                total = int(total)
                add_book(isbn, title, author, genre, total)
            except ValueError:
                print(" Total copies must be a number.")
        elif choice == "2":
            view_books()
        elif choice == "3":
            isbn = input("ISBN to update: ")
            title = input("New Title (leave blank to skip): ") or None
            author = input("New Author (leave blank to skip): ") or None
            genre = input(f"New Genre {GENRES} (leave blank to skip): ") or None
            total = input("New Total Copies (leave blank to skip): ")
            total = int(total) if total else None
            update_book(isbn, title, author, genre, total)
        elif choice == "4":
            delete_book(input("ISBN to delete: "))
        elif choice == "5":
            add_member(input("Member ID: "), input("Name: "), input("Email: "))
        elif choice == "6":
            view_members()
        elif choice == "7":
            delete_member(input("Member ID to delete: "))
        elif choice == "8":
            borrow_book(input("Member ID: "), input("ISBN: "))
        elif choice == "9":
            return_book(input("Member ID: "), input("ISBN: "))
        elif choice == "0":
            print(" Exiting system. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

# Run menu only if executed directly
if __name__ == "__main__":
    main_menu()
