# Mini-library-Management
Mini Library Management System for Object Oriented assignment
A Python-based library management system implementing CRUD operations for books and members, plus borrowing/returning functionality.

Features
Add, search, update, and delete books

 Add, update, and delete members

 Borrow and return books with validation
 Genre validation using tuples

 ISBN-based book lookup using dictionaries

 Member management using lists

Project Structure
text
library-management/
├── operations.py    # Core functions
├── demo.py         # Quick demo script
├── tests.py        # Unit tests
├── DesignRationale.pdf
└── README.md
Quick Start
1. Run the Demo
bash
python demo.py
2. Run Tests
bash
python tests.py
3. Use in Your Code
python
import operations

# Add a book
operations.add_book("1234567890", "Python Guide", "Author Name", "Non-Fiction", 3)

# Add a member  
operations.add_member("MEM001", "John Doe", "john@email.com")

# Borrow a book
operations.borrow_book("MEM001", "1234567890")
Requirements
Python 3.6+

Data Structures
Books: Dictionary (ISBN → book details)

Members: List of dictionaries

Genres: Tuple of valid genres

Core Functions
add_book(isbn, title, author, genre, total_copies)

add_member(member_id, name, email)

search_books(search_term)

borrow_book(member_id, isbn)

return_book(member_id, isbn)

update_book(), update_member()

delete_book(), delete_member()
