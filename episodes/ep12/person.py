class Person:
    
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._street = None
        self._city = None
        self._state = None
        self._zipcode = None
        self._phone = None
        
    def __str__(self):
        return f"{self._last_name}, {self._first_name}"
