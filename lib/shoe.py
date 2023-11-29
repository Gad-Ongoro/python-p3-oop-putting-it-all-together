#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size

    def brand_getter(self):
        return self._brand
    
    def brand_setter(self, new_brand):
        self._brand = new_brand

    def size_getter(self):
        return self._size

    def size_setter(self, new_size):
        if type(new_size) not in (int,):
            print("size must be an integer")
        self._size = new_size

    brand = property(brand_getter, brand_setter)
    size = property(size_getter, size_setter)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"