class Book:
    def __init__(self, title):
        self.title = title
        self.author = None

    def add_author(self, name):
        # add author property
        self.author = name

    def add_chapter(self, number, title):
        # add properties chapter_number and chapter_title
        self.chapter_number = number
        self.chapter_title = title


class BookInfo(Book):
    def __init__(self, title, price, info=False):
        Book.__init__(self, title)
        # add properties price and info
        self.price = price
        self.info = info
        self.stars = 0

    def rating(self, stars):
        try:
            # check if existing stars are less than new stars
            # and if new stars are greater than 4
            # adjust new price by a 20% increase
            if self.stars < stars:
                if self.stars > 4:
                    self.price += 0.2 * self.price

            # update the stars property
            self.stars = stars
        except Exception as e:
            print(e, "Please try again")


# Create a book object titled 'Two Scoops of Django'
obj_book = Book('Two Scoops of Django')

# Add the author 'Greenfeld'
obj_book.add_author('Greenfeld')

# Add a chapter 3, with title 'Async Views'
obj_book.add_chapter(3, 'Async Views')

# Create a book_info object titled 'Two Scoops of Django'
# with a price of 10, and info set to True
book_info = BookInfo('Two Scoops of Django', 10, True)

# Give the book_info a rating of 5 stars
book_info.rating(5)

print("Book info: ", end=" ")

# Print book_info's title, stars and price
print(
    book_info.title, str(book_info.stars) + " stars",
    book_info.price, sep=", "
)

# Print all properties of book and book_info objects
Book_Properties = {}
Book_Info_Properties = {}

Book_Properties['title'] = obj_book.title
Book_Properties['author'] = obj_book.author
Book_Properties['chapter_number'] = obj_book.chapter_number
Book_Properties['chapter_title'] = obj_book.chapter_title

print("Book properties: ", Book_Properties)
print("BookInfo properties: ", book_info.title, book_info.author,
      book_info.info, book_info.price, book_info.stars)
