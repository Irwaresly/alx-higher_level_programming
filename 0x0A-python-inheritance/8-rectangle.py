#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Validate and set width and height using the integer_validator method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
         """"Set the private width and height attributes"""
        self.__width = width
        self.__height = height

