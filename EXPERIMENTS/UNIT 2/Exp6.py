class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display(self):
        return f'Title:{self.title}, Author:{self.author}'
    

class Ebook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        base_info =super().display()
        return f'{base_info}, File Size:{self.file_size} MB'


ebook = Ebook("Theory of Evolution","Charles Darwin",25)
printed_book = Book("Mockingbird","Harper Lee")

print(ebook.display())
print(printed_book.display())