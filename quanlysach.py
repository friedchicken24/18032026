class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Sách: '{self.title}' - Tác giả: {self.author} - Năm xuất bản: {self.year}")

book1 = Book("Dế Mèn Phiêu Lưu Ký", "Tô Hoài", 1941)
book2 = Book("Harry Potter", "J.K Rowling", 1997)


print("Thông tin sách")
book1.display_info()
book2.display_info()