"""
Mock data for Mini Library Management System.

"""

#   Genres
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Romance", "Fantasy", "Mystery")

#  Books
books = {
    "201": {"title": "The Code Within", "author": "Mason Reed", "genre": "Tech Thriller", "total_copies": 6},
    "202": {"title": "Whispers of Eternity", "author": "Elena Cross", "genre": "Fantasy", "total_copies": 4},
    "203": {"title": "The Forgotten City", "author": "Leo Grant", "genre": "Adventure", "total_copies": 3},
    "204": {"title": "Mind Over Matter", "author": "Sophia Lane", "genre": "Self-Help", "total_copies": 5},
    "205": {"title": "Echoes in the Dark", "author": "Dylan Frost", "genre": "Mystery", "total_copies": 2}
}

members = [
    {"member_id": "M101", "name": "Ethan Cole", "email": "ethan.cole@example.com", "borrowed_books": ["201"]},
    {"member_id": "M102", "name": "Nora Lewis", "email": "nora.lewis@example.com", "borrowed_books": ["203"]},
    {"member_id": "M103", "name": "Jacob Miller", "email": "jacob.miller@example.com", "borrowed_books": []}
]

