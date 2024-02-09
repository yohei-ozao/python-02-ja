# Challenge 1
Create a Python class `Library` to manage a personal book collection.

This class should allow adding books, removing books, and retrieving the current book collection.

- Implement a Library class with methods to add books, remove books, and display books.
- Use private attributes to store book information.
- Ensure that removed books are handled gracefully.

## Requirements
- **Class Name**: `Library`
- **Interface**:
    - `add_book(title, author)`: Adds a new book.
    - `remove_book(title)`: Removes a book by title.
    - `retrieve_books()`: Returns a list of all books in the library.

## Example Usage

```python
my_library = Library()
my_library.add_book("1984", "George Orwell")
my_library.add_book("To Kill a Mockingbird", "Harper Lee")
for book in my_library.retrieve_books():
    print(book)
my_library.remove_book("1984")
for book in my_library.retrieve_books():
    print(book)
```
