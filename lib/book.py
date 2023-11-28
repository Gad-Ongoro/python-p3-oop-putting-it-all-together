#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count:int):
        self.title = title 
        self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def page_count_getter(self):
        return self._page_count

    def page_count_setter(self, page_count):
        if (type(page_count) in (int,)):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    page_count = property(page_count_getter, page_count_setter)

    pass

# mybk = Book("Gad", "22")
# mybk.turn_page()   
        