"""
Unit Tests for Library Management System
"""
import operations

def test_add_book():
    """Test adding books"""
    # Test valid book addition
    result, message = operations.add_book("1234567890", "Test Book", "Test Author", "Fiction", 5)
    assert result == True
    assert message == "Book added successfully"
    assert "1234567890" in operations.books
    
    # Test duplicate ISBN
    result, message = operations.add_book("1234567890", "Another Book", "Another Author", "Sci-Fi", 3)
    assert result == False
    assert "already exists" in message
    
    # Test invalid genre
    result, message = operations.add_book("0987654321", "Invalid Book", "Some Author", "Invalid Genre", 2)
    assert result == False
    assert "Invalid genre" in message

def test_add_member():
    """Test adding members"""
    # Test valid member addition
    result, message = operations.add_member("M001", "John Doe", "john@email.com")
    assert result == True
    assert message == "Member added successfully"
    assert len(operations.members) == 1
    
    # Test duplicate member ID
    result, message = operations.add_member("M001", "Jane Doe", "jane@email.com")
    assert result == False
    assert "already exists" in message

def test_borrow_and_return():
    """Test borrowing and returning books"""
    # Setup
    operations.add_book("1111111111", "Borrow Book", "Borrow Author", "Fiction", 2)
    operations.add_member("M002", "Borrower", "borrower@email.com")
    
    # Test successful borrow
    result, message = operations.borrow_book("M002", "1111111111")
    assert result == True
    assert "borrowed successfully" in message
    
    # Test borrowing same book again
    result, message = operations.borrow_book("M002", "1111111111")
    assert result == False
    assert "already borrowed" in message
    
    # Test borrowing more than 3 books
    operations.add_book("2222222222", "Book 2", "Author 2", "Fiction", 1)
    operations.add_book("3333333333", "Book 3", "Author 3", "Fiction", 1)
    operations.add_book("4444444444", "Book 4", "Author 4", "Fiction", 1)
    
    operations.borrow_book("M002", "2222222222")
    operations.borrow_book("M002", "3333333333")
    
    result, message = operations.borrow_book("M002", "4444444444")
    assert result == False
    assert "cannot borrow more than 3" in message
    
    # Test successful return
    result, message = operations.return_book("M002", "1111111111")
    assert result == True
    assert "returned successfully" in message

def test_search_books():
    """Test book search functionality"""
    operations.add_book("5555555555", "Python Programming", "Python Expert", "Non-Fiction", 3)
    
    results = operations.search_books("Python")
    assert len(results) == 1
    assert results[0]['title'] == "Python Programming"
    
    results = operations.search_books("Expert")
    assert len(results) == 1
    assert results[0]['author'] == "Python Expert"

def test_delete_operations():
    """Test deletion operations"""
    # Test deleting book with borrowed copies
    operations.add_book("6666666666", "Popular Book", "Popular Author", "Fiction", 1)
    operations.add_member("M003", "Reader", "reader@email.com")
    
    operations.borrow_book("M003", "6666666666")
    
    result, message = operations.delete_book("6666666666")
    assert result == False
    assert "copies are currently borrowed" in message
    
    # Test deleting member with borrowed books
    result, message = operations.delete_member("M003")
    assert result == False
    assert "has borrowed books" in message

def run_all_tests():
    """Run all tests"""
    # Clear data before tests
    operations.books.clear()
    operations.members.clear()
    
    test_add_book()
    print("✓ test_add_book passed")
    
    test_add_member()
    print("✓ test_add_member passed")
    
    test_borrow_and_return()
    print("✓ test_borrow_and_return passed")
    
    test_search_books()
    print("✓ test_search_books passed")
    
    test_delete_operations()
    print("✓ test_delete_operations passed")
    
    print("\n🎉 All tests passed!")

if __name__ == "__main__":
    run_all_tests()