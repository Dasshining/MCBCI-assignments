class Gallery:
    def __init__(self, direction, name, city, length, width, paintings_in_gall=None) -> None:
        self._direction = direction
        self._name = name
        self._city = city
        self._length = length
        self._width = width
        self._dim = length * width
        self._paintings_in_gall = paintings_in_gall

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def dim(self):
        return self._dim

    @dim.setter
    def dim(self, dim):
        self._dim = dim

    @property
    def paintings_in_gall(self):
        return self._paintings_in_gall

    @paintings_in_gall.setter
    def paintings_in_gall(self, paintings_in_gall):
        self._paintings_in_gall = paintings_in_gall

    def __str__(self):
        return f"Name: {self.name}, Direction: {self.direction}, City: {self.city}, Length: {self.length}, " \
               f"Width: {self.width}, Dim: {self.dim} m2, Paintings in gallery: {self.paintings_in_gall}"
