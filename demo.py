"""
Demo Script for Library Management System
"""
import operations

def demo():
    """Demonstrate the library management system"""
    print("🚀 LIBRARY MANAGEMENT SYSTEM DEMO")
    print("=" * 40)
    
    # Clear any existing data
    operations.books.clear()
    operations.members.clear()
    
    # 1. Add Books
    print("\n1. ADDING BOOKS")
    print("-" * 20)
    
    books_to_add = [
        ("9780134853457", "Clean Code", "Robert Martin", "Non-Fiction", 5),
        ("9780201633610", "Design Patterns", "Gang of Four", "Non-Fiction", 3),
        ("9780451524935", "1984", "George Orwell", "Fiction", 4),
        ("9780439708180", "Harry Potter", "J.K. Rowling", "Fantasy", 6),
        ("9780765326355", "The Way of Kings", "Brandon Sanderson", "Fantasy", 2)
    ]
    
    for book in books_to_add:
        success, message = operations.add_book(*book)
        print(f"Adding '{book[1]}': {message}")
    
    # 2. Add Members
    print("\n2. ADDING MEMBERS")
    print("-" * 20)
    
    members_to_add = [
        ("MEM001", "Alice Johnson", "alice@email.com"),
        ("MEM002", "Bob Smith", "bob@email.com"),
        ("MEM003", "Carol Davis", "carol@email.com")
    ]
    
    for member in members_to_add:
        success, message = operations.add_member(*member)
        print(f"Adding '{member[1]}': {message}")
    
    # 3. Display Current State
    print("\n3. CURRENT LIBRARY STATUS")
    print("-" * 20)
    print(f"Total Books: {len(operations.books)}")
    print(f"Total Members: {len(operations.members)}")
    
    # 4. Search Books
    print("\n4. SEARCHING BOOKS")
    print("-" * 20)
    
    search_terms = ["Clean", "Harry", "Sanderson"]
    for term in search_terms:
        results = operations.search_books(term)
        print(f"\nSearch for '{term}': Found {len(results)} books")
        for book in results:
            print(f"  - {book['title']} by {book['author']}")
    
    # 5. Borrow Books
    print("\n5. BORROWING BOOKS")
    print("-" * 20)
    
    borrow_actions = [
        ("MEM001", "9780134853457"),  # Alice borrows Clean Code
        ("MEM001", "9780439708180"),  # Alice borrows Harry Potter
        ("MEM002", "9780134853457"),  # Bob borrows Clean Code
        ("MEM001", "9780765326355"),  # Alice borrows The Way of Kings (3rd book)
    ]
    
    for member_id, isbn in borrow_actions:
        member_name = next(m['name'] for m in operations.members if m['member_id'] == member_id)
        book_title = operations.books[isbn]['title']
        success, message = operations.borrow_book(member_id, isbn)
        status = "✅" if success else "❌"
        print(f"{status} {member_name} borrowing '{book_title}': {message}")
    
    # 6. Try to borrow more than 3 books
    print("\n6. TESTING BORROW LIMIT")
    print("-" * 20)
    
    # Alice tries to borrow a 4th book
    success, message = operations.borrow_book("MEM001", "9780451524935")
    print(f"Alice trying to borrow 4th book: {message}")
    
    # 7. Return Books
    print("\n7. RETURNING BOOKS")
    print("-" * 20)
    
    return_actions = [
        ("MEM001", "9780134853457"),  # Alice returns Clean Code
    ]
    
    for member_id, isbn in return_actions:
        member_name = next(m['name'] for m in operations.members if m['member_id'] == member_id)
        book_title = operations.books[isbn]['title']
        success, message = operations.return_book(member_id, isbn)
        print(f"✅ {member_name} returning '{book_title}': {message}")
    
    # 8. Update Operations
    print("\n8. UPDATING RECORDS")
    print("-" * 20)
    
    # Update book
    success, message = operations.update_book("9780134853457", total_copies=6)
    print(f"Updating Clean Code copies: {message}")
    
    # Update member
    success, message = operations.update_member("MEM001", email="alice.johnson@newemail.com")
    print(f"Updating Alice's email: {message}")
    
    # 9. Delete Operations
    print("\n9. DELETION OPERATIONS")
    print("-" * 20)
    
    # Try to delete member with borrowed books (should fail)
    success, message = operations.delete_member("MEM001")
    print(f"Deleting Alice (has borrowed books): {message}")
    
    # Add and delete a member with no books
    operations.add_member("MEM004", "Temporary Member", "temp@email.com")
    success, message = operations.delete_member("MEM004")
    print(f"Deleting temporary member: {message}")
    
    # 10. Final Status
    print("\n10. FINAL LIBRARY STATUS")
    print("-" * 20)
    
    print("Books in library:")
    for isbn, book in operations.books.items():
        print(f"  - {book['title']}: {book['available_copies']}/{book['total_copies']} available")
    
    print("\nMembers and their borrowed books:")
    for member in operations.members:
        borrowed_count = len(member['borrowed_books'])
        print(f"  - {member['name']}: {borrowed_count} books borrowed")
    
    print("\n🎉 DEMO COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    demo()