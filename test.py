from operation import add_book, update_book, delete_book, add_member, delete_member, borrow_book, return_book
from mock_data import books, members, GENRES

# Reset mock data before tests
# Clear previous data
books.clear()
members.clear()

# Initialize mock data
books.update({
    "201": {"title": "The Code Within", "author": "Mason Reed", "genre": "Tech Thriller", "total_copies": 6},
    "202": {"title": "Whispers of Eternity", "author": "Elena Cross", "genre": "Fantasy", "total_copies": 4},
    "203": {"title": "The Forgotten City", "author": "Leo Grant", "genre": "Adventure", "total_copies": 3},
    "204": {"title": "Mind Over Matter", "author": "Sophia Lane", "genre": "Self-Help", "total_copies": 5},
    "205": {"title": "Echoes in the Dark", "author": "Dylan Frost", "genre": "Mystery", "total_copies": 2}
})

members.extend([
    {"member_id": "M101", "name": "Ethan Cole", "email": "ethan.cole@example.com", "borrowed_books": ["201"]},
    {"member_id": "M102", "name": "Nora Lewis", "email": "nora.lewis@example.com", "borrowed_books": ["203"]},
    {"member_id": "M103", "name": "Jacob Miller", "email": "jacob.miller@example.com", "borrowed_books": []}
])

# ---------- BOOK TESTS ----------
assert add_book("206", "Deep Code", "Ava Green", "Fiction", 4) == True, "Failed to add book"
assert add_book("201", "Duplicate ISBN Book", "Mason Reed", "Tech Thriller", 2) == False, "Duplicate ISBN allowed"
assert add_book("207", "Funny Book", "Author X", "Comedy", 2) == False, "Invalid genre allowed"

assert update_book("202", title="Whispers of Eternity - Revised") == True, "Failed to update book"
assert books["202"]["title"] == "Whispers of Eternity - Revised", "Title not updated"

assert delete_book("205") == True, "Failed to delete book"
assert "205" not in books, "Book not deleted"




# ---------- MEMBER TESTS ----------
assert add_member("M104", "David Lee", "david@example.com") == True, "Failed to add member"
assert add_member("M101", "Duplicate Ethan", "ethan2@example.com") == False, "Duplicate member ID allowed"
assert delete_member("M103") == True, "Failed to delete member"
assert all(m["member_id"] != "M103" for m in members), "Member not deleted"

# ---------- BORROW/RETURN TESTS ----------
assert borrow_book("M102", "202") == True, "Failed to borrow book"
assert borrow_book("M102", "202") == False, "Allowed borrowing same book twice"
assert return_book("M102", "202") == True, "Failed to return book"
assert return_book("M102", "202") == False, "Allowed returning a book not borrowed"



print("✅ All tests passed!")
