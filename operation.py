# Import mock data
from mock_data import books, members, GENRES


"""
Mira Mini Library Management System

"""



# CRUD OPERATIONS FOR BOOKS 

def add_book(isbn, title, author, genre, total_copies):
    """ New book if ISBN is unique and genre is valid."""
    if isbn in books:
        print(" ISBN already exists. Book not added.")
        return False
    if genre not in GENRES:
        print(" Invalid genre. Choose from:", GENRES)
        return False
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies
    }
    print(f" Book '{title}' added successfully.")
    return True



def view_books():
    """Display all books in the library."""
    if not books:
        print(" No books available.")
        return
    print("\n--- Library Books ---")
    for isbn, info in books.items():
        print(f"ISBN: {isbn} | {info['title']} by {info['author']} | Genre: {info['genre']} | Copies: {info['total_copies']}")


def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    """Update details of an existing book."""
    if isbn not in books:
        print(" Book not found.")
        return False
    if genre and genre not in GENRES:
        print(" Invalid genre.")
        return False

    # Update only provided fields
    if title: books[isbn]["title"] = title
    if author: books[isbn]["author"] = author
    if genre: books[isbn]["genre"] = genre
    if total_copies is not None: books[isbn]["total_copies"] = total_copies

    print(f" Book '{isbn}' updated successfully.")
    return True


def delete_book(isbn):
    """Delete a book by ISBN."""
    if isbn in books:
        del books[isbn]
        print(" Book deleted successfully.")
        return True
    print(" Book not found.")
    return False


# CRUD OPERATIONS FOR MEMBERS 

def add_member(member_id, name, email):
    """Add a new member if member_id is unique."""
    for m in members:
        if m["member_id"] == member_id:
            print(" Member ID already exists.")
            return False
    member = {"member_id": member_id, "name": name, "email": email, "borrowed_books": []}
    members.append(member)
    print(f" Member '{name}' added successfully.")
    return True


def view_members():
    """Display library members."""
    if not members:
        print(" No members found.")
        return
    print("\n--- Library Members ---")
    for m in members:
        print(f"ID: {m['member_id']} | Name: {m['name']} | Email: {m['email']} | Borrowed: {m['borrowed_books']}")


def delete_member(member_id):
    """Remove a member by ID."""
    for m in members:
        if m["member_id"] == member_id:
            members.remove(m)
            print(" Member removed successfully.")
            return True
    print(" Member not found.")
    return False


# BORROW / RETURN OPERATIONS 

def borrow_book(member_id, isbn):
    """Allow a member to borrow a book if available."""
    if isbn not in books:
        print(" Invalid ISBN.")
        return False
    for m in members:
        if m["member_id"] == member_id:
            if books[isbn]["total_copies"] <= 0:
                print(" No copies available.")
                return False
            if isbn in m["borrowed_books"]:
                print(" Book already borrowed by this member.")
                return False
            m["borrowed_books"].append(isbn)
            books[isbn]["total_copies"] -= 1
            print(f" '{books[isbn]['title']}' borrowed successfully by {m['name']}.")
            return True
    print(" Member not found.")
    return False


def return_book(member_id, isbn):
    """Return borrowed book."""
    for m in members:
        if m["member_id"] == member_id:
            if isbn not in m["borrowed_books"]:
                print(" This book wasn't borrowed by the member.")
                return False
            m["borrowed_books"].remove(isbn)
            books[isbn]["total_copies"] += 1
            print(f" '{books[isbn]['title']}' returned successfully.")
            return True
    print(" Member not found.")
    return False



