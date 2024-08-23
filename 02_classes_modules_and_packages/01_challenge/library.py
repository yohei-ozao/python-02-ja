class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        """新しい本を追加します。"""
        self._books.append({"title": title, "author": author})

    def remove_book(self, title):
        """タイトルで指定した本を削除します。"""
        for book in self._books:
            if book["title"] == title:
                self._books.remove(book)
                return f'Book titled "{title}" has been removed.'
        return f'Book titled "{title}" not found in the library.'

    def retrieve_books(self):
        """ライブラリ内の本を表す辞書のリストを返します。"""
        return self._books