import math


class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '[' + str(self.x) + ', ' + str(self.y) + ']'

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
        assert isinstance(other, (int, float, long, Mat2)), 'Requires a rotation matrix or an angle'

        if isinstance(other, Mat2):
            om = other.matrix
            vec_x = om[0]*self.x + om[1]*self.y
            vec_y = om[2]*self.x + om[3]*self.y
        else:
            vec_x = math.cos(other)*self.x - math.sin(other)*self.y
            vec_y = math.sin(other)*self.x + math.cos(other)*self.y

        self.x = vec_x
        self.y = vec_y
        return self

    def zero(self):
        self.x = 0
        self.y = 0
        return self


class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '[' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ']'

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        assert isinstance(other, Vec3), 'Requires a Vec3'
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        assert isinstance(other, (int, float, long)), 'Requires a int, float or long'
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __div__(self, other):
        assert isinstance(other, (int, float, long)), 'Requires a int, float or long'
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

    def __str__(self):
        return '[' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + ']'


#  inverse, det, reflect
class Mat2:
    """ Creates a 2x2 matrix

        |0, 1|
        |2, 3|

    """
    def __init__(self, mat):
        assert isinstance(mat, list) and len(mat) <= 4, 'Requires input to be a list and len <= 4'
        self.__matrix = []
        self.x_size = 2
        self.y_size = 2
        self.size = 9

        # Initialise the matrix to zero
        for i in xrange(self.size):
            self.__matrix.append(0)
        self.__input_matrix_values(mat)

    def __str__(self):
        max_size = 0
        for i in self.__matrix:
            if len(str(i)) > max_size:
                max_size = len(str(i))

        str_out = ''
        for j in range(self.y_size):
            str_out += '| '
            for i in range(self.x_size):
                str_out += str('{:>'+str(max_size)+'}').format(str(self.__matrix[i+(j*self.x_size)])) + ' '

            str_out += "|\n"
        return str_out

    def __mul__(self, other):
        assert isinstance(other, (int, float, long, Mat2)), 'Requires a int, float, long or Mat2'
        if isinstance(other, Mat2):
            new_matrix = []
            sm = self.__matrix
            om = other.__matrix

            new_matrix.append(sm[0]*om[0] + sm[1]*om[2])
            new_matrix.append(sm[0]*om[1] + sm[1]*om[3])

            new_matrix.append(sm[2]*om[0] + sm[3]*om[2])
            new_matrix.append(sm[2]*om[1] + sm[3]*om[3])

            return Mat2(new_matrix)
        else:
            self.__matrix = [i*other for i in self.__matrix]
            return self

    def __div__(self, other):
        assert isinstance(other, (int, float, long)), 'Requires a int, float or long'
        self.__matrix = [i/other for i in self.__matrix]
        return self

    def __add__(self, other):
        assert isinstance(other, Mat2), 'Requires a Mat2'
        new_matrix = []
        for i in range(self.size):
            new_matrix.append(self.__matrix[i] + other.__matrix[i])
        return Mat3(new_matrix)

    def __sub__(self, other):
        assert isinstance(other, Mat2), 'Requires a Mat2'

        new_matrix = []
        for i in range(self.size):
            new_matrix.append(self.__matrix[i] - other.__matrix[i])
        return Mat3(new_matrix)

    @property
    def matrix(self):
        return self.__matrix

    def load_zero(self):
        for i in range(self.size):
            self.__matrix[i] = 0
        return self

    def __input_matrix_values(self, values):
        for i, element in enumerate(values):
            self.__matrix[i] = element

    def load_identity(self):
        self.__matrix[0] = 1
        self.__matrix[1] = 0

        self.__matrix[2] = 0
        self.__matrix[3] = 1

        return self

    def transpose(self):
        """
            0, 1            0, 2
            2, 3     ->     1, 3
        """
        self.__matrix[1], self.__matrix[2] = self.__matrix[2], self.__matrix[1]
        return self

    def rotate(self, angle):
        rotation_matrix = self.__rotation_matrix(angle)
        self *= rotation_matrix
        return self

    def __rotation_matrix(self, angle):
        mat = Mat2([]).load_identity()
        sin_angle = math.sin(angle)
        cos_angle = math.cos(angle)
        mat.set_value(cos_angle, 0)
        mat.set_value(-sin_angle, 1)
        mat.set_value(sin_angle, 2)
        mat.set_value(cos_angle, 3)
        return mat


class Mat3:
    """ Creates a 3x3 matrix

        |0, 1, 2|
        |3, 4, 5|
        |6, 7, 8|

    """

    def __init__(self, mat):
        assert isinstance(mat, list) and len(mat) <= 9, 'Requires input to be a list and len <= 9'
        self.__matrix = []
        self.__x_size = 3
        self.__y_size = 3
        self.size = 9

        # Initialise the matrix to zero
        for i in xrange(self.size):
            self.__matrix.append(0)
        self.__input_matrix_values(mat)

    def __str__(self):
        max_size = 0
        for i in self.__matrix:
            if len(str(i)) > max_size:
                max_size = len(str(i))

        str_out = ''
        for j in range(self.__y_size):
            str_out += '| '
            for i in range(self.__x_size):
                str_out += str('{:>'+str(max_size)+'}').format(str(self.__matrix[i+(j*self.__x_size)])) + ' '

            str_out += "|\n"
        return str_out

    def __mul__(self, other):
        assert isinstance(other, (int, float, long, Mat3, Vec2)), 'Requires a int, float, long, Vec2, Mat3'
        if isinstance(other, Mat3):
            new_matrix = []
            sm = self.__matrix
            om = other.__matrix

            new_matrix.append(sm[0]*om[0] + sm[1]*om[3] + sm[2]*om[6])
            new_matrix.append(sm[0]*om[1] + sm[1]*om[4] + sm[2]*om[7])
            new_matrix.append(sm[0]*om[2] + sm[1]*om[5] + sm[2]*om[8])

            new_matrix.append(sm[3]*om[0] + sm[4]*om[3] + sm[5]*om[6])
            new_matrix.append(sm[3]*om[1] + sm[4]*om[4] + sm[5]*om[7])
            new_matrix.append(sm[3]*om[2] + sm[4]*om[5] + sm[5]*om[8])

            new_matrix.append(sm[6]*om[0] + sm[7]*om[3] + sm[8]*om[6])
            new_matrix.append(sm[6]*om[1] + sm[7]*om[4] + sm[8]*om[7])
            new_matrix.append(sm[6]*om[2] + sm[7]*om[5] + sm[8]*om[8])

            return Mat3(new_matrix)

        else:
            self.__matrix = [i*other for i in self.__matrix]
            return self

    def __div__(self, other):
        assert isinstance(other, (int, float, long)), 'Requires a int, float or long'
        self.__matrix = [i/other for i in self.__matrix]
        return self

    def __add__(self, other):
        assert isinstance(other, Mat3), 'Requires a Mat3'
        new_matrix = []
        for i in range(self.size):
            new_matrix.append(self.__matrix[i] + other.__matrix[i])
        return Mat3(new_matrix)

    def __sub__(self, other):
        assert isinstance(other, Mat3), 'Requires a Mat3'

        new_matrix = []
        for i in range(self.size):
            new_matrix.append(self.__matrix[i] - other.__matrix[i])
        return Mat3(new_matrix)

    @property
    def matrix(self):
        return self.__matrix

    def __input_matrix_values(self, values):
        for i, element in enumerate(values):
            self.__matrix[i] = element

    def set_value(self, value, position):
        # Can take in a 1d position or 2d position
        coord = position
        if isinstance(position, list) and len(position) == 2:
            coord = self.convert_2d(position[0], position[1])
        self.__matrix[coord] = value

    def convert_2d(self, x, y):
        # This is used to convert a 2D matrix coords into the 1D representation
        # E.g. for a 3x3 matrix [0][1] (x, y) - > [3] as
        # 0, 1, 2
        # 3, 4, 5
        # 6, 7, 8
        real_coord = self.__x_size*y + x
        return real_coord

    def load_zero(self):
        for i in range(self.size):
            self.__matrix[i] = 0
        return self

    def load_identity(self):
        self.__matrix[0] = 1
        self.__matrix[1] = 0
        self.__matrix[2] = 0

        self.__matrix[3] = 0
        self.__matrix[4] = 1
        self.__matrix[5] = 0

        self.__matrix[6] = 0
        self.__matrix[7] = 0
        self.__matrix[8] = 1

        return self

    def transpose(self):
        """
            0, 1, 2         0, 3, 6
            3, 4, 5     ->  1, 4, 7
            6, 7, 8         2, 5, 8
        """
        self.__matrix[1], self.__matrix[3] = self.__matrix[3], self.__matrix[1]
        self.__matrix[2], self.__matrix[6] = self.__matrix[6], self.__matrix[2]
        self.__matrix[5], self.__matrix[7] = self.__matrix[7], self.__matrix[5]

        return self

    def translate(self, x, y):
        """
            0, 1, 2         0, 0, x
            3, 4, 5     *=  0, 0, y
            6, 7, 8         0, 0, 0
        """
        # TODO - Should translate a vector
        translation_matrix = self.__translation_matrix(x, y)
        self *= translation_matrix
        return self

    def rotate(self, angle):
        rotation_matrix = self.__rotation_matrix(angle)
        self *= rotation_matrix
        return self

    def scale(self, x, y):
        scale_matrix = self.__scale_matrix(x, y)
        self *= scale_matrix
        return self

    def share(self, x, y):
        share_matrix = self.__share_matrix(x, y)
        self *= share_matrix
        return self

    def __share_matrix(self, x, y):
        # 1, x, 0
        # y, 1, 0
        # 0, 0, 1
        mat = Mat3([]).load_identity()
        mat.set_value(x, 1)
        mat.set_value(y, 3)
        return mat

    def __scale_matrix(self, x, y):
        # x, 0, 0
        # 0, y, 0
        # 0, 0, 1
        mat = Mat3([]).load_identity()
        mat.set_value(x, 0)
        mat.set_value(y, 4)
        return mat

    def __translation_matrix(self, x, y):
        mat = Mat3([]).load_identity()
        mat.set_value(x, 2)
        mat.set_value(y, 5)
        return mat

    def __rotation_matrix(self, angle):
        mat = Mat3([]).load_identity()
        sin_angle = math.sin(angle)
        cos_angle = math.cos(angle)
        mat.set_value(cos_angle, 0)
        mat.set_value(-sin_angle, 1)
        mat.set_value(sin_angle, 3)
        mat.set_value(cos_angle, 4)
        return mat



class Mat4:
    """ Creates a 4x4 matrix

        | 0,  1,  2,  3|
        | 4,  5,  6,  7|
        | 8,  9, 10, 11|
        |12, 13, 14, 15|

    """

    def __init__(self, mat):
        assert isinstance(mat, list) and len(mat) <= 16, 'Requires input to be a list and len <= 16'
        self.__matrix = []
        self.__x_size = 4
        self.__y_size = 4
        self.size = 16

        # Initialise the matrix to zero
        for i in xrange(self.size):
            self.__matrix.append(0)
        self.__input_matrix_values(mat)

    def __mul__(self, other):
        assert isinstance(other, (int, float, long, Mat4, Vec4)), 'Requires an int, float, long, Vec4 or Mat4'
        if isinstance(other, Mat4):
            new_matrix = []
            sm = self.__matrix
            om = other.__matrix

            # | 0,  1,  2,  3|              # | 0,  1,  2,  3|
            # | 4,  5,  6,  7|              # | 4,  5,  6,  7|
            # | 8,  9, 10, 11|              # | 8,  9, 10, 11|
            # |12, 13, 14, 15|              # |12, 13, 14, 15|

            new_matrix.append(sm[0]*om[0] + sm[1]*om[4] + sm[2]*om[8] + sm[3]*om[12])
            new_matrix.append(sm[0]*om[1] + sm[1]*om[5] + sm[2]*om[9] + sm[3]*om[13])
            new_matrix.append(sm[0]*om[2] + sm[1]*om[6] + sm[2]*om[10] + sm[3]*om[14])
            new_matrix.append(sm[0]*om[3] + sm[1]*om[7] + sm[2]*om[11] + sm[3]*om[15])

            new_matrix.append(sm[4]*om[0] + sm[5]*om[4] + sm[6]*om[8] + sm[7]*om[12])
            new_matrix.append(sm[4]*om[1] + sm[5]*om[5] + sm[6]*om[9] + sm[7]*om[13])
            new_matrix.append(sm[4]*om[2] + sm[5]*om[6] + sm[6]*om[10] + sm[7]*om[14])
            new_matrix.append(sm[4]*om[3] + sm[5]*om[7] + sm[6]*om[11] + sm[7]*om[15])

            new_matrix.append(sm[8]*om[0] + sm[9]*om[4] + sm[10]*om[8] + sm[11]*om[12])
            new_matrix.append(sm[8]*om[1] + sm[9]*om[5] + sm[10]*om[9] + sm[11]*om[13])
            new_matrix.append(sm[8]*om[2] + sm[9]*om[6] + sm[10]*om[10] + sm[11]*om[14])
            new_matrix.append(sm[8]*om[3] + sm[9]*om[7] + sm[10]*om[11] + sm[11]*om[15])

            new_matrix.append(sm[12]*om[0] + sm[13]*om[4] + sm[14]*om[8] + sm[15]*om[12])
            new_matrix.append(sm[12]*om[1] + sm[13]*om[5] + sm[14]*om[9] + sm[15]*om[13])
            new_matrix.append(sm[12]*om[2] + sm[13]*om[6] + sm[14]*om[10] + sm[15]*om[14])
            new_matrix.append(sm[12]*om[3] + sm[13]*om[7] + sm[14]*om[11] + sm[15]*om[15])

            return Mat4(new_matrix)

        else:
            # v = [self.__matrix[0]*other.x + self.__matrix[1]*other.y + self.__matrix[2]*other.z + self.__matrix[3]*other.w,
            #     self.__matrix[4]*other.x + self.__matrix[5]*other.y + self.__matrix[6]*other.z + self.__matrix[7]*other.w,
            #     self.__matrix[8]*other.x + self.__matrix[9]*other.y + self.__matrix[10]*other.z + self.__matrix[11]*other.w,
            #     self.__matrix[12]*other.x + self.__matrix[13]*other.y + self.__matrix[14]*other.z + self.__matrix[15]*other.w]

            v = [self.__matrix[0]*other.x + self.__matrix[4]*other.y + self.__matrix[8]*other.z + self.__matrix[12]*other.w,
                self.__matrix[1]*other.x + self.__matrix[5]*other.y + self.__matrix[9]*other.z + self.__matrix[13]*other.w,
                self.__matrix[2]*other.x + self.__matrix[6]*other.y + self.__matrix[10]*other.z + self.__matrix[14]*other.w,
                self.__matrix[3]*other.x + self.__matrix[7]*other.y + self.__matrix[11]*other.z + self.__matrix[15]*other.w]
            return Vec4(v[0], v[1], v[2], v[3])

    def __str__(self):
        max_size = 0
        for i in self.__matrix:
            if len(str(i)) > max_size:
                max_size = len(str(i))

        str_out = ''
        for j in range(self.__y_size):
            str_out += '| '
            for i in range(self.__x_size):
                str_out += str('{:>'+str(max_size)+'}').format(str(self.__matrix[i+(j*self.__x_size)])) + ' '

            str_out += "|\n"
        return str_out


    @property
    def matrix(self):
        return self.__matrix

    def __input_matrix_values(self, values):
        for i, element in enumerate(values):
            self.__matrix[i] = element

    def load_identity(self):
        self.__matrix[0] = 1
        self.__matrix[1] = 0
        self.__matrix[2] = 0
        self.__matrix[3] = 0

        self.__matrix[4] = 0
        self.__matrix[5] = 1
        self.__matrix[6] = 0
        self.__matrix[7] = 0

        self.__matrix[8] = 0
        self.__matrix[9] = 0
        self.__matrix[10] = 1
        self.__matrix[11] = 0

        self.__matrix[12] = 0
        self.__matrix[13] = 0
        self.__matrix[14] = 0
        self.__matrix[15] = 1

        return self

    def load_zero(self):
        for i in range(self.size):
            self.__matrix[i] = 0
        return self

    # TODO - Set value should be setter for the matrix
    # TODO - Reverse order, it makes more sense to have index then value like an array a[index] = value
    def set_value(self, value, position):
        # Can take in a 1d position or 2d position
        coord = position
        if isinstance(position, list) and len(position) == 2:
            coord = self.convert_2d(position[0], position[1])
        self.__matrix[coord] = value

    # TODO - Multiple axis
    def rotate_x(self, angle):
        rotation_matrix = self.__rotation_matrix_x(angle)
        self *= rotation_matrix

        return self

    def rotate_y(self, angle):
        rotation_matrix = self.__rotation_matrix_y(angle)
        self *= rotation_matrix
        return self

    def rotate_z(self, angle):
        rotation_matrix = self.__rotation_matrix_z(angle)
        self *= rotation_matrix
        return self

    def translate(self, x, y, z):
        # self.__matrix[3] -= x
        # self.__matrix[7] -= y
        # self.__matrix[11] -= z

        self.__matrix[12] -= x
        self.__matrix[13] -= y
        self.__matrix[14] -= z

        return self

    def __rotation_matrix_x(self, angle):
        mat = Mat4([]).load_identity()
        sin_angle = math.sin(angle)
        cos_angle = math.cos(angle)
        # mat.set_value(cos_angle, 5)
        # mat.set_value(-sin_angle, 6)
        # mat.set_value(sin_angle, 9)
        # mat.set_value(cos_angle, 10)
        mat.set_value(cos_angle, 5)
        mat.set_value(sin_angle, 6)
        mat.set_value(-sin_angle, 9)
        mat.set_value(cos_angle, 10)
        mat.set_value(0, 15)
        return mat

    def __rotation_matrix_y(self, angle):
        mat = Mat4([]).load_identity()
        sin_angle = math.sin(angle)
        cos_angle = math.cos(angle)
        mat.set_value(cos_angle, 0)
        mat.set_value(-sin_angle, 2)
        mat.set_value(sin_angle, 8)
        mat.set_value(cos_angle, 10)
        mat.set_value(0, 15)
        return mat

    def __rotation_matrix_z(self, angle):
        mat = Mat4([]).load_identity()
        sin_angle = math.sin(angle)
        cos_angle = math.cos(angle)
        mat.set_value(cos_angle, 0)
        mat.set_value(sin_angle, 1)
        mat.set_value(-sin_angle, 4)
        mat.set_value(cos_angle, 5)
        mat.set_value(0, 15)
        return mat
