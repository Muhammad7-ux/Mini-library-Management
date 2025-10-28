"""
Library Management System - Core Operations
"""

# Valid genres tuple
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Biography", "Fantasy", "History")

# Books dictionary (ISBN -> book details)
books = {}

# Members list of dictionaries
members = []

def add_book(isbn, title, author, genre, total_copies):
    """
    Add a book if ISBN is unique and genre is valid
    """
    if isbn in books:
        return False, "Book with this ISBN already exists"
    
    if genre not in GENRES:
        return False, f"Invalid genre. Must be one of: {GENRES}"
    
    books[isbn] = {
        'title': title,
        'author': author,
        'genre': genre,
        'total_copies': total_copies,
        'available_copies': total_copies
    }
    return True, "Book added successfully"

def add_member(member_id, name, email):
    """
    Add a member if ID is unique
    """
    for member in members:
        if member['member_id'] == member_id:
            return False, "Member ID already exists"
    
    members.append({
        'member_id': member_id,
        'name': name,
        'email': email,
        'borrowed_books': []
    })
    return True, "Member added successfully"

def search_books(search_term):
    """
    Search books by title or author
    """
    results = []
    for isbn, book in books.items():
        if (search_term.lower() in book['title'].lower() or 
            search_term.lower() in book['author'].lower()):
            results.append({
                'isbn': isbn,
                **book
            })
    return results

def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    """
    Update book details
    """
    if isbn not in books:
        return False, "Book not found"
    
    if genre and genre not in GENRES:
        return False, f"Invalid genre. Must be one of: {GENRES}"
    
    book = books[isbn]
    if title:
        book['title'] = title
    if author:
        book['author'] = author
    if genre:
        book['genre'] = genre
    if total_copies is not None:
        # Adjust available copies accordingly
        old_total = book['total_copies']
        book['total_copies'] = total_copies
        book['available_copies'] = max(0, book['available_copies'] + (total_copies - old_total))
    
    return True, "Book updated successfully"

def update_member(member_id, name=None, email=None):
    """
    Update member details
    """
    for member in members:
        if member['member_id'] == member_id:
            if name:
                member['name'] = name
            if email:
                member['email'] = email
            return True, "Member updated successfully"
    
    return False, "Member not found"

def delete_book(isbn):
    """
    Delete book only if no borrowed copies
    """
    if isbn not in books:
        return False, "Book not found"
    
    book = books[isbn]
    if book['available_copies'] < book['total_copies']:
        return False, "Cannot delete book - copies are currently borrowed"
    
    del books[isbn]
    return True, "Book deleted successfully"

def delete_member(member_id):
    """
    Delete member only if no borrowed books
    """
    for i, member in enumerate(members):
        if member['member_id'] == member_id:
            if len(member['borrowed_books']) > 0:
                return False, "Cannot delete member - has borrowed books"
            
            members.pop(i)
            return True, "Member deleted successfully"
    
    return False, "Member not found"

def borrow_book(member_id, isbn):
    """
    Member can borrow up to 3 books if available
    """
    # Find member
    member = None
    for m in members:
        if m['member_id'] == member_id:
            member = m
            break
    
    if not member:
        return False, "Member not found"
    
    if isbn not in books:
        return False, "Book not found"
    
    book = books[isbn]
    
    # Check if member already has 3 books
    if len(member['borrowed_books']) >= 3:
        return False, "Member cannot borrow more than 3 books"
    
    # Check if book is available
    if book['available_copies'] <= 0:
        return False, "No copies available for borrowing"
    
    # Check if member already borrowed this book
    if isbn in member['borrowed_books']:
        return False, "Member already borrowed this book"
    
    # Borrow the book
    member['borrowed_books'].append(isbn)
    book['available_copies'] -= 1
    
    return True, "Book borrowed successfully"

def return_book(member_id, isbn):
    """
    Return borrowed book
    """
    # Find member
    member = None
    for m in members:
        if m['member_id'] == member_id:
            member = m
            break
    
    if not member:
        return False, "Member not found"
    
    if isbn not in books:
        return False, "Book not found"
    
    # Check if member has borrowed this book
    if isbn not in member['borrowed_books']:
        return False, "Member hasn't borrowed this book"
    
    # Return the book
    member['borrowed_books'].remove(isbn)
    books[isbn]['available_copies'] += 1
    
    return True, "Book returned successfully"

def get_all_books():
    """Get all books for display"""
    return books

def get_all_members():
    """Get all members for display"""
    return members