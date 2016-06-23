import math

#import pyclid.matrix as matrix
import pyclid.matrix


class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __len__(self):
        return 2

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        assert isinstance(other, (int, float)), 'Requires a int, float'
        self.x *= other
        self.y *= other
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        assert isinstance(other, (int, float)), 'Requires a int, float'
        self.x /= other
        self.y /= other
        return self

    def __eq__(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return not self.__eq__(other)

    def distance_between(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

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
        return self.x*other.x + self.y*other.y

    def angle(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return math.acos(self.dot(other)/(self.magnitude() * other.magnitude()))

    def mid_point(self, other):
        assert isinstance(other, Vec2), 'Requires a Vec2'
        return Vec2((self.x + other.x)/2.0, (self.y + other.y)/2.0)

    def rotate(self, other):
        assert isinstance(other, (int, float, pyclid.matrix.Mat2)), 'Requires a rotation matrix or an angle'

        if isinstance(other, pyclid.matrix.Mat2):
            om = other.matrix
            vec_x = om[0]*self.x + om[1]*self.y
            vec_y = om[2]*self.x + om[3]*self.y
        else:
            vec_x = math.cos(other)*self.x - math.sin(other)*self.y
            vec_y = math.sin(other)*self.x + math.cos(other)*self.y

        self.x = vec_x
        self.y = vec_y
        return self

    def set_rotation(self, other):
        assert isinstance(other, (int, float)), 'Requires an int float'
        vec_x = math.cos(other)*self.x - math.sin(other)*self.y
        vec_y = math.sin(other)*self.x + math.cos(other)*self.y


        vec_x = math.cos(other)
        vec_y = math.sin(other)

        self.x = vec_x
        self.y = vec_y


    def zero(self):
        self.x = 0
        self.y = 0
        return self


class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return 3

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '>'

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        assert isinstance(other, (int, float)), 'Requires a int, float'
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __rmul__(self, other):
        return self.__rmul__(other)

    def __div__(self, other):
        assert isinstance(other, (int, float)), 'Requires a int, float'
        self.x /= other
        self.y /= other
        self.z /= other
        return self

    def __eq__(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return not self.__eq__(other)

    def distance_between(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)

    def magnitude(self):
        return self.__abs__()

    def normalize(self):
        mag = self.magnitude()
        if mag:
            self.x /= mag
            self.y /= mag
            self.z /= mag
        return self

    def cross(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return Vec3((self.y*other.z - other.y*self.z),
                    -(self.x*other.z - other.x*self.z),
                    (self.x*other.y - other.x*self.y))

    def dot(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return self.x*other.x + self.y*other.y + self.z*other.z

    def angle(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return math.acos(self.dot(other)/(self.magnitude()*other.magnitude()))

    def mid_point(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return Vec3((self.x + other.x)/2.0, (self.y + other.y)/2.0, (self.z + other.z)/2.0)

    def triple_s(self, other, other2):
        assert isinstance(other, Vec3), 'Requires all inputs to be Vec3'
        assert isinstance(other2, Vec3), 'Requires all inputs to be Vec3'
        return self.dot(other.cross(other2))

    def triple_v(self, other, other2):
        assert isinstance(other, Vec3), 'Requires all inputs to be Vec3'
        assert isinstance(other2, Vec3), 'Requires all inputs to be Vec3'
        return self.cross(other.cross(other2))

    def zero(self):
        self.x = 0
        self.y = 0
        self.z = 0
        return self


class Vec4:
    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __len__(self):
        return 4

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + '>'

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

    def __add__(self, other):
        assert isinstance(other, Vec4), 'Requires a Vec4'
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        assert isinstance(other, Vec4), 'Requires a Vec4'
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.z)

    def __mul__(self, other):
        assert isinstance(other, (int, float)), 'Requires a int, float'
        self.x *= other
        self.y *= other
        self.z *= other
        self.w *= other
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        assert isinstance(other, (int, float)), 'Requires a int, float'
        self.x /= other
        self.y /= other
        self.z /= other
        self.w /= other
        return self

    def __eq__(self, other):
        assert isinstance(other, Vec4), 'Requires a Vec4'
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

    def __ne__(self, other):
        assert isinstance(other, Vec4), 'Requires a Vec4'
        return not self.__eq__(other)

    def distance_between(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2 + (self.w-other.w)**2)

    def magnitude(self):
        return self.__abs__()

    def normalize(self):
        mag = self.magnitude()
        if mag:
            self.x /= mag
            self.y /= mag
            self.z /= mag
            self.w /= mag
        return self


    # def angle(self, other):
    #     assert isinstance(other, Vec2), 'Requires a Vec2'
    #     return math.acos(self.dot(other)/(self.magnitude() * other.magnitude()))

    # def mid_point(self, other):
    #     assert isinstance(other, Vec2), 'Requires a Vec2'
    #     return Vec2((self.x + other.x)/2.0, (self.y + other.y)/2.0)


    # def rotate(self, other):
    #     assert isinstance(other, (int, float, long, matrix.Mat2)), 'Requires a rotation matrix or an angle'
    #
    #     if isinstance(other, matrix.Mat2):
    #         om = other.matrix
    #         vec_x = om[0]*self.x + om[1]*self.y
    #         vec_y = om[2]*self.x + om[3]*self.y
    #     else:
    #         vec_x = math.cos(other)*self.x - math.sin(other)*self.y
    #         vec_y = math.sin(other)*self.x + math.cos(other)*self.y
    #
    #     self.x = vec_x
    #     self.y = vec_y
    #     return self
    #
    # def set_rotation(self, other):
    #     assert isinstance(other, (int, float, long)), 'Requires an int float or long'
    #     vec_x = math.cos(other)*self.x - math.sin(other)*self.y
    #     vec_y = math.sin(other)*self.x + math.cos(other)*self.y
    #
    #
    #     vec_x = math.cos(other)
    #     vec_y = math.sin(other)
    #
    #     self.x = vec_x
    #     self.y = vec_y

    def zero(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0
        return self

