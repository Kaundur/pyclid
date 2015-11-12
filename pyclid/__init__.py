import math

# TODO - Should mag be a property of Vec2


class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        assert isinstance(other, (int, float, long)), 'Requires a int, float or long'
        self.x *= other
        self.y *= other
        return self

    def __div__(self, other):
        assert isinstance(other, (int, float, long)), 'Requires a int, float or long'
        self.x /= other
        self.y /= other
        return self

    def magnitude(self):
        return self.__abs__()

    def normalize(self):
        mag = self.magnitude()
        if mag:
            self.x /= mag
            self.y /= mag
        return self

    def cross(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return self.x*other.y - self.y*other.x

    def dot(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return self.x * other.x + self.y * other.y

    def angle(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return math.acos(self.dot(other)/(self.magnitude() * other.magnitude()))

    def mid_point(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return Vec2((self.x + other.x)/2.0, (self.y + other.y)/2.0)



# scalar triple product
# vector triple product a.(bXc)

# eq/ne
# reflect

# function to find intercept between two vectors

# Matrix algebra
# ident

# Quaternion
# raycast
# surface

# Make compatible with 2 and 3
# Import numpy if available


# To work with other types
# elif hasattr(other, '__len__') and len(other == 2):
