import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def test_add_and_remove_book(self):
        lib = Library()
        lib.add_book("1984", "George Orwell")
        lib.add_book("To Kill a Mockingbird", "Harper Lee")
        lib.remove_book("1984")

        has_book = False
        for book in lib.retrieve_books():
            if "To Kill a Mockingbird" in book:
                has_book = True
        self.assertTrue(has_book)

        has_book = False
        for book in lib.retrieve_books():
            if "1984" in book:
                has_book = True
        self.assertFalse(has_book)

    def test_retrieve_books(self):
        lib = Library()
        lib.add_book("The Great Gatsby", "F. Scott Fitzgerald")
        has_book = False
        for book in lib.retrieve_books():
            if "The Great Gatsby" in book:
                has_book = True
        self.assertTrue(has_book)

if __name__ == '__main__':
    unittest.main()
